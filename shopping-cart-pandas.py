# shopping_cart_pandas.py
from __future__ import print_function
import datetime
import os
import pandas as pd 
import csv
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import functools


now = datetime.datetime.now()
pd.options.display.float_format = '${:,.2f}'.format

# load_dotenv()
# api_key = os.getenv("SENDGRID_API_KEY", "Oops, please set env var called SENDGRID_API_KEY")
# sendgrid_template = os.getenv("SENDGRID_TEMPLATE", "Oops, please set env var called SENDGRID_TEMPLATE" )
# my_address = os.getenv("MY_EMAIL_ADDRESS", "Oops, please set env var called MY_EMAIL_ADDRESS")

# products = [
#     {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
#     {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
#     {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
#     {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
#     {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
#     {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
#     {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
#     {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
#     {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
#     {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
#     {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
#     {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
#     {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
#     {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
#     {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
#     {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
#     {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
#     {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
#     {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
#     {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
# ] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

# df = pd.DataFrame(products)
# df.to_csv('product_list.csv')
product_filepath = os.path.join(os.path.dirname(__file__), "product_list.csv")
product_filename = "product_list.csv"
products = pd.read_csv(product_filename)

def to_usd(my_price):
    return f"${my_price:,.2f}" #> $12,000.71

#User inputs
total_price = 0
product_ids = []

valid_ids = products["id"]
# print(valid_ids)

while True:
    product_id = input("Please input a product identifier, or enter DONE when finished: ")
    if product_id == "DONE":
        break
    elif int(product_id) in valid_ids:
        product_ids.append(int(product_id))
    else:    
        print("Identifier not recognized, please try again.")
       
idx = []
for i in product_ids:
    idx.append(i - 1)
p2 = products.iloc[idx].rename(columns={'id': 'id','name': 'Name','department': 'department','aisle': 'aisle','price': 'Price'}).reset_index()

#Program Outputs

print("---------------------------------")
print("THANK YOU FOR SHOPPING AT NOOK'S CRANNY")
print("www.nooks.com")
print("---------------------------------")
print("CHECKOUT AT: " + str(now))
print("---------------------------------")
print("SELECTED PRODUCTS:")

print((p2[['Name', 'Price']]).to_string(index=False, header=True, justify={'left'}))

print("---------------------------------")
subtotal_p = p2['Price'].sum()
stotal = to_usd(subtotal_p)
tax = 0.0875
tax_price = float(subtotal_p) * tax
tprice = to_usd(tax_price)
total_price = (float(subtotal_p) * tax) + float(subtotal_p)
print("SUBTOTAL: " + str(stotal))
print("TAX (8.75%):" + str(tprice))
def final_total(total_price, tax):
    return (total_price * tax) + total_price
f_total = to_usd(total_price)
print(f"TOTAL: {f_total}")
print("---------------------------------")
print("THANK YOU, PLEASE COME AGAIN")
print("---------------------------------")