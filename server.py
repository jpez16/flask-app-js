from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.update(
    SQLALCHEMY_DATABASE_URI = "sqlite:///main",
    SQLALCHEMY_TRACK_MODIFICATIONS = True
)

db = SQLAlchemy(app)

class Base(db.Model):

    __abstract__  = True

    id            = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

class User(Base):
    __tablename__ = 'users'

    username = db.Column(db.String(128),  nullable=False)
    email    = db.Column(db.String(128),  nullable=False, unique=True)
    password = db.Column(db.String(192),  nullable=False)

    def __init__(self, username, email, password):

        self.username = username
        self.email    = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.name)

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/register/<string:username>/<string:email>/<string:password>")
def register(username, email, password):
    from datetime import datetime
    date_created = datetime.now()
    date_modified = date_created
    user = User(username, email, password)
    db.session.add(user)
    db.session.commit()
    return ("Hello %s (%s)" % (username, email))

if __name__ == '__main__':
    app.run(debug=True)
