# ============================================================
# Import required libraries
# ============================================================
# Core numerical and data processing libraries
import numpy as np
import pandas as pd
import datetime
from datetime import datetime
import math

# Data access and market data interface
from jqdatasdk import *
auth('*','*')

# ============================================================
# Option Data Retrieval
# ============================================================
# This section retrieves option contract data required for
# constructing a VIX-style implied volatility index.
#
# The dataset includes option prices, strike prices, maturity
# dates, and option types (call/put).

# Retrieve option contract information
df = get_price(
    security='510050.XSHG',
    start_date='2016-01-01',
    end_date='2022-12-31',
    frequency='daily',
    fields=None,
    skip_paused=False,
    fq='none'
)

# Convert date column to datetime format
df['date'] = pd.to_datetime(df['date'])

# ============================================================
# Basic Data Cleaning and Filtering
# ============================================================
# Remove missing values and ensure valid option prices
# to avoid numerical instability in variance calculation.

df = df.dropna()

# Filter out options with non-positive prices
df = df[df['close'] > 0]

# ============================================================
# Option Maturity and Strike Processing
# ============================================================
# Convert option maturity into time-to-maturity (in years),
# which is required in the model-free implied variance formula.

df['maturity_date'] = pd.to_datetime(df['maturity_date'])

# Time to maturity in years (ACT/365 convention)
df['T'] = (df['maturity_date'] - df['date']).dt.days / 365

# Remove expired or near-expired contracts
df = df[df['T'] > 0]
