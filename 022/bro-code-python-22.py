#shopping cart program

foods = []
prices = []
total = 0



while True:
    food = input("Enter a food to buy (q to Quit):")
    if food == "q":
        break
    else:
        price = input(f"enter the price of a {food} $")
        foods.append(food)
        prices.append(price)

print("------- YOUR CART -------")

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price 

print(f"your total is ${total}")