import argparse
from bot.client import BinanceClient
from bot.orders import OrderService
from bot.logging_config import get_logger

logger = get_logger()

def main():
    parser = argparse.ArgumentParser(description="Mock Binance Trading Bot")

    parser.add_argument("symbol", type=str)
    parser.add_argument("side", type=str, choices=["BUY", "SELL"])
    parser.add_argument("order_type", type=str, choices=["MARKET", "LIMIT"])
    parser.add_argument("quantity", type=float)
    parser.add_argument("--price", type=float, default=None)

    args = parser.parse_args()

    # INIT MOCK CLIENT
    client = BinanceClient()
    orders = OrderService(client)

    print("\n📦 ORDER REQUEST SUMMARY")
    print(f"Symbol     : {args.symbol}")
    print(f"Side       : {args.side}")
    print(f"Order Type : {args.order_type}")
    print(f"Quantity   : {args.quantity}")

    if args.order_type == "LIMIT":
        print(f"Price      : {args.price}")

    try:
        if args.order_type == "MARKET":
            response = orders.market_order(args.symbol, args.side, args.quantity)
        else:
            if args.price is None:
                raise ValueError("Price is required for LIMIT order")

            response = orders.limit_order(
                args.symbol,
                args.side,
                args.quantity,
                args.price
            )

        print("\n✅ ORDER EXECUTED SUCCESSFULLY")
        print(response)

        logger.info(f"SUCCESS: {response}")

    except Exception as e:
        print("\n❌ ORDER FAILED")
        print(str(e))
        logger.error(str(e))


if __name__ == "__main__":
    main()