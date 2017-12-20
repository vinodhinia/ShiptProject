from db import db
import enum

class Status(enum.Enum):
    WAITING_FOR_SHIPPING =1
    ON_ITS_WAY = 2
    DELIVERED = 3


class OrderProduct(db.Model):
    '''order_product table'''
    __tablename__ = 'order_product'

    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), primary_key=True)
    quantity = db.Column(db.Numeric(10,2))
    cost = db.Column(db.Numeric(10,2))

    product = db.relationship("Product", back_populates="orders")
    order = db.relationship("Order", back_populates="products")

    def __init__(self, quantity, cost=0):
        self.quantity = quantity
        self.cost = cost

class Order(db.Model):
    '''orders table'''
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key = True)
    status = db.Column(db.Enum(Status))
    date = db.Column(db.DATETIME)

    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    customer = db.relationship('Customer', back_populates = 'orders')

    products = db.relationship("OrderProduct", back_populates="order")

    def __init__(self, status, date, customer_id):
        self.date = date
        self.status = status
        self.customer_id = customer_id

    def json(self):
        order_product = self.products
        order_products = []

        for op in order_product:
            order_products.append(int(op.product_id))
        return {'id':self.id, 'status' : self.status._name_ , 'date' : self.date.strftime('%Y-%m-%d'), 'customer_id' : self.customer_id, 'products': order_products}

    @classmethod
    def find_by_id(cls, _id):
        '''Find Order by ID and return Order Instance'''
        return cls.query.filter_by(id = _id).first()

    def save_to_db(self):
        '''Persist Order information in Database'''
        db.session.add(self)
        db.session.commit()


