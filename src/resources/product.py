from flask_restful import Resource, reqparse
import json
from flask import Flask, request

from models.product import Product
from models.category import Category

class ProductResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name')

    parser.add_argument('price')

    parser.add_argument('category_id')

    def get(self, id):
        product = Product.find_by_id(id)
        if product:
            return product.json()
        else:
            return {'message' : 'product not found'}, 404


    def post(self,id):
        product_records = request.json['product']
        # import pdb;pdb.set_trace()
        product = Product(product_records['name'], product_records['price'])
        category_list = product_records['category_id']
        for c in category_list:
            category = Category.find_by_id(c)
            # import pdb;pdb.set_trace()
            product.categories.append(category)
        product.save_to_db()

        return {'message' : 'Product Created Successfully'}

    def put(self, id):
        data = ProductResource.parser.parse_args()
        product = Product.find_by_id(id)
        if not product:
            return {'message' : "Prodcut with id: '{}' does not exist. Please create the Product first ".format(id)}
        else:
            product.price = data['price']
            product.save_to_db()
            return product.json()


class ProductListResource(Resource):
    def get(self):
        return {'product': list(map(lambda product: product.json(), Product.query.all()))}
