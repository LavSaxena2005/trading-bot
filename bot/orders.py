import logging
import random
import time

def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        logging.info(f"Placing order: {symbol} {side} {order_type} {quantity} {price}")

        # 🔥 MOCK RESPONSE (simulate Binance)
        response = {
            "orderId": random.randint(100000, 999999),
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "status": "FILLED" if order_type == "MARKET" else "NEW",
            "executedQty": quantity,
            "avgPrice": price if price else round(random.uniform(50000, 70000), 2)
        }

        time.sleep(1)  # simulate network delay

        logging.info(f"Response: {response}")
        return response

    except Exception as e:
        logging.error(f"Order failed: {str(e)}")
        raise