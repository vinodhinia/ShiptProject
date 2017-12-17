from flask_restful import Resource, reqparse

from models.customer import Customer

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
        import pdb;pdb.set_trace()
        customer_order = Customer.find_by_id(id)
        return{'customer_order': list(map(lambda customer_order: customer_order.json(), customer_order.orders))}
      #  return {'customer_order' : customer_order.orders}