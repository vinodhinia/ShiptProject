**Folders**
- seed
- src
  - models
  - resources
  - app.py
- tests



**seed**
- Contains the sample data to populate the database

**src**
- src contains the actual logic for the project

**app.py**
- Contains the URL endpoints.
  - Categories
    - http://localhost/categories - GET all the Categories in the database.POST/CREATE a Category in the database
    - http://localhost/category/{id} - GET Category by Id.
  - Customer
    - http://localhost/customers - GET all the Customers in the database. POST/CREATE a Customer in the database
    - http://localhost/customer/{id} - GET Customer by Id.
  - Products
    - http://localhost/products - GET all the products in the database
    - http://localhost/product/{id} - GET Product by Id. POST/CREATE a Product in the database
  - Orders
    - http://localhost/orders - GET all the Orders in the database. POST/CREATE a Order in the database.
    - http://localhost/order/{id} - GET Order by Id.
  - CustomerOrders
    - http://localhost/customer/{id}/orders GETs all the Orders placed by the customer
  - All Customers Orders
    - http://localhost/customers/orders/ GETs all the orders placed by all the customers.
  - Aggregate of Products sold grouped by category
    - http://localhost/aggregate/product/ GETs the aggregate of all the products by category.

**Additional Questions**
- We want to give customers the ability to create lists of products for one-click ordering of bulk items. How would you design the tables, what are the pros and cons of your approach?
  - One Click ordering speeds up the online shopping process. It remembers the payment and shipping information.
  - Basically PaymentMethod table and Address table will be created to persist the payment method details and address information of the cuctomers.
  - Customer and PaymentMethod table will have one to many relationship.
  - Customer and ShippingAddress tables will have one to many relationship.
- If Shipt knew exact inventory of stores, and when facing a high traffic and limited supply of particular item, how do you distribute the inventory among customers checking out?
  - We need to have a Master Product table which has a column name StockLeft which holds the information of quantity of stock in inventory.
  - Every time user purchases the product the purchased quantity should be reduced from the Master Product.
  - When Product is no more available it must me marked as SOLD Out. Customers should not be allowed to make orders more than quantity of product in inventory.

