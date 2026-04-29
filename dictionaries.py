# Python Dictionaries
car = {
    "name":"Toyota",
    "year": 2006,
    "model": "IST"
}

for key, value in car.items():
    print(f"{key}: {value}")

# Python Nested Dictionaries

cars = {
    "car1": {
        "name":"Toyota",
        "year": 2006,
        "model": "IST"
    },
    "car2": {
        "name":"Mazda",
        "year": 2013,
        "model": "CX5"
    },
    "car3": {
        "name":"Testa",
        "year": 2023,
        "model": "Model X"
    }
}

print()
for x, obj in cars.items():
    print(f"{x}")
    for y in obj:
        print(f"{y}: {obj[y]}")
    print()
    