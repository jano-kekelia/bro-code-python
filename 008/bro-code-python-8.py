#python weight

weight=float(input("Enter your weight:"))
unit=input("Kilograms or pounds (K or P):")


if unit == "k":
    weight = weight * 2.205
    unit = "pound"
    print(f" your weight is {round(weight, 1)}")
elif unit == "p":
    weight = weight / 2.205
    unit = "kilograms"
    print(f"your weight is {round(weight, 1)}")