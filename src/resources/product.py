import StringIO
import csv

import flask
from flask import request
from flask_restful import Resource, reqparse
from models.category import Category
from models.order import Order, OrderProduct
from models.product import Product
import os


class ProductResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name')

    parser.add_argument('price')

    parser.add_argument('category_id')

    def get(self, id):
        #GET the Product by Id
        product = Product.find_by_id(id)
        if product:
            return product.json()
        else:
            return {'message' : 'product not found'}, 404

    def put(self):
        data = ProductResource.parser.parse_args()
        product = Product.find_by_id(data['id'])
        if not product:
            return {'message' : "Prodcut with id: '{}' does not exist. Please create the Product first ".format(id)}
        else:
            product.price = data['price']
            product.save_to_db()
            return product.json()


class ProductListResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name')

    parser.add_argument('price')

    parser.add_argument('category_id')

    def get(self):
        return {'product': list(map(lambda product: product.json(), Product.query.all()))}

    def post(self):
        #POST/ CREATE the product
        product_records = request.json['products']
        product = Product(product_records['name'], product_records['price'])
        category_list = product_records['category_id']
        for c in category_list:
            category = Category.find_by_id(c)
            # import pdb;pdb.set_trace()
            product.categories.append(category)
        product.save_to_db()

        return {'message' : 'Product Created Successfully'}

class ProductSalesResource(Resource):

    def get(self):
        accept_type = request.headers['ACCEPT']
        file_name = 'output.csv'
        file_path = '/home/vinu/TakeHomeProjects'
        dirname = os.path.dirname(os.path.join(file_path,file_name))
        if not os.path.exists(dirname):
            os.makedirs(dirname)

        w_file = open(os.path.join(file_path,file_name), 'w')
        w_file.write('your data headers separated by commas \n')

        args = request.args
        from_date = args['from_date']
        to_date = args['to_date']
        breakdown_by = args['breakdown_by']

        from db import db
        if breakdown_by.lower() == 'day':
            breakdown_type = Order.date
        elif breakdown_by.lower() == 'week':
            breakdown_type = db.func.concat(db.func.week(Order.date), "-", db.func.year(Order.date))
        else:
            breakdown_type = db.func.concat(db.func.month(Order.date), "-", db.func.year(Order.date))

        product = db.session.query(
            Product.id,
            Product.name,
            db.func.sum(OrderProduct.quantity),
            breakdown_type)\
            .join(OrderProduct)\
            .join(Order)\
            .filter(Order.date.between(from_date, to_date))\
            .group_by(Product.id, breakdown_type)

        products_json = []
        csv_file = StringIO.StringIO()

        writer = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(['product_id', 'product_name', 'quantity_sold', breakdown_by])

        if product:
            for prod in product:

                writer.writerow([r for r in prod])

                prod_json = {
                    'product_id' : prod[0],
                    'product_name' :prod[1],
                    'quantity_sold': prod[2],
                    breakdown_by: prod[3]
                }
                products_json.append(prod_json)

        if str(accept_type) =='text/csv':
            response = flask.make_response(csv_file.getvalue())
            response.headers['Content-Disposition'] = 'attachment;  filename=output.csv'
            response.mimetype = 'text/csv'
            return response
        return products_json



