import requests_html
from config import config
import logging

logger = logging.getLogger(__name__)


class Crawler:
    def __init__(self):
        """
        Crawls.
        """
        self.http_session = requests_html.HTMLSession()
        logger.debug('Sending GET request to start_url...')
        self.start_response = self.http_session.get(url=config.start_url, headers=config.request_headers)
        logger.debug('Received %s response.', self.start_response.status_code)

        self.request_count = 1

    def get_urls(self):
        # Set to hold all URLs on the website
        urls = {}

        # Set containing all URLs from the start page
        start_urls = list(self.start_response.html.absolute_links)
        logger.info('start urls: %s', start_urls)

        # URLs to visit
        to_visit = start_urls
        while to_visit:

            current = to_visit.pop(0)

            # Stay in domain
            if not config.regex_url.match(current):
                continue

            # Check against the desired level of depth
            depth = urls.get(current, 0)
            if depth == config.max_depth:
                logger.info('Out of depth.')
                continue

            logger.info('current link: %s', current)
            # Get all URLs from the page
            try:
                new_urls = self.http_session.get(current, allow_redirects=True, timeout=30).html.absolute_links
                self.request_count += 1
            except TimeoutError as e:
                logger.exception(e)
                continue
            except OSError as e:
                logger.exception(e)
                continue
            # Add URLs to to_visit if internal and not already in urls
            for link in new_urls:
                if config.regex_url.match(link):
                    if link not in urls:
                        urls[link] = depth + 1
                        to_visit.append(link)

        logger.info('Crawled {} links.'.format(len(urls)))
        logger.info(urls)
        logger.debug('Made {} HTTP requests.'.format(self.request_count))
