import logging
from config import config
from url_crawler import crawler
from api import api


if __name__ == "__main__":

    # Set logger
    logger = logging.getLogger(__name__)
    logger.setLevel(config.log_level)

    logger.info("Talk to the endpoint at http://localhost:5000/crawler")

    
