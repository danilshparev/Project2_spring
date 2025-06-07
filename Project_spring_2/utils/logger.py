import logging

def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        filename="bot.log",
        encoding="utf-8",
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )