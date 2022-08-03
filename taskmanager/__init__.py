import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

if os.path.exists("env.py"):
    import env

# creating an instance of Flask and by defualt takes __name__ flask module
app = Flask(__name__)
# create 2 app configuration vars
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")

# create instance of the SQLAlchemy class and pass it the instance of the flask app
db = SQLAlchemy(app)

from taskmanager import routes  # noqa