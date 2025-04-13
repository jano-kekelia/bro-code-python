#print(help(str))


full_name=input("Enter your full name:")

if len(full_name) > 10:
    print("your full name contains more then 10 characters")
elif not full_name.find(" ") == -1:
    print("your full name contains spaces")
elif not full_name.isalpha():
    print("your full name contains numbers")
else:
    print(f"Hello {full_name}")