from flask import Flask, request
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from resources.category import CategoryResource, CategoryListResource
from resources.customer import CustomerResource, CustomerListResource, CustomerOrderResource, CustomersOrdersResource
from resources.order import OrderResource, OrderListResource
from resources.product import ProductResource, ProductListResource, ProductSalesResource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://shipt:shipt123@localhost/shipt_project' #mysql://username:password@server/db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
db = SQLAlchemy(app)


@app.before_first_request
def create_tables():
    db.create_all()

#Basic APIs
api.add_resource(ProductResource, '/product/<int:id>')# GET by product id.  POST/CREATE a product in database
api.add_resource(ProductListResource, '/products') # GET all the products on PRODUCT table

api.add_resource(CategoryResource, '/category/<int:id>') # GET by Category id
api.add_resource(CategoryListResource, '/categories') # GET all the categories
#
api.add_resource(CustomerResource, '/customer/<int:id>') #GET customer by id
api.add_resource(CustomerListResource, '/customers') #GET all the customers in the database
#
api.add_resource(OrderResource, '/order/<int:id>') #GET Order by ID
api.add_resource(OrderListResource, '/orders')  #GET all the the Orders in the database

api.add_resource(CustomerOrderResource,'/customer/<int:id>/orders')

api.add_resource(ProductSalesResource, '/aggregate/product/')
api.add_resource(CustomersOrdersResource, '/customers/orders/')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)

