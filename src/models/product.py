from db import db
import json
categories = db.Table('product_category',
                    db.Column('product_id', db.Integer, db.ForeignKey('products.id'), primary_key=True),
                    db.Column('category_id', db.Integer, db.ForeignKey('categories.id'), primary_key=True)
                    )


from sqlalchemy.ext.declarative import DeclarativeMeta
class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data) # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float)

    categories = db.relationship('Category', secondary=categories, lazy='subquery',
        backref=db.backref('productes', lazy=True))

    orders = db.relationship("OrderProduct", back_populates="product")


    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return {'id':self.id, 'name' : self.name, 'price' : self.price}

    @classmethod
    def find_by_id(cls,_id):
        return cls.query.filter_by(id = _id).first()

    def save_to_db(self):
        db.session.add(self);
        db.session.commit();






# Master
# Product
# id
# name
# price
#
# Customer (User)
# id
# first_name
# last_name
#
# Category
# id
# name
#
#
# ProductCategory
# id
# product_id FK Product
# category_id FK Category
#
# ProductOrder
# id
# product_id
# quantity float
# Order_id
#
#
# Order
# id
# customer_id
# status
# date
# shipping_id
#
# Shipping
# Address_id
#
# Address
# customer_id
# street
# zip
# apt


