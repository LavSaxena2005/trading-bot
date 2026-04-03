# Binance Futures Testnet Trading Bot

## Overview

This is a CLI-based Python trading bot that simulates placing orders on Binance Futures Testnet.

## Features

* Place MARKET and LIMIT orders
* Supports BUY and SELL
* CLI input using argparse
* Input validation
* Logging of requests and responses
* Error handling

---

## Setup

```bash
pip install -r requirements.txt
```

---

## Run Examples

### Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Limit Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000
```

---

## Assumptions

* Only USDT-M Futures pairs supported
* Quantity is assumed valid for testnet
* Binance Testnet API had access issues, so order execution is mocked while maintaining real structure

---

```

* Order response
* Errors (if any)
