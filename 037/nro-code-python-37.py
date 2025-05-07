#math-case statement

def is_weekend(day):
    match day:
        case  "sunday":
            return True
        case  "monday":
            return False
        case  "tuesday":
            return False
        case  "wednesday":
            return False
        case  "Thursday":
            return  False
        case  "Friday":
            return False
        case  "saturday":
            return True
        case _:
            return False
    
print(is_weekend)