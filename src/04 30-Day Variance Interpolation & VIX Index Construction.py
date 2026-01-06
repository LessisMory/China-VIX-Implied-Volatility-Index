# ============================================================
# Term Structure Interpolation for 30-Day Variance
# ============================================================
# The VIX index represents the market's expectation of
# 30-day forward-looking volatility. When the available
# option maturities do not exactly match 30 days, linear
# interpolation across two maturities is applied.

# Time to maturity for near-term and next-term options
T1 = T.iloc[0]     # Near-term maturity (in years)
T2 = T.iloc[1]     # Next-term maturity (in years)

# Corresponding implied variances
sigma1_sq = implied_variance.iloc[0]
sigma2_sq = implied_variance.iloc[1]

# Target maturity: 30 days expressed in years
T_target = 30 / 365

# Linear interpolation of variance to 30-day horizon
var_30 = (
    (T2 - T_target) / (T2 - T1) * sigma1_sq * T1 +
    (T_target - T1) / (T2 - T1) * sigma2_sq * T2
) * (365 / 30)

# ============================================================
# Volatility Index Scaling
# ============================================================
# Convert the interpolated 30-day variance into an annualized
# volatility index. The index is expressed in percentage terms.

VIX_China = 100 * np.sqrt(var_30)
