from flask import Flask
from routes.company import company
from routes.clients import clients
from config import DATABASE_CONNECTION_URI

app = Flask(__name__)

# settings
app.config['SECRET_KEY'] = 'dev'
print(DATABASE_CONNECTION_URI)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# no cache
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# SQLAlchemy(app)

app.register_blueprint(company)
# app.register_blueprint(clients)
