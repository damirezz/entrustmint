#This page contains pages that only renders and have no special function
from flask import Blueprint, render_template

idle = Blueprint('idle', __name__)

@idle.route('/about')
def about_us():
    return "Hello World!"
    return render_template("about.html", title="ENTRUSTMINT")


@idle.route("/")
@app.route("/index", methods=['GET', 'POST'])
def home():
    return render_template("index.html", title="ENTRUSTMINT")