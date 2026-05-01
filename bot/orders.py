from bot.logging_config import get_logger

logger = get_logger()

class OrderService:
    def __init__(self, client):
        self.client = client

    def market_order(self, symbol, side, quantity):
        logger.info(f"Market order: {symbol} {side} {quantity}")

        return self.client.place_order(
            symbol=symbol,
            side=side,
            order_type="MARKET",
            quantity=quantity
        )

    def limit_order(self, symbol, side, quantity, price):
        logger.info(f"Limit order: {symbol} {side} {quantity} {price}")

        return self.client.place_order(
            symbol=symbol,
            side=side,
            order_type="LIMIT",
            quantity=quantity,
            price=price
        )