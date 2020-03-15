import requests_html
from config import config
import logging


class Agent:
    def __init__(self):
        """
        Web agent. Handles session and requests.
        """
        self.http_session = requests_html.HTMLSession()

        logging.debug('Sending GET request to start_url...')
        self.start_response = self.http_session.get(url=config.start_url, headers=config.request_headers)
        logging.debug('Received %s response.', self.start_response.status_code)

    def get_session(self):
        return self.http_session, self.start_response


class Crawler:
    def __init__(self, http_session, start_response):
        """
        Crawls.
        """
        self.http_session = http_session
        self.start_response = start_response

    def get_urls(self):
        # Set to hold all URLs on the website
        urls = set()

        # Set containing all URLs from the start page
        start_urls = self.start_response.html.absolute_links

        # Stay in domain
        for i in start_urls:
            if config.regex_url.match(i):
                urls.add(i)




