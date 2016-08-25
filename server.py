from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.update(
    SQLALCHEMY_DATABASE_URI = "sqlite:///main",
    SQLALCHEMY_TRACK_MODIFICATIONS = True
)

db = SQLAlchemy(app)

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/register/<string:username>/<string:email>/<string:password>")
def test(username, email, password):
    user = User(username, email, password)
    db.session.add(user)
    db.session.commit()
    return ("Hello %s (%s)" % (username, email))

if __name__ == '__main__':
    app.run(debug=True)
