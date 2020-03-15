import logging
import re


# Logger level
log_level = logging.DEBUG

# Starting point URL
start_url = 'https://www.zoomit.ir/'

# Allowed domains
allowed_domains = ['zoomit.ir']

# Regex - URLs to keep
regex_url = re.compile('https://.*zoomit.ir.*')

# HTTP request headers
request_headers = {
    'Host': 'www.zoomit.ir',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:74.0) Gecko/20100101 Firefox/74.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive'
}
