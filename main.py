import logging
from url_crawler import crawler
from config import config


if __name__ == '__main__':

    # Set logging level
    logging.basicConfig(level=config.log_level)

    logging.info('Connecting to site...')
    agent = crawler.Agent()
    session, response = agent.get_session()

    logging.info('Running Crawler...')
    crawl = crawler.Crawler(session, response)
    crawl.get_urls()






