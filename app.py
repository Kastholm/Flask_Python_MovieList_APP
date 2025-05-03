# app.py
from flask import Flask, render_template
from api import get_movie, save_movie

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('search.html')

if __name__ == '__main__':

    """ Starter server """
    app.run(debug=True) 