#default arguments


def net_price(list_price, discount=0, tex=0.05):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500))
print(net_price(500, 01))
print(net_price(500, 0.1, 0))



import time


def count(end, start=0):
    for x in range(start, end+1):
        print(x)
    time.sleep(1)
    print("DONE!")


count(30, 15)