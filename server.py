from flask import Flask, request, jsonify
from flask_cors import CORS
from bs4 import BeautifulSoup
import json
import os
import requests

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def hello():
    return "<h2>Scraping server</h2>"


@app.route('/data', methods=['GET'])
def get_data():
    url = request.args.get('url')
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    img = soup.find("img", class_="media_image_link")
    src = img["src"]
    return src


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 2700))
    # app.run(host='0.0.0.0', port=port)
    app.run(host='127.0.0.1', port=port)
