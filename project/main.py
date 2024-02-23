from loguru import logger
from utils.helpers import add

if __name__ == "__main__":
    logger.info(f"1 + 2 = {add(1, 2)}")
