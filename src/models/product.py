from db import db

categories = db.Table('product_category',
                    db.Column('product_id', db.Integer, db.ForeignKey('products.id'), primary_key=True),
                    db.Column('category_id', db.Integer, db.ForeignKey('categories.id'), primary_key=True)
                    )
class Product(db.Model):
    '''products table'''
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))
    price = db.Column(db.Numeric(10,2))

    categories = db.relationship('Category', secondary=categories, lazy='subquery',
        backref=db.backref('productes', lazy=True))

    orders = db.relationship("OrderProduct", back_populates="product")


    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return {'id':self.id, 'name' : self.name, 'price' : round(self.price,2)}

    @classmethod
    def find_by_id(cls,_id):
        return cls.query.filter_by(id = _id).first()

    def save_to_db(self):
        db.session.add(self);
        db.session.commit();