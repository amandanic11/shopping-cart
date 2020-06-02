# shopping_cart.py

import datetime
now = datetime.datetime.now()

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

def to_usd(my_price):
    # """
    # Converts a numeric value to usd-formatted string, for printing and display purposes.

    # Param: my_price (int or float) like 4000.444444

    # Example: to_usd(4000.444444)

    # Returns: $4,000.44
    # """
    return f"${my_price:,.2f}" #> $12,000.71

# TODO: write some Python code here to produce the desired output

#User inputs
total_price = 0
product_ids = []

while True:
    product_id = input("Please input a product identifier, or enter DONE when finished: ")
    # except ValueError:
    #     print("Identifier not recognized. Please try again.")
    #     continue
    if product_id == "DONE":
        break
    else:    
        product_ids.append(product_id)
       

#Program Outputs

print("---------------------------------")
print("THANK YOU FOR SHOPPING AT NOOK'S CRANNY")
print("www.nooks.com")
print("---------------------------------")
print("CHECKOUT AT: " + str(now))
print("---------------------------------")
print("SELECTED PRODUCTS:")
for product_id in product_ids:
        product_attributes = [p for p in products if str(p["id"]) == str(product_id)]
        unique_product = product_attributes[0]
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