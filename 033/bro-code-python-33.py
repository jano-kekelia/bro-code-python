#*args
#**kwargs


#def add(*args):
#    total = 0
 #   for arg in args:
#        total += arg

#print(add(1, 2, 3))



#def display_name(*args):
    #for arg in args:
        #print(arg, end=" ")


#display_name("spongebob", "harold", "squarepents" "III")


#def print_address(**kwargs):
    #for key, value in kwargs.items():
        #print(f"{key}: {value}")

#print_address(street="123 fje st.",apt="100", city="fueu", state="mi", zip="3882",)



def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    
    if "apt" in kwargs:

        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Dr" "davit", "grezilshvili" "III", street="123 fake st", apt="100", city="eeefue", state="Mi", zip="3729")