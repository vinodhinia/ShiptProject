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

