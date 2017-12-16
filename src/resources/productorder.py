# from flask_restful import Resource, reqparse
# from models.productorder import ProductOrder
#
# class ProductOrderResource(Resource):
#     parser = reqparse.RequestParser()
#     parser.add_argument('product_id',
#                         required=True,
#                         help="This field is required")
#     parser.add_argument('order_id',
#                         required = True,
#                         help = "This field is required")
#     parser.add_argument('quantity',
#                         required=True,
#                         help="This field is required")
#     parser.add_argument('cost',
#                         required=True,
#                         help="This field is required")
#
#
#     def get(self,id):
#         product_order = ProductOrder.find_by_id(id)
#         if product_order:
#             return product_order.json()
#         return {'message' : 'Product and Order realtion not found in the database'}
#
#     def post(self, id):
#         data = ProductOrderResource.parser.parse_args()
#         product_order = ProductOrder(data['quantity'], data['cost'], data['product_id'], data['order_id'])
#         product_order.save_to_db()
#         return product_order.json()
#
#
# class ProductOrderListResource(Resource):
#     def get(self):
#         return {'product_order': list(
#             map(lambda product_order: product_order.json(), ProductOrder.query.all()))}