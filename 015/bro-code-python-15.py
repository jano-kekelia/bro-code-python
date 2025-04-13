#format specifiers


number1= 900
number2= -2
number3= 2.98761123
number4= 1.9
number5= 8.123
number6= 6.93
number7= 3
number8=8.390


print(f"price 1 is {number1:10}")
print(f"price 2 is {number2:<10}")
print(f"price 3 is {number3:>10}")
print(f"price 4 is {number4:^10}")
print(f"price 5 is {number5:+10}")
print(f"price 6 is {number6:.10f}")
print(f"price 7 is {number7:010}")

#also we can combined them 

print(f"price 8 is {number8:+,.9f}")