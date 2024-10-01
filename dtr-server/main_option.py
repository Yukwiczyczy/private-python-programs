from dotenv import load_dotenv, find_dotenv
from datetime import datetime
import os, msvcrt, sqlite3
import concurrent.futures
import time

# Local file insertion
from Website import store_to_web, get_attendance_list, print_website_list
# from Database import process_store
from Database import get_view_list, print_view_list, sort_list
from main_display_option import show_instruction
from main_insert import website_data_insertion
from main_insert_db import database_data_insertion
from main_calculate import calculate_execution, calculate_execution_insertion
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
    (os.getenv("ih2_api"), API_login, "IH2")
    ]


# Database Connection and Processes

def loop_menu():
    
    start_time_code = time.time()

    show_instruction()
    current_date = datetime.now()
    
    def continues_clock():
        while True:
            # Set the current time to live current time        
            current_date = datetime.now()
            get_date = current_date.strftime("%Y-%m-%d")
            get_date = current_date.strftime("%Y-%m-%d")
            get_current_time = current_date.strftime("%H:%M:%S")
            start_time = "00:00:00"

            #data need from the live current time
            data = get_date, start_time, get_current_time
            print(f"Current Timestamp: {get_date} - {start_time} - {get_current_time}", end="\r")

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
        # print(f"Current Timestamp: {get_date} - {start_time} - {get_current_time}", end="\r")
        
        # Insert list_attendance from the device response
        def timeline_in(user_input):
            data = get_date, start_time, get_current_time, user_input
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
                    # c = executor.submit(continues_clock)
                    f = executor.submit(device_method, api)
                    # threads.append(f)

        def db_save():
            data = get_date, start_time, get_current_time, get_date
                        
            def device_method(tuple_data):
                location = tuple_data[2]
                temp_attendance = []
                Device = BiometricDevice(tuple_data[0], login=tuple_data[1])
                get_response_list = Device.get_response(data)
                temp_attendance += Device.get_attendance(get_list=get_response_list, department=location)

                return temp_attendance

            # Create threads
            threads = []
            with concurrent.futures.ThreadPoolExecutor() as executor:
                for api in API_URL:
                    f = executor.submit(device_method, api)
                    threads.append(f)
                    
            # Process and print results
            for future in concurrent.futures.as_completed(threads):
                result = future.result()
                for details in result:
                    # Process each detail as needed
                    database_data_insertion(details)

        def timeline_db_save(user_input):
            data = get_date, start_time, get_current_time, user_input
            def device_method(tuple_data: tuple):
                location = tuple_data[2]
                temp_attendance = []
                Device = BiometricDevice(tuple_data[0], login=tuple_data[1]) 
                get_response_list = Device.get_response(data)
                temp_attendance += Device.get_attendance(get_list=get_response_list, department=location)
                
                return temp_attendance

            # DONE: Concurrent Threading - Shorten code of threading
            
            threads = []
            with concurrent.futures.ThreadPoolExecutor() as executor:

                for api in API_URL:
                    f = executor.submit(device_method, api)
                    
                        # Process and print results
            for future in concurrent.futures.as_completed(threads):
                result = future.result()
                for details in result:
                    # Process each detail as needed
                    print(details)
                    database_data_insertion(details)
                        
        insert_message = ""
        if msvcrt.kbhit():
        
            key_pressed = msvcrt.getch()
            if key_pressed == b'6':
                calculate_execution(start_time_code, "program execution")
                print("Thank you for using the system.")
                break
            elif key_pressed == b'1':
                response_, data = get_attendance_list()
                if response_.status_code == 200:
                    print_website_list(data)
                else:
                    print(f"There a problem. {response_}")

                show_instruction()                
            elif key_pressed == b'2':
                # if current_device_attendance() != []:
                #     [print(record) for record in current_device_attendance()]
                #     show_instruction()
                # else:
                #     print("\nThere are no attendance record for today\n")
                print_view_list()
            elif key_pressed == b'3':
                user_date = input("Starting Date [Year-Month-Day]: ")
                timeline_in(user_date)
            elif key_pressed == b'4':
                db_save()
                sort_list()
                show_instruction()
            elif key_pressed == b'5':
                user_date = input("Starting Date [Year-Month-Day]: ")
                sort_list()
                timeline_db_save(user_date)
                show_instruction()
            else:
                print(f"Cannot recognize the key: {key_pressed.decode()}")
                show_instruction()


# START EXECUTION
loop_menu()

