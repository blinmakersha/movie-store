from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
metadata = db.metadata


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(300), nullable=False)
    role = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    orders = db.relationship("Order", backref="orders",
                             lazy=True, cascade="all,delete-orphan")

    def __repr__(self):
        return self.email


class Roles(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    users = db.relationship('User', backref='user',
                            lazy=True, cascade="all,delete-orphan")


cart = db.Table('cart', db.Column('movie', db.Integer, db.ForeignKey(
    'movies.id')), db.Column('orders', db.Integer, db.ForeignKey('orders.id')))


class Movies(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    director = db.Column(db.String(120), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(120), nullable=False)
    kind = db.Column(db.String(120), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=True)
    poster_url = db.Column(db.String(255), nullable=True)
    trailer_url = db.Column(db.String(255), nullable=True)
    price = db.Column(db.Float, nullable=False)
    orders = db.relationship("Order", secondary=cart, back_populates="cart")

    def __repr__(self):
        return self.title


class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    cart = db.relationship("Movies", secondary=cart, back_populates="orders")
    date = db.Column(db.DateTime)
    total = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return str(self.id)
