# Practicing Shopping Cart

# 1. Define a products dictionary
# 2. Take user input for which item they would like to add to the cart
# 3. Add the item to the cart
# 4. Show total

products = {
    "1": {
        "name": "Pen",
        "price": 12.99,
        "quantity": 0
    },
    "2": {
        "name": "Notebook",
        "price": 5,
        "quantity": 23
    },
    "3": {
        "name": "Colors",
        "price": 17.25,
        "quantity": 5
    },
    "4": {
        "name": "Ruler",
        "price": 1.5,
        "quantity": 11
    },
    "5": {
        "name": "Correction fluid",
        "price": 4.15,
        "quantity": 55
    }, 
}

print("Shopping Street")

selected_item = input("Enter products number to add it to cart: ")

cart_items = {}

cart_items.update(products[selected_item])

print(f"{cart_items[selected_item]}")