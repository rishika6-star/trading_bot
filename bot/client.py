import random
import time

class BinanceClient:
    def __init__(self, api_key=None, api_secret=None):
        # MOCK MODE (no real API)
        pass

    def place_order(self, symbol, side, order_type, quantity, price=None):

        order_id = random.randint(100000, 999999)

        response = {
            "orderId": order_id,
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "status": "FILLED" if order_type == "MARKET" else "NEW",
            "executedQty": quantity,
            "avgPrice": price if price else "market_price",
            "timestamp": int(time.time() * 1000)
        }

        return response