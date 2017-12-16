# from db import db
#
# class ProductCategory(db.Model):
#     __table__name = 'product_category'
#
#     id  = db.Column(db.Integer, primary_key = True)
#
#     product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
#     product = db.relationship('Product')
#
#     category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
#     category = db.relationship('Category')
#
#     def __init__(self, product_id, category_id):
#         self.product_id = product_id
#         self.category_id = category_id
#
#     def json(self):
#         return {'product_id' : self.product_id, 'category_id': self.category_id}
#
#     def __init__(self, product_id, category_id):
#         self.product_id = product_id
#         self.category_id = category_id
#
#     @classmethod
#     def find_by_id(cls, id):
#         return cls.query.filter_by(id = id).first()
#
#     def save_to_db(self):
#         db.session.add(self)
#         db.session.commit()
#
#
#
#
