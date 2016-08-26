from __main__ import app
from flask_sqlalchemy import SQLAlchemy
from db import *

class User(db.Model):

    __tablename__ = "users"
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password     #TODO: hash passwords before putting in db

    def __repr__(self):
        return '<User %r>' % self.username
