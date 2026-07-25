# Built-in Modules
import time

current_time = time.localtime()

def get_current_date():
    """
    Get current date
    """

    current_date = current_time.tm_mday
    current_month = current_time.tm_mon
    current_year = current_time.tm_year

    current_date_msg = f"{current_date}/{current_month}/{current_year}"
    
    return current_date_msg

def get_current_time():
    """
    Get current time
    """

    current_time_minutes = current_time.tm_min
    current_time_hours = current_time.tm_hour
    current_time_seconds = current_time.tm_sec

    current_time_msg = f"{current_time_hours}:{current_time_minutes}:{current_time_seconds}"

    return current_time_msg

if __name__ == '__main__':

    current_date_msg = get_current_date()
    current_time_msg = get_current_time()

    print(f"Today's date in DD/MM/YYYY format is {current_date_msg}.")
    print(f"Time: {current_time_msg}.")