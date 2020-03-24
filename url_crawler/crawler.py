import time
import requests_html
from config import config
import logging
from .celery import celery_app


logger = logging.getLogger(__name__)
logger.setLevel(config.log_level)


@celery_app.task
def url_crawler():
    """
        Crawls.
    """
    # Set time
    start = time.time()

    http_session = requests_html.HTMLSession()
    logger.debug("Sending GET request to start_url...")
    start_response = http_session.get(url=config.start_url)
    logger.debug("Received %s response.", start_response.status_code)

    request_count = 1

    # Dict to hold all URLs on the website
    urls = {}

    # Set containing all URLs from the start page
    start_urls = list(start_response.html.absolute_links)
    logger.info("start urls: %s", start_urls)

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
            logger.info("Out of depth: {}".format(current))
            continue

        logger.info("current link: {}".format(current))
        # Get all URLs from the page
        try:
            new_urls = http_session.get(
                current, allow_redirects=True, timeout=15
            ).html.absolute_links
            request_count += 1
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

    http_session.close()

    logger.info("Crawled {} links.".format(len(urls)))
    logger.info(urls)
    logger.debug("Made {} HTTP requests.".format(request_count))

    finish = time.time()
    logger.info("Execution time: {}".format(finish - start))
