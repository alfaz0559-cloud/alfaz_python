# module2_exercise2.py

person = {
    "name": "Alice",
    "age": 25,
    "city": "Quatre Bornes"
}

print(person["name"])
print(person["age"])
print(person["city"])

# Add a new key
person["job"] = "Developer"

print(person)

# This causes KeyError
#print(person["country"])

print(person.get("country", "Country not specified"))
