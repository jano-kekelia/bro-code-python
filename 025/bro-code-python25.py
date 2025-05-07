menu = {
    "pizza":2.00,
    "nachos":4.50,
    "popcorn":5.00,
    "fries":3.00,
    "chips":1.00,
    "pretzel":3.00,
    "soda": 3.00,
    "lemonade": 4.25
}


cart = []
total = 0

print("--------------   MENU    ---------------")
for key, value in menu.items():
    print(f"{key}: ${value:.2f}")
print("--------------   MENU    ---------------")

while True:
    food =  input("select an item (q to quit)")
    if food == "q":
        break
    elif menu.get(food)is not None:
        cart.append(food)

for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"total is: ${total:.2f}")