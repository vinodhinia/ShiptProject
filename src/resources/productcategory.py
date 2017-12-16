# from flask_restful import Resource, reqparse
#
# from models.productcategory import ProductCategory
#
# class ProductCategoryResource(Resource):
#     parser = reqparse.RequestParser()
#
#     parser.add_argument('product_id',
#                         required=True,
#                         help="This field is required")
#     parser.add_argument('category_id',
#                         required=True,
#                         help="This field is required")
#
#
#
#     def get(self, id):
#         data = ProductCategoryResource.parser.parse_args()
#         product_category = ProductCategory.find_by_id(id)
#         if product_category:
#             return {'productcategory' : product_category.json()}
#         else:
#             return {'message' : 'Product and category mapping does not exist'}, 404
#
#     def post(self, id):
#         data = ProductCategoryResource.parser.parse_args()
#         product_category = ProductCategory( data['product_id'], data['category_id'])
#         product_category.save_to_db()
#         return product_category.json()
#
#
# class ProductCategoryListResource(Resource):
#     def get(self):
#         return {'product_category' : list(map(lambda product_category: product_category.json(), ProductCategory.query.all()))}
