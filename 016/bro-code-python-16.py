#python compound interest calculator

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount:"))
    if principle <= 0:
        print("princile can't be less or equal to zero")
        