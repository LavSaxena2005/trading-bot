# Binance Futures Testnet Trading Bot

## Setup

pip install -r requirements.txt

Add .env file:
BINANCE_API_KEY=test
BINANCE_API_SECRET=test

## Run

Market Order:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

Limit Order:
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000


## Note

Due to Binance Futures Testnet API UI limitations, order execution is mocked.
The structure, validation, logging, and CLI behavior remain identical to real API usage.