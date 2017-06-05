from mongoengine import *


class Inventory(DynamicDocument):
    name = StringField(db_field="Product Name", default=None, required=True)
    quantity = IntField(db_field="Quantity", default=None, required=True)
    price = IntField(db_field="Price", default=None, required=True)

    meta = {
        "db_alias": "inventories"
    }

# if __name__ == '__main__':
#     from pymongo import MongoClient
#
#     client = MongoClient("127.0.0.1", 27017)
#     client = client["inventories"]["inventory"]
#     # client.insert({"Product Name": "Patanjali Aloe Vera Face Pack", "Quantity": 19, "Price": 5})
#     # client.update({'Quantity': 234}, {'Product Name': 'Purifying Neem Face Pack', 'Quantity': 234, 'Price': 10})
#     for doc in client.find({}):
#         print(doc)
