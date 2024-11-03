import time  # Import the time module to work with time-related functions

# Get the current time in the format of Hour:Minute:Second, Date, Timezone
current_time = time.strftime("%X %x %Z")
print(current_time)  # Print the current time and date

# Get the current hour in 24-hour format
current_hour = int(time.strftime("%H"))

# Check the current hour and print the appropriate greeting
if current_hour > 0 and current_hour < 12:
    print("Hi, Good Morning.")  # Morning greeting

elif current_hour >= 12 and current_hour < 16:
    print("Hi, Good Afternoon.")  # Afternoon greeting

else:
    print("Hi, Good Evening.")  # Evening greeting
