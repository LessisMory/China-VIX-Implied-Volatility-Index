# ============================================================
# Forward Index Level Estimation
# ============================================================
# This section estimates the forward level of the underlying
# index using call–put parity. The forward price F plays a
# central role in the VIX-style model-free implied variance
# formula and is used to determine the reference strike K0.

# Separate call and put options
call = df[df['option_type'] == 'C']
put = df[df['option_type'] == 'P']

# Merge call and put options by strike price and maturity
# to apply call–put parity
cp = pd.merge(
    call,
    put,
    on=['strike_price', 'maturity_date', 'date'],
    suffixes=('_call', '_put')
)

# Risk-free interest rate (annualized)
# This rate is typically proxied by short-term interbank rates
r = 0.03

# Time to maturity (in years)
T = cp['T_call']

# Compute the forward price using call–put parity:
# F = K + exp(rT) * (C - P)
cp['F'] = cp['strike_price'] + np.exp(r * T) * (
    cp['close_call'] - cp['close_put']
)

# ============================================================
# Reference Strike K0 Determination
# ============================================================
# K0 is defined as the strike price immediately below the
# forward index level F. It serves as the anchor point in
# the model-free variance calculation.

# Compute the absolute difference between strike and forward price
cp['diff'] = abs(cp['strike_price'] - cp['F'])

# Identify K0 as the strike price minimizing |K - F|
K0 = cp.loc[cp['diff'].idxmin(), 'strike_price']
