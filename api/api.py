from flask import Flask, request
from url_crawler import crawler
from config import config

app = Flask(__name__)


@app.route("/crawler", methods=["POST"])
def crawler_endpoint():
    if request.method == "POST":
        data = request.form
        url = data['url']
        # check the url against a regex
        if url:
            crawler.url_crawler.delay(url)
            return 'Running\n'
        else:
            return 'Bad URL:{}'.format(url)


app.run()