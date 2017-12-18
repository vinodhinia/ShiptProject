from db import db
import enum
import json
import datetime

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

class Status(enum.Enum):
    WAITING_FOR_SHIPPING =1
    ON_ITS_WAY = 2
    DELIVERED = 3


class OrderProduct(db.Model):
    __tablename__ = 'order_product'

    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), primary_key=True)
    quantity = db.Column(db.Float)
    cost = db.Column(db.Float)

    product = db.relationship("Product", back_populates="orders")
    order = db.relationship("Order", back_populates="products")

    def __init__(self, quantity, cost=0):
        self.quantity = quantity
        self.cost = cost

class Order(db.Model):
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
        import pdb;pdb.set_trace()
        order_product = self.products
        order_products = []

        for op in order_product:
            order_products.append(int(op.product_id))
        return {'id':self.id, 'status' : self.status._name_ , 'date' : self.date.strftime('%Y-%m-%d'), 'customer_id' : self.customer_id, 'products': order_products}



    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id = _id).first()

    def save_to_db(self):
        import pdb;pdb.set_trace()
        db.session.add(self)
        db.session.commit()




#select orders.id as Order_ID, products.id as Product_id, products.name from orders inner join order_product on orders.id = order_product.order_id inner join products on products.id = order_product.product_id group by orders.id, products.id;
#select orders.id as Order_ID, products.id as Product_id, products.name from orders inner join order_product on orders.id = order_product.order_id inner join products on products.id = order_product.product_id group by orders.id, products.id;


