from base import *

class User(Base):
    __tablename__ = 'users'

    id            = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    username = db.Column(db.String(128),  nullable=False)
    email    = db.Column(db.String(128),  nullable=False, unique=True)
    password = db.Column(db.String(192),  nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email    = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.name)
