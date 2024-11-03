import time

current_time = time.strftime("%X %x %Z")
print(current_time)
current_hour = int(time.strftime("%H"))

if current_hour>0 and current_hour<12:
    print("Hi, Good Morning.")

elif current_hour>=12 and current_hour<16:
    print("Hi, Good Afternoon.")

else:
    print("Hi, Good Evening.")