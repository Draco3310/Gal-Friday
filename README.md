# Gal-Friday Crypto Trading Bot

## Overview

Gal-Friday is a sophisticated cryptocurrency trading bot designed to operate on the Kraken Cryptocurrency Exchange. The bot aims to maximize profitability while managing risk across multiple cryptocurrencies: Bitcoin (BTC), Ripple (XRP), and Dogecoin (DOGE). It employs a range of strategies and advanced algorithms to make informed trading decisions.

## Features

### Trading Strategies
- Scalping
- Day Trading

### Risk Management
- Value at Risk (VaR)
- Conditional Value at Risk (CVaR)
- Sharpe Ratio

### Rate Limiting
- Dynamic rate limiting to comply with Kraken API limitations.

### Error Handling
- Circuit breaker pattern
- Real-time error tracking with Sentry

### Data Validation
- Extensive data validation and caching using Joblib

### Logging
- Comprehensive logging with a timed rotating file handler

### Testing
- Unit tests with the unittest framework
- Parameterized tests for various trading scenarios

## Installation

### Prerequisites
- Python 3.x
- Kraken account

### Libraries Used
- NumPy
- Pandas
- Joblib
- Sentry
- Backtrader
- TA-Lib
- QuantConnect/Lean

### Setup
1. Clone the repository: `git clone https://github.com/Draco3310/Gal-Friday.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Set environment variables for Kraken API keys.

## Usage

1. Update the `config.ini` file with your trading parameters.
2. Run `main.py` to start the bot.

## Testing

Run `test_modules.py` to execute the test suite.

## Backtesting

Add your backtesting logic to `backtest_strategy.py`.

## Contributing

Please read `CONTRIBUTING.md` for details on contributions.

## License

This project is licensed under the MIT License. See the `LICENSE.md` file for details.
