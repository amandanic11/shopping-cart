# shopping_cart.py

# shopping_cart_backup.py

import datetime
import os
import pandas as pd 
import csv
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

now = datetime.datetime.now()

# product_filepath = os.path.join(os.path.dirname(__file__), "product_list.csv")
# product_filename = "product_list.csv"


#set SENDGRID_API_KEY = "environments/sendgrid_api_key.env"
# SENDGRID_API_KEY = os.environ.get("sendgrid_api_key.env", "Oops, please set env var called sendgrid_api_key")
# SENDGRID_TEMPLATE_ID = os.environ.get("sendgrid_template_id.env", "Oops, please set env var called sendgrid_template_id")
# MY_ADDRESS = os.environ.get("my_email_address.env", "Oops, please set env var called my_email_address")

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

#products = pd.read_csv(product_filename)

def to_usd(my_price):
    # """
    # Converts a numeric value to usd-formatted string, for printing and display purposes.

    # Param: my_price (int or float) like 4000.444444

    # Example: to_usd(4000.444444)

    # Returns: $4,000.44
    # """
    return f"${my_price:,.2f}" #> $12,000.71

#User inputs
total_price = 0
product_ids = []

valid_ids = [product["id"] for product in products]

while True:
    product_id = input("Please input a product identifier, or enter DONE when finished: ")
    if product_id == "DONE":
        break
    elif int(product_id) in valid_ids:
        product_ids.append(int(product_id))
    else:    
        print("Identifier not recognized, please try again.")
       

#Program Outputs

print("---------------------------------")
print("THANK YOU FOR SHOPPING AT NOOK'S CRANNY")
print("www.nooks.com")
print("---------------------------------")
print("CHECKOUT AT: " + str(now))
print("---------------------------------")
print("SELECTED PRODUCTS:")

for product_id in product_ids:
        selected_products = [p for p in products if p["id"] == product_id]
        unique_product = selected_products[0]
        total_price = total_price + unique_product["price"]
        price_usd = to_usd(unique_product["price"])
        print(f"+ {str(unique_product['name'])} ({price_usd})")
print("---------------------------------")
subtotal_p = to_usd(total_price)
print("SUBTOTAL: " + str(subtotal_p))
tax_price = to_usd(total_price * 0.0875)
print("TAX (8.75%):" + str(tax_price))
def final_total(total_price, tax):
    return (total_price * tax) + total_price
tax = 0.0875
f_total = to_usd(final_total(total_price, tax))
print(f"TOTAL: {f_total}")
print("---------------------------------")
print("THANK YOU, PLEASE COME AGAIN")
print("---------------------------------")

# template_data = {
#     "total_price_usd": "$14.95",
#     "human_friendly_timestamp": "June 1st, 2019 10:00 AM",
#     "products":[
#         {"id":1, "name": "Product 1"},
#         {"id":2, "name": "Product 2"},
#         {"id":3, "name": "Product 3"},
#         {"id":2, "name": "Product 2"},
#         {"id":1, "name": "Product 1"}
#     ]
#   }

# client = SendGridAPIClient(SENDGRID_API_KEY)
# print("CLIENT: ", type(client))
# message = Mail(from_email=MY_ADDRESS, to_emails=MY_ADDRESS)
# print("MESSAGE", type(message))
# print(SENDGRID_API_KEY)

# message.template_id = SENDGRID_TEMPLATE_ID

# message.dynamic_template_data = template_data

# try:
#     response = client.send(message)
#     print("RESPONSE:", type(response))
#     print(response.status_code)
#     print(response.body)
#     print(response.headers)
# except Exception as e:
#     print("OOPS", e)