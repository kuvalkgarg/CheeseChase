from flask import Flask, render_template
import pyautogui as pag
import random

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/move_cursor", methods=["GET"])
def move_cursor():
    while True:
        xcor = random.randint(100, 1819)
        ycor = random.randint(100, 979)
        pag.moveTo(xcor, ycor, 2)


if __name__ == "__main__":
    app.run(debug=True)
