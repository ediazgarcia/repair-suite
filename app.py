from flask import Flask
from routes.auth import auth
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.register_blueprint(auth)
