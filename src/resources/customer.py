from flask_restful import Resource, reqparse

from models.customer import Customer
from models.category import Category
from models.product import Product
from models.order import Order, OrderProduct


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
        customer = Customer.find_by_id(id)
        if customer:
            return customer.json()
        return {'message' : 'Customer cannot be found'}, 404

    def post(self,id):
        data = CustomerResource.parser.parse_args()
        customer = Customer(data['first_name'], data['last_name'], data['address'])
        customer.save_to_db()
        return customer.json()


    def put(self, id):
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
    def get(self):
        return {'customer' :  list(map(lambda customer: customer.json(), Customer.query.all()))}

class CustomerOrderResource(Resource):
    def get(self, id):
        # import pdb;pdb.set_trace()
        customer_order = Customer.find_by_id(id)
        return{'customer_order': list(map(lambda customer_order: customer_order.json(), customer_order.orders))}

class CustomersOrdersResource(Resource):
    def get(self):
        from db import db
        customers_orders = db.session.query(Order.id,Product.id, Product.name,
                                           Category.id, Category.name, Customer.id, Customer.first_name, OrderProduct.quantity)\
            .join(OrderProduct)\
            .join(Product) \
            .join(Category, Product.categories)\
            .join(Customer, Order.customer)\
            .group_by(Order.id, Product.id, Category.id)

        customers_orders_list = []

        for customer_order_obj in customers_orders:
            print customer_order_obj
            customers_orders_dict = {
                'customer_id' : customer_order_obj[5],
                'customer_name' : customer_order_obj[6],
                'category_id' : customer_order_obj[3],
                'category_name' : customer_order_obj[4],
                'quantity' : customer_order_obj[7]
            }
            customers_orders_list.append(customers_orders_dict)
        return customers_orders_list

