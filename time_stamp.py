import time
timestamp = time.strftime('%H:%M:%S')           # SHOWS HOUR MINUTES AND SECOND
print(timestamp)
timestamp1 = int(time.strftime('%H'))            # SHOWS HOUR 
print(timestamp1)
#timestamp1 = int(input("Enter hour\n"))           #if you need to check without current time 
timestamp2 = int(time.strftime('%M'))                # SHOWS  MINUTES 
print(timestamp2)
timestamp3 = int(time.strftime('%S'))                # SHOWS  SECOND
print(timestamp3)

if timestamp1 < 12 and timestamp1 >= 00 :
    print("Good Morning")
elif timestamp1 > 11 and timestamp1 < 18 :
    print("Good Afternoon")
elif timestamp1 > 17 :
    print("Good Evening")