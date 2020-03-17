import logging
import re

# Logger config
log_level = logging.DEBUG
log_fhandler = logging.FileHandler('url_crawler.log')
log_fhandler.setLevel(log_level)
log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log_fhandler.setFormatter(log_formatter)

root_log = logging.getLogger()
root_log.addHandler(log_fhandler)

# Starting point URL
start_url = 'https://www.zoomit.ir/'

# Allowed domains
allowed_domains = ['zoomit.ir']

# Regex for URLs to keep
regex_url = re.compile('https://' + '.*' + allowed_domains[0] + '.*' + '/')

# Max depth for links
max_depth = 2

# HTTP request headers
request_headers = {
    'Host': 'www.zoomit.ir',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:74.0) Gecko/20100101 Firefox/74.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive'
}
