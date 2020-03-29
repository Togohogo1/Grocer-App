from traceback import format_exc

from flask import Blueprint, redirect, request, url_for, escape

from ..extensions import db
from ..scraper import scrape

user = Blueprint("user", __name__)

@user.route("/")
def index():
    return redirect(url_for('static', filename='index.html'))

NUM_DEFAULT = 25
@user.route("/startup")
def startup():
    try:
        db.create_all()
        scrape(
            request.args.get("num", NUM_DEFAULT),
            "https://grocer-app-flask.herokuapp.com/items",
            "grocer_app/food.csv",
        )
    except Exception as e:
        return f"""
        <h3> Fatal Error </h3>
        <pre> {escape(format_exc())} </pre>
        """
    else:
        return redirect(url_for('static', filename='startup.html'))
