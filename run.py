'''the main ru.py file'''

import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    '''this func renders the index.html file from the templates'''
    return render_template("index.html")


@app.route("/about")
def about():
    '''this func renders the about.html file from the templates'''
    return render_template("about.html")


@app.route("/contact")
def contact():
    '''this func renders the contact.html file from the templates'''
    return render_template("contact.html")


@app.route("/careers")
def careers():
    '''this func renders the contact.html file from the templates'''
    return render_template("careers.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)