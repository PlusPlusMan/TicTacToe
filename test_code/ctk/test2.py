import datetime as dt
import time as t

#print current time with format HH:MM:SS
#print(dt.datetime.now().strftime("%A, %B, %Y"))
#print(dt.datetime.now().strftime("%H:%M:%S"))

def current_time():
    return dt.datetime.now().strftime("%A, %B, %Y"), dt.datetime.now().strftime("%H:%M:%S")

print(current_time()[1])
