#python calculator *,/,+,-,=.

operator=input("Enter the operator (*,/,+,-,=.):")
Number1=int(input("Enter your 1 number:"))
Number2=int(input("Enter your 2 number:"))

if operator == "+":
    print( Number1 + Number2 )
elif operator == "-":
    print(Number1 - Number2)
elif operator == "/":
    print(Number1 / Number2)
elif operator == "*":
    print(Number1 * Number2)