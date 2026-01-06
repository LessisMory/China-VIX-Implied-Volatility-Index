# China VIX-Style Implied Volatility Index

This project constructs a VIX-style implied volatility index for the Chinese options market using a model-free variance approach.

Following the CBOE VIX methodology, the index is computed from option prices without assuming any parametric volatility model. The implementation includes option data preprocessing, forward index level estimation via call–put parity, model-free implied variance calculation, and interpolation to a constant 30-day maturity.

The project demonstrates how market expectations of future volatility can be extracted directly from option prices and highlights the role of volatility indices as forward-looking risk indicators.
