import logging
import time
from config import config
from url_crawler import crawler


if __name__ == '__main__':

    # Set time
    start = time.time()

    # Set logging level
    logging.basicConfig(level=config.log_level)

    logging.info('Connecting to site...')
    agent = crawler.Agent()
    session, response = agent.get_session()

    logging.info('Running Crawler...')
    crawl = crawler.Crawler(session, response)
    crawl.get_urls()

    finish = time.time()
    logging.debug('Execution time: {}'.format(finish - start))






