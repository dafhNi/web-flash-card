from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
import pandas
import random
import time

app = Flask(__name__)
Bootstrap(app)

SECONDS =2
next_card = True
data = pandas.read_csv("data/nihongo_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}


def remove_card():
    to_learn.remove(current_card)


@app.route("/")
def home():
    global current_card
    current_card = random.choice(to_learn)
    nihongo = current_card['nihongo']
    return render_template("index.html", nihongo=nihongo)


@app.route("/flip")
def flip():
    global current_card
    english = current_card['english']
    remove_card()
    return render_template("flip.html", english=english)





if __name__ == "__main__":
    app.run(debug=True)
