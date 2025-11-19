import time

current_time = time.gmtime()

current_date = current_time.tm_mday
current_month = current_time.tm_mon
current_year = current_time.tm_year

print(f"Today's date in DD/MM/YYYY format is {current_date}/{current_month}/{current_year}.")

for i in range(10):
    current_time = time.gmtime()
    current_time_minutes = current_time.tm_min
    current_time_hours = current_time.tm_hour
    current_time_seconds = current_time.tm_sec
    print(f"Time: {current_time_hours}:{current_time_minutes}:{current_time_seconds}")
    time.sleep(1)