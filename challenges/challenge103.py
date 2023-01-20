#!/usr/bin/env python3

from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template
import requests
import random
import html

app = Flask(__name__)

URL = "https://opentdb.com/api.php?amount=10&category=31&difficulty=medium&type=multiple"

resp = requests.get(URL).json()

question_number = random.randint(0, 9)
q = html.unescape(resp["results"][question_number]["question"])
a1 = resp["results"][question_number]["correct_answer"]
a2 = resp["results"][question_number]["incorrect_answers"][0]
a3 = resp["results"][question_number]["incorrect_answers"][1]
a4 = resp["results"][question_number]["incorrect_answers"][2]

@app.route("/")
def index():
    return render_template("103index.html", question = q, answer1 = a1, answer2 = a2, answer3 = a3, answer4 = a4)

@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        return render_template("103correct.html", answer = request.form["answer"])
    elif request.method == "GET":
        return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
