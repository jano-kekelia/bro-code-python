#or, not, and.

#or
num1=int(input("enter your number:"))
word1= True

if num1 > 40 or num1 < 0 or word1:
    print("True")
else:
    print("False")

#and

num2=int(input("enter your number:"))
word2=True
if num2 >= 30 and word2:
    print("True")
else:
    print("False")


#not

num3=int(input("enter your number:"))
word3=True

if num3 > 30 and word3:
    print("True")
elif num3 > 10 and not word3:
    print("False")
else:
    print("bye")