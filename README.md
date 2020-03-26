# URL Crawler
This projects crawls all URLs found on a website.

Run the Celery worker:
```
celery -A url_crawler.crawler worker -l info
```
Run the the webserver:
```
python3 main.py
```
Send POST request to the crawler endpoint:
```
curl -F 'url=https://www.zoomit.ir/' -X POST http://localhost:5000/crawler
```