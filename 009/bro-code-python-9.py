#python Temperature

unit=input("Enter Fahrenheit or Celsius :")
Temp=float(input("Enter your Temperature: "))

if unit == "C":
    Temp = round(( 9 * Temp ) / 5 + 32, 1 )
    print(f"your Temperature is {Temp}F")
elif unit == "F":
    Temp = round((Temp - 32) * 5 / 9, 1)
    print(f"your Temperature is {Temp} C")
else:
    print("you are not giving a correct unit")