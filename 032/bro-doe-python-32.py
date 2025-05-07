#keyword arguments


#def hello(greeting, title, first, las):
    #print(f"{greeting} {title}{first} {last}")

#hello("Hello", title="Mr.", last="grzelishvili", #first="davit")


#print("1", "2", "3", "4", "5", sep="-")


def get_phone(country, area, first, last):
    return f"{country}--{area}--{first}--{last}"


phone_num = get_phone(country=1, area=123, first=456, last=7890)

print(phone_num)