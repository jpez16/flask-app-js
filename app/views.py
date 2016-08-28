from flask import Flask, render_template
from app import app
@app.route('/')
def index():
    return render_template('index.html')


@app.route("/register/<string:username>/<string:email>/<string:password>")
def register(username, email, password):
    from datetime import datetime
    from models.user import *
    date_created = datetime.now()
    date_modified = date_created
    user = User(username, email, password)
    db.session.add(user)
    db.session.commit()
    return ("Hello %s (%s)" % (username, email))
