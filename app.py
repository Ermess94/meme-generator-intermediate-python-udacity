from io import BytesIO
import random
import os
import time
import requests
from flask import Flask, render_template, request
from PIL import Image

from ingestor import Ingestor
from meme_engine import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for file in quote_files:
        quotes += Ingestor().parse(file)

    images_path = "./_data/photos/dog/"

    imgs = []
    for root, dirs, files in os.walk(images_path):
        for file in files:
            imgs.append(os.path.join(root, file))

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """
    url = request.form['image_url'] 
    body = request.form['body'] 
    author = request.form['author'] 

    if not url or not body or not author:
        return 'Bad request', 404

    tmp_file = f'./{time.time()}.png'
    try:
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            image_content = BytesIO(response.content)
            image = Image.open(image_content)
            image.save(tmp_file)
            path = meme.make_meme(tmp_file, body, author)
            return render_template('meme.html', path=path)
        else:
            return f"Failed to download image. Status code: {response.status_code}", 500
    except Exception as e:
            return f"Error during meme generation. Reason: {e}", 500
    finally:
        if os.path.exists(tmp_file):
            os.remove(tmp_file)


if __name__ == "__main__":
    app.run()
