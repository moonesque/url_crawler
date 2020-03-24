import logging
from config import config
from url_crawler import crawler


if __name__ == "__main__":

    # Set logger
    logger = logging.getLogger(__name__)
    logger.setLevel(config.log_level)

    logger.info("Running Crawler...")

    crawler.url_crawler.delay()
