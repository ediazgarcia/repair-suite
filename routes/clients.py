from flask import Blueprint, render_template

clients = Blueprint("clients", __name__)


@clients.route("/")
def home():
    return render_template("admin/index.html")


@clients.route("/new")
def add_client():
    return "add a client"


@clients.route("/update")
def update():
    return "update a client"


@clients.route("/delete")
def delete():
    return "delete a client"
