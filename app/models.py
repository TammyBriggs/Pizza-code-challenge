from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    pizzas = db.relationship('RestaurantPizza', backref='restaurants', cascade='all, delete-orphan')

class Pizza(db.Model):
    __tablename__ = 'pizzas'

    id = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    ingredients = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    restaurants = db.relationship('RestaurantPizza', backref='pizzas', cascade='all, delete-orphan')

class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizzas'

    id = db.Column(db.String(255), primary_key=True)
    pizza_id = db.Column(db.String(255), db.ForeignKey('pizzas.id'), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    @validates('price')
    def validate_price(self, key, price):
        assert 1 <= price <= 30, "Price must be between 1 and 30."
        return price