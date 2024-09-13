from dotenv import load_dotenv, find_dotenv
from datetime import datetime, timedelta
import os, msvcrt
import concurrent.futures
import time

# Local file insertion
from main_display import show_instruction
from main_insert import website_data_insertion
from main_calculate import calculate_execution
from Device import BiometricDevice

# Define the file path of the python
env_path = find_dotenv()
# Load the env file
load_dotenv(env_path)

API_login = (os.getenv("API_USERNAME"), os.getenv("API_PASSWORD"))
API_URL = [
    (os.getenv("admin1_api"), API_login, "ADMIN BUILDING 1"),
    (os.getenv("admin2_api"), API_login, "ADMIN BUILDING 2"), 
    (os.getenv("icto_api"), API_login, "ICTO"), 
    (os.getenv("ced_api"), API_login, "CED"), 
    (os.getenv("ccj_api"), API_login, "CCJ"), 
    (os.getenv("ceit_api"), API_login, "CEIT"), 
    (os.getenv("library_api"), API_login, "LIBRARY"), 
    (os.getenv("ih1_api"), API_login, "IH1"), 
    (os.getenv("cas_api"), API_login, "CAS"), 
    (os.getenv("ih2_api"), API_login, "IH2")]

def loop_menu():
    
    start_time_code = time.time()

    show_instruction()
    current_date = datetime.now()

    def current_device_attendance():
        tuple_data = (os.getenv("icto_api"), API_login, "ICTO")
        list_attendance = []
        location = tuple_data[2]
        
        Device = BiometricDevice(tuple_data[0], login=tuple_data[1]) 
        get_response_list = Device.get_response(data)
        list_attendance = Device.get_attendance(get_list=get_response_list, department=location)
        return list_attendance
    
    while True:
        # Set the current time to live current time        
        current_date = datetime.now()
        get_date = current_date.strftime("%Y-%m-%d")
        get_date = current_date.strftime("%Y-%m-%d")
        get_current_time = current_date.strftime("%H:%M:%S")
        start_time = "00:00:00"

        #data need from the live current time
        data = get_date, start_time, get_current_time, get_date
        
        # Insert list_attendance from the device response
        def device_method(tuple_data: tuple):
            location = tuple_data[2]
            temp_attendance = []
            Device = BiometricDevice(tuple_data[0], login=tuple_data[1]) 
            get_response_list = Device.get_response(data)
            temp_attendance += Device.get_attendance(get_list=get_response_list, department=location)

            website_data_insertion(temp_attendance, location )

        # DONE: Concurrent Threading - Shorten code of threading
        threads = []
        with concurrent.futures.ThreadPoolExecutor() as executor:

            for api in API_URL:
                f = executor.submit(device_method, api)

        time.sleep(120)


        insert_message = ""
        if msvcrt.kbhit():
        
            key_pressed = msvcrt.getch()
            if key_pressed == b'0':
                calculate_execution(start_time_code, "program execution")
                print("Thank you for using the system.")
                break
            else:
                print(f"Cannot recognize the key: {key_pressed.decode()}")

                show_instruction()


# START EXECUTION
loop_menu()

