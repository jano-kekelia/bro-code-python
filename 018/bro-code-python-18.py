#import time
import time

the_time=int(input("enter the time (in seconds):"))

for i in range(0, the_time):
    print(i)
    time.sleep(0,1)

print("Time's up")

#-----------------------------------------------------------------------------------------------------------------------------------------------------

my_time= int(input("Enter the time (in seconds)"))

for i in range(my_time, 0, -1):
    seconds = i % 60 
    minutes = int( i /60 ) % 60
    hours = int( i / 3600 )% 24
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(0.5)

print("time's up")