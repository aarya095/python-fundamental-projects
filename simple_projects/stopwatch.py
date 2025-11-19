import time

time_to_run = int(input("Enter the time in seconds: "))

while time_to_run != 0:
    time.sleep(1)
    print(time_to_run)
    time_to_run = time_to_run - 1
