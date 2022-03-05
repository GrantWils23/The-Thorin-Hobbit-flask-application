'''the main ru.py file'''

import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")
def index():
    '''this func renders the index.html file from the templates'''
    return render_template("index.html")


@app.route("/about")
def about():
    '''this func renders the about.html file from the templates'''
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)

    return render_template("about.html", page_title="About", company=data)


@app.route("/about/<member_name>")
def about_member(member_name):
    '''this func will render the pages of the members from about.html'''
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    '''this func renders the contact.html file from the templates'''
    if request.method == "POST":
        flash("Thanks {}, we have recieved your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    '''this func renders the contact.html file from the templates'''
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
