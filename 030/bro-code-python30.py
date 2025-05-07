#function
def happy_birthday(name, age):
    print(f"Happy birthday to {name}")
    print(f"you are {age} years old ")
    print("Happy birthday to you")
    print()

happy_birthday("jano", 25)
happy_birthday("dato", 15)
happy_birthday("andria", 18)


def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"your bill of ${amount:.2f} is due: {due_date}")

display_invoice("joeschmo", 100.01, "01/02")


def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(1, 2))
print(subtract(1, 2))
print(multiply(1, 2))
print(divide(1, 2))






def create_name(first, last):
    first= first.capitalize()
    last= last.capitalize()
    return first + " " + last


full_name = create_name("spongebob", "squarepants")


print(full_name)