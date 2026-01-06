# ============================================================
# Model-Free Implied Variance Calculation
# ============================================================
# This section computes the model-free implied variance using
# a VIX-style formula. The calculation aggregates out-of-the-
# money option prices across strikes, weighted by strike
# spacing, without assuming any specific volatility model.

# Select out-of-the-money (OTM) options
# Calls with strike >= K0 and puts with strike <= K0
otm_calls = call[call['strike_price'] >= K0]
otm_puts = put[put['strike_price'] <= K0]

# Combine OTM calls and puts
otm_options = pd.concat([otm_puts, otm_calls])

# Sort options by strike price
otm_options = otm_options.sort_values(by='strike_price')

# Compute strike spacing ΔK
# ΔK is defined as half the distance between adjacent strikes
otm_options['delta_K'] = otm_options['strike_price'].diff().shift(-1)
otm_options['delta_K'].fillna(method='ffill', inplace=True)

# ============================================================
# Option Price Function Q(K)
# ============================================================
# Q(K) represents the option price used in the variance
# calculation. For OTM options, Q(K) equals:
#   - Put price for strikes below K0
#   - Call price for strikes above K0

otm_options['Q_K'] = np.where(
    otm_options['strike_price'] < K0,
    otm_options['close'],
    otm_options['close']
)

# ============================================================
# Variance Integral Approximation
# ============================================================
# The model-free implied variance is approximated using a
# discretized integral over option prices:
#
# sigma^2 = (2 / T) * sum( ΔK / K^2 * Q(K) )
#           - (1 / T) * ( (F / K0 - 1) ^ 2 )

# First term: weighted sum of option prices
variance_sum = (
    otm_options['delta_K'] /
    (otm_options['strike_price'] ** 2)
    * otm_options['Q_K']
).sum()

# Full model-free implied variance
implied_variance = (
    2 / T.iloc[0] * variance_sum
    - (1 / T.iloc[0]) * ((cp['F'].iloc[0] / K0 - 1) ** 2)
)
