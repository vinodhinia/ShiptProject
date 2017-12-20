from flask_restful import Resource, reqparse

from models.customer import Customer
from sqlalchemy import text


class CustomerResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('first_name',
                        required = True,
                        help = "This field cannot be blank")

    parser.add_argument('last_name',
                        required=True,
                        help="This field cannot be blank")

    parser.add_argument('address',
                        required=True,
                        help="This field cannot be blank")

    def get(self, id):
        '''Get Customer information by ID'''
        customer = Customer.find_by_id(id)
        if customer:
            return customer.json()
        return {'message' : 'Customer cannot be found'}, 404


    def put(self, id):
        '''Update the Customer information by ID'''
        data = CustomerResource.parser.parse_args()
        customer = Customer.find_by_id(id)
        if not customer:
            return {'message' : 'Customer with ID: {} does not exist in the database '.format(id)}, 404
        else:
            customer.first_name = data['first_name']
            customer.last_name = data['last_name']
            customer.address = data['address']

            customer.save_to_db()
            return customer.json()

class CustomerListResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('first_name',
                        required = True,
                        help = "This field cannot be blank")

    parser.add_argument('last_name',
                        required=True,
                        help="This field cannot be blank")

    parser.add_argument('address',
                        required=True,
                        help="This field cannot be blank")

    def get(self):
        '''GET all the Customers'''
        return {'customer' :  list(map(lambda customer: customer.json(), Customer.query.all()))}

    def post(self):
        '''CREATE a new Product in the database'''
        data = CustomerResource.parser.parse_args()
        customer = Customer(data['first_name'], data['last_name'], data['address'])
        customer.save_to_db()
        return customer.json()


class CustomerOrderResource(Resource):
    def get(self, id):
        '''GETs all the orders placed by a Customer'''
        customer_order = Customer.find_by_id(id)
        return{'customer_order': list(map(lambda customer_order: customer_order.json(), customer_order.orders))}

class CustomersOrdersResource(Resource):
    def get(self):
        from db import db
        sql = text('SELECT  customers.id, customers.first_name,'
                   ' categories.id, categories.name,  SUM(order_product.quantity) '
                   'FROM customers '
                   'INNER JOIN orders on customers.id = orders.customer_id '
                   'INNER JOIN order_product ON orders.id = order_product.order_id '
                   'INNER JOIN products on products.id = order_product.product_id '
                   'INNER JOIN product_category on products.id = product_category.product_id '
                   'INNER JOIN categories ON categories.id = product_category.category_id '
                   'GROUP BY customers.id, categories.id;')
        result = db.engine.execute(sql)
        customers_orders = []
        for row in result:
            customer_order = {
                'customer_id' :int(row[0]),
                'customer_name' : str(row[1]), 'category_id': int(row[2]),
                'category_name': str(row[3]) , 'quantity' :round(int(row[4]),2) }
            customers_orders.append(customer_order)

        return customers_orders


