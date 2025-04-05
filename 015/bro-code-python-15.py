#while loop

name= input("enter your name:")

while name== "":
    print("name was not enter")
    name = input("enter your name:")
print(f"hello {name}")

#-----------------------------------------------------------------------------------------------------------------------------------------------------

age = int(input("enter your age:"))

while age < 0:
    print("age can't be negative")
    age = int(input("enter your age:"))

print(f"you are {age} year old")
print(f"you are adult because you are {age} years old")