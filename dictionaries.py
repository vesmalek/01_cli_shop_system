# Python Dictionaries
car = {
    "name":"Toyota",
    "year": 2006,
    "model": "IST"
}

# Python Nested Dictionaries

cars = {
    "car1": {
        "name":"Toyota",
        "year": 2006,
        "model": "IST",
        "price": 1500,
        "quantity": 0
    },
    "car2": {
        "name":"Mazda",
        "year": 2013,
        "model": "CX5",
        "price": 1690,
        "quantity": 12
    },
    "car3": {
        "name":"Testa",
        "year": 2023,
        "model": "Model X",
        "price": 3600,
        "quantity": 5
        
    }
}

print()
for index, (outer_key, inner_dict) in enumerate(cars.items()):
    print(f"{index + 1}. {outer_key}")
    for inner_key, value in inner_dict.items():
        if ((inner_key != "quantity") & (inner_key != "price")):
            print(f"{inner_key}: {value}")
        if (inner_key == "price"):
            if (inner_dict["quantity"] != 0):
                print(f"{inner_key}: {value:.2f}")
        if((inner_key == "quantity")):
            if (not value):
                print(f"Out of Stock")
            else:
                print(f"{inner_key}: {value}")
        
        #print(f"{inner_key}: {value}")
    print()


    