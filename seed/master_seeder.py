import requests;
import json

APP_HOST = 'http://127.0.0.1'
APP_PORT = '5000'
APP_URL = '{}:{}'.format(APP_HOST,APP_PORT)


#API End Points
CATEGORY_API_END_POINT = '{}/{}'.format(APP_URL,'categories')
PRODUCT_API_END_POINT = '{}/{}'.format(APP_URL,'products')
CUSTOMER_API_END_POINT = '{}/{}'.format(APP_URL,'customers')
ORDER_API_END_POINT = '{}/{}'.format(APP_URL,'orders')




product_data = [
	{
		"name" : "Mango",
		"price" : 2.99,
		"category_id" : [1,2]
	},
    {
 		"name" : "Banana",
		"price" : 6.9238309,
		"category_id" : [1,2]
    },
    {
		"name" : "Milk",
		"price" : 1.99,
		"category_id" : [3]
    },
    {
		"name" : "Eggs",
		"price" : 0.99,
		"category_id" : [3,4]
	}
]


category_data =[{
    "name" : "Vegitable"
    },{"name" : "Fruits"}, {"name" : "Meat"}, {"name" : "Dairy"}
]

customer_data = [{
        "first_name": "Bill",
        "last_name": "Clinton",
        "address": "WhiteHouse"
    },{
        "first_name": "Diane",
        "last_name": "Johanson",
        "address": "SunnyVale"
    },{
        "first_name": "Kathy",
        "last_name": "Harington",
        "address": "Santa Clara"
    }
]

order_data =  [{
		"status" : "ON_ITS_WAY",
		"date": "2017-01-01",
		"customer_id" : 2,
		"products" : [{
			"id":1,
			"quantity" : 1.2,
		}, {
			"id":2,
			"quantity" : 3.8,
		}]
	},{
		"status" : "ON_ITS_WAY",
		"date": "2017-01-01",
		"customer_id" : 1,
		"products" : [{
			"id":3,
			"quantity" : 8
		}, {
			"id":4,
			"quantity" : 3
		}]
	},{
		"status" : "DELIVERED",
		"date": "2015-04-10",
		"customer_id" : 3,
		"products" : [{
			"id":2,
			"quantity" : 4
		}, {
			"id":4,
			"quantity" : 3
		}]
	},{
		"status" : "DELIVERED",
		"date": "2015-10-20",
		"customer_id" : 1,
		"products" : [{
			"id":3,
			"quantity" : 3
		}, {
			"id":4,
			"quantity" : 4
		}]
	},{
		"status" : "DELIVERED",
		"date": "2015-11-20",
		"customer_id" : 2,
		"products" : [{
			"id":2,
			"quantity" : 3
		}, {
			"id":1,
			"quantity" : 4
		}]
	},{
		"status" : "DELIVERED",
		"date": "2015-08-20",
		"customer_id" : 3,
		"products" : [{
			"id":2,
			"quantity" : 3
		}, {
			"id":1,
			"quantity" : 4
		}]
	}
]


#Create Categories

for category in category_data:
	#import pdb;pdb.set_trace()
	r = requests.post(CATEGORY_API_END_POINT,data=category)
	if r.status_code != requests.status_codes.codes.OK:
		raise Exception("Category seeding failed")

for customer in customer_data:
	r = requests.post(CUSTOMER_API_END_POINT,data=customer)
	if r.status_code != requests.status_codes.codes.OK:
		raise Exception("Customer seeding failed")

headers = {'Content-type': 'application/json'}
for product in product_data:
	r = requests.post(PRODUCT_API_END_POINT, data=json.dumps({'products': product}), headers=headers)
	if r.status_code != requests.status_codes.codes.OK:
		raise Exception("Product seeding failed")

for order in order_data:
	r = requests.post(ORDER_API_END_POINT, data =json.dumps({'orders': order}), headers=headers)
	if r.status_code != requests.status_codes.codes.OK:
		raise Exception("Order seeding failed")