from loguru import logger

logger.add("trading_bot.log", rotation="1 MB")

def get_logger():
    return logger