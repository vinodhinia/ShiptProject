from flask_restful import Resource, reqparse

from models.order import Order,OrderProduct
from models.product import Product
from flask import request

class OrderResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('status')

    parser.add_argument('date')

    parser.add_argument('customer_id')

    def get(self, id):
        order  = Order.find_by_id(id)
        if order:
            return order.json()
        return {'message' : 'Order does not exist'}



class OrderListResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('status')

    parser.add_argument('date')

    parser.add_argument('customer_id')

    def get(self):
        return {'order' :  list(map(lambda order: order.json(), Order.query.all()))}

    def post(self):
        order_request = request.json['orders']
        order = Order(order_request['status'], order_request['date'], order_request['customer_id'])
        product_list = order_request['products']

        for prod in product_list:
            product = Product.find_by_id(prod['id'])
            order_product = OrderProduct(prod['quantity'], int(prod['quantity'])*product.price)
            order_product.product = product
            order.products.append(order_product)
        order.save_to_db()
        # import pdb;pdb.set_trace()

        return {'message': 'Order created successfully'}
