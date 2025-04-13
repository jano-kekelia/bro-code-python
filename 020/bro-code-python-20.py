#nested loop (outer loop, inner loop.)

rows = int(input("enter rows:"))
columns = int(input("enter columns:"))
symbol = input("enter symbol:")

for i in range(rows):
    for u in range(columns):
        print(symbol, end="; ")
    print() 