from random import randrange

person = [
    {
    "name": "Arild",
    "age": 9,
    "height": 1.34
    },
    {
    "name": "ingvild",
    "age": 16,
    "height": 1.60
    },
    {
    "name": "Aashild",
    "age": 86,
    "height": 1.70
    }
    ]

winner = person[1]["name"]



i = randrange(3)
name = person[i]["name"]
age = person[i]["age"]
print(f"The winner is {name}!. They are {age} years old.")