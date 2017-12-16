# from db import db
#
# class ProductOrder(db.Model):
#     __tablename__ = 'product_order'
#
#     id = db.Column(db.Integer, primary_key = True)
#     quantity = db.Column(db.Float(precision=2))
#     cost = db.Column(db.Float)
#
#     product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
#     product = db.relationship('Product')
#
#     order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
#     order = db.relationship('Order')
#
#     def __init__(self, quantity, cost, product_id, order_id):
#         self.cost = cost
#         self.quantity = quantity
#         self.product_id = product_id
#         self.order_id = order_id
#
#     @classmethod
#     def find_by_id(cls, id):
#         return cls.query.filter_by(id = id)
#
#     def json(self):
#         return {'quantity' : self.quantity, 'cost' : self.cost, 'product_id' :self.product_id, 'order_id' : self.order_id}
#
#
#     def save_to_db(self):
#         db.session.add(self)
#         db.session.commit()