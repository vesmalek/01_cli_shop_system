choice = ""
products = {
    "1":{
        "Name": "iPhone 17 Pro Max",
        "Price": 1950,
        "Quantity": 3
    },
    "2":{
        "Name": "Notebook",
        "Price": 4.99,
        "Quantity": 12
    },
    "3":{
        "Name": "Adidas Running Shoe",
        "Price": 55,
        "Quantity": 7
    },
    "4":{
        "Name": "Avocadoes (1kg)",
        "Price": 7.50,
        "Quantity": 0
    },
    "5":{
        "Name": "5L Shower Gel",
        "Price": 33.50,
        "Quantity": 24
    },
    "6":{
        "Name": "Toothpaste 50g",
        "Price": 2.45,
        "Quantity": 42
    }
}

while True:
    # menu start
    print()
    print("="*28)

    print("       ISMAIL'S SHOP")

    print("="*28)

    print("1. View Products")
    print("2. Add Item to Cart")
    print("3. View Cart")
    print("4. Remove Item from Cart")
    print("5. Apply Discount Code")
    print("6. Checkout")
    print("7. Exit")

    print("="*28)

    #menu end

    choice = input("Enter your choice: ")
    if choice.strip() == "7":
        print("Goodbye!")
        break
    elif choice.strip() == "1":
        print()
        print("~"*28)
        print("VIEW PRODUCTS")
        print("~"*28)
        print()

        for outer_key, inner_dict in products.items():
            name = inner_dict['Name']

            price = (f"Price: ${inner_dict['Price']:.2f}" if inner_dict['Quantity'] else "N/A")

            quantity = (f"Quantity: {inner_dict['Quantity']}" if inner_dict['Quantity'] else "[Out of Stock]")

            print(f"{outer_key}. {name:<22}{price:<18}{quantity}")
    elif choice.strip() == "2":
        print()
        print("~"*28)
        print("ADD ITEM TO CART")
        print("~"*28)
        print()

        cart_items = []

        while True:
            item = input("Enter product number to add item to cart: ")
            cart_items.append(item)
            wanna_continue = input("Wanna add more items? Press 1 for YES, any other key for NO ")
            
            if wanna_continue.strip() == "1":
                continue
            else:
                print("Exiting...")
                break
            
        print(cart_items)
    elif choice.strip() == "3":
        print("View Cart - coming soon")
    elif choice.strip() == "4":
        print("Remove Item from Cart - coming soon")
    elif choice.strip() == "5":
        print("Apply Discount Code - coming soon")
    elif choice.strip() == "6":
        print("Checkout - coming soon")
    else:
        print("Invalid choice. Please enter 1 - 7")
print()