from flask_restful import Resource, reqparse

from models.order import Order
from models.product import Product
from flask import Flask, request

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
        for prod in product_list:
            product = Product.find_by_id(prod)
            order.products.append(product)
        order.save_to_db()
        return {'message': 'Order created successfully'}  # DATE shoulb be taken care


class OrderListResource(Resource):
    def get(self):
        return {'order' :  list(map(lambda order: order.json(), Order.query.all()))}