from flask import Blueprint, render_template

company = Blueprint('company', __name__)


@company.route("/")
def home():
    return render_template("admin/settings.html")


@company.route("/new")
def add_company():
    return "add a company"


@company.route("/update")
def update():
    return "update a company"


@company.route("/delete")
def delete():
    return "delete a company"
