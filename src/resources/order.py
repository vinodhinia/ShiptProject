from flask_restful import Resource, reqparse

from models.order import Order,OrderProduct
from models.product import Product
#from models.customer import Customer
from flask import Flask, request
from models.order import AlchemyEncoder
import json

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

    def post(self, id):
        order_request = request.json['orders']
        order = Order(order_request['status'], order_request['date'], order_request['customer_id'])
        product_list = order_request['products']

        # customer = Customer.find_by_id(order_request['customer_id'])
        for prod in product_list:
            product = Product.find_by_id(prod['id'])
            order_product = OrderProduct(prod['quantity'], int(prod['quantity'])*product.price)
            order_product.product = product
            order.products.append(order_product)
        order.save_to_db()
        import pdb;pdb.set_trace()
        # customer.orders.append(order)
        # customer.save_to_db()
        return {'message': 'Order created successfully'}  # DATE shoulb be taken care


class OrderListResource(Resource):
    def get(self):
        return {'order' :  list(map(lambda order: order.json(), Order.query.all()))}