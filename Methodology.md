# China VIX: Methodology and Market Adaptation

## 1. Project Overview

This project constructs a VIX-style implied volatility index for the Chinese options market. The index is designed to capture the market’s risk-neutral expectation of future volatility over a 30-day horizon.

The methodology closely follows the CBOE VIX framework, while adapting key components to reflect the characteristics of the Chinese options market, including contract specifications, maturity structure, and market conventions.

---

## 2. Methodological Framework

### 2.1 Option Data Preprocessing

Option contracts are filtered to remove invalid or illiquid observations. Only options with positive prices and non-zero time to maturity are retained. Time to maturity is computed using an ACT/365 convention.

This preprocessing step is essential because the model-free variance formula is highly sensitive to noisy or mispriced option data.

---

### 2.2 Forward Index Level Estimation

The forward index level is estimated using call–put parity. For options sharing the same strike price and maturity, the forward price is computed as:

\[
F = K + e^{rT}(C - P)
\]

The reference strike \(K_0\) is defined as the strike price immediately below the estimated forward level. This step ensures that the implied variance calculation is centered around the risk-neutral forward price of the underlying.

---

### 2.3 Model-Free Implied Variance Calculation

Following the VIX methodology, the implied variance is computed using a discretized integral over out-of-the-money option prices:

\[
\sigma^2 = \frac{2}{T} \sum \frac{\Delta K}{K^2} Q(K)
- \frac{1}{T} \left( \frac{F}{K_0} - 1 \right)^2
\]

This approach extracts the market’s expectation of future variance without assuming any specific stochastic volatility model.

---

### 2.4 Constant-Maturity Interpolation

Because listed option maturities rarely correspond exactly to a 30-day horizon, implied variances from two adjacent maturities are interpolated to obtain a constant 30-day variance. The resulting value is annualized and transformed into a volatility index.

---

## 3. Interpretation of the Volatility Index

The resulting index reflects the market’s forward-looking assessment of uncertainty. Unlike historical volatility, the implied volatility index incorporates investor risk preferences and tail-risk expectations embedded in option prices.

As a result, the index serves as a real-time barometer of market sentiment and systemic risk.

---

## 4. Comparison with the CBOE VIX

### 4.1 Key Similarities

- Both indices rely on a **model-free implied variance framework**
- Both aggregate **out-of-the-money option prices across strikes**
- Both represent **30-day forward-looking volatility expectations**
- No parametric volatility model is assumed

---

### 4.2 Key Differences

| Dimension | CBOE VIX | China VIX (This Project) |
|---------|---------|--------------------------|
| Underlying | S&P 500 Index | Chinese equity index / ETF |
| Market structure | Highly liquid, mature | Relatively younger, less liquid |
| Option availability | Dense strike grid | Coarser strike spacing |
| Risk-free proxy | US Treasury yield | Domestic interbank rate |
| Contract conventions | US-style standards | Adapted to Chinese market rules |

These differences necessitate careful adaptation of the VIX methodology when applied to the Chinese market.

---

## 5. Limitations and Practical Considerations

- Option liquidity constraints may introduce noise into the variance estimation
- Market-specific features such as trading halts and price limits can affect option pricing
- Linear interpolation assumes smooth variance term structure, which may not always hold

Despite these limitations, the index provides a meaningful approximation of market-implied volatility in the Chinese context.

---

## 6. Conclusion

This project demonstrates how a VIX-style volatility index can be constructed for the Chinese options market using a transparent and model-free approach. The framework provides valuable insights into market expectations and serves as a foundation for volatility research, risk management, and derivative pricing applications.
