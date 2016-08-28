from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.update(
    SQLALCHEMY_DATABASE_URI = "sqlite:///main",
    SQLALCHEMY_TRACK_MODIFICATIONS = True
)

db = SQLAlchemy(app)
from app import views, models
