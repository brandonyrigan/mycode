#!/usr/bin/env python3

from flask import Flask
from flask import redirect
from flask import request
from flask import render_template
import requests

app = Flask(__name__)

URL = "https://opentdb.com/api.php?amount=1&category=27&difficulty=medium&type=multiple"

resp = requests.get(URL).json()

@app.route("/")
def index():
    return render_template("103index.html", question = resp["question"], answer1 = resp["correct_answer"], answer2 = resp["incorrect_answers"][0], answer3 = resp["incorrect_answers"][1], answer4 = resp["incorrect_answers"][2])


@app.route("/wrong")
def wrong():
    return "Wrong answer"

@app.route("/correct")
def correct():
    return "Correct!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
