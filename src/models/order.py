from db import db
import enum

products = db.Table('order_product',
                    db.Column('product_id', db.Integer, db.ForeignKey('product.id'), primary_key=True),
                    db.Column('order_id', db.Integer, db.ForeignKey('order.id'), primary_key=True),
                    db.Column('quantity', db.Float),
                    db.Column('cost', db.Float)
                    )

class OrderStatus(enum.Enum):
    ON_ITS_WAY = 1
    DELIVERED = 2

class Order(db.Model):
    __tablename__ = 'order'

    id = db.Column(db.Integer, primary_key = True)
    status = db.Column(db.Enum(OrderStatus))
    date = db.Column(db.DATE)

    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    customer = db.relationship('Customer')

    products = db.relationship('Product', secondary=products, lazy='subquery',
                                 backref=db.backref('orders', lazy=True))

    def __init__(self, status, date, customer_id):
        self.date = date
        self.status = status
        self.customer_id = customer_id

    def json(self):
        return {'id':self.id, 'status' : self.status , 'date' : self.date, 'customer_id' : self.customer_id}


    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id = _id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

