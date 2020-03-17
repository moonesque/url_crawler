import logging
import time
from config import config
from url_crawler import crawler


if __name__ == '__main__':

    # Set time
    start = time.time()

    # Set logger
    logger = logging.getLogger(__name__)
    logger.setLevel(config.log_level)

    logger.info('Running Crawler...')
    crawl = crawler.Crawler()
    crawl.get_urls()

    finish = time.time()
    logger.debug('Execution time: {}'.format(finish - start))






