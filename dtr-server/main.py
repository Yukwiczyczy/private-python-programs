from Website import store_to_web, get_attendance_list, print_website_list
from Database import get_view_list, print_view_list, store_to_db, store_log
import concurrent.futures, threading, multiprocessing
from Device import BiometricDevice
from datetime import datetime, timedelta
import os, msvcrt
from dotenv import load_dotenv, find_dotenv
import time

<<<<<<< Updated upstream
=======
# Local file insertion
from main_display import show_instruction
from main_insert_db import database_data_insertion
from main_insert import website_data_insertion
from main_calculate import calculate_execution
from Device import BiometricDevice
from Database import sort_list
>>>>>>> Stashed changes

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
# API_URL = [(os.getenv("icto_api"), API_login, "ICTO"), (os.getenv("ced_api"), API_login, "CED")]
# API_URL = [(os.getenv("icto_api"), API_login, "ICTO")]

log_set = {}

def clear_screen():
    os.system("cls")


def isapi_logo():
    print_logo = """
╔═╗┬  ┬╔═╗╦ ╦  ╦┌┐┌┌┬┐┌─┐┬  ┬  ┬┌─┐┌─┐┌┐┌┌┬┐  ╔═╗┌┬┐┌┬┐┌─┐┌┐┌┌┬┐┌─┐┌┐┌┌─┐┌─┐ ╔╦╗┬─┐┌─┐┌─┐┬┌─┌─┐┬─┐
║  └┐┌┘╚═╗║ ║  ║│││ │ ├┤ │  │  ││ ┬├┤ │││ │   ╠═╣ │  │ ├┤ │││ ││├─┤││││  ├┤   ║ ├┬┘├─┤│  ├┴┐├┤ ├┬┘
╚═╝ └┘ ╚═╝╚═╝  ╩┘└┘ ┴ └─┘┴─┘┴─┘┴└─┘└─┘┘└┘ ┴   ╩ ╩ ┴  ┴ └─┘┘└┘─┴┘┴ ┴┘└┘└─┘└─┘  ╩ ┴└─┴ ┴└─┘┴ ┴└─┘┴└─ 
    """
    print(print_logo)

def store_log_txt(text: str):
    path = "log.txt"
    file_open = open(path, "r")
    data = file_open.read()
    file_input = open(path, 'a')
    file_input.write(f"{text}\n")

    file_open.close()


def calculate_execution(start_time, method):
    end_time = time.time()
    execution = end_time -  start_time

    log_statement = f"Execution of {method} takes {execution: .3f} seconds"
    store_log_txt(log_statement)
    
    print(f"\n{log_statement}\n")


def calculate_execution_insertion(start_time, method, update_number, department):
    end_time = time.time()
    execution = end_time -  start_time

    log_statement = f"Execution of {method} in {department} takes {execution: .3f} seconds\n Total of list updated: {update_number}"
    store_log_txt(log_statement)
    
    print(f"\n{log_statement}\n")
    

def website_data_insertion(list_attendance, department):
    start_time = time.time()
    """ Check if there is a not existent data inserted. """
    if_any_false = []
    success_counter = 0
    success = "No message modified"
    not_success = "No message modified"

    for details in list_attendance:
        response_status = store_to_web(details=details)

        # print(details)
        # print(response_status.text)

        if response_status.status_code == 200:
            success_counter += 1
            if_any_false += [True]    
        else:
            if_any_false += [False]
            # print(response_message.text)
            
    if_has_true = any(true for true in if_any_false)

    if if_has_true:
        success = "successfully inserted.\n"
        success = f"{success_counter} list/s " + success
        calculate_execution_insertion(start_time, "data insertion", f"{success_counter} list/s", department)
        return success
    else:
        not_success = f"Error: Data maybe already exists."
        calculate_execution_insertion(start_time, "data insertion", f"{success_counter} list/s", department)
        return not_success


def show_instruction():
    isapi_logo()
    print("""
Press "1" to view the list of the data.
Press "2" to view the list of attendance today.
Press "3" to quit to the automation.\n
            """)


def loop_menu():
    
    start_time_code = time.time()

    show_instruction()
    current_date = datetime.now()

    # Advance first current time added with 15 secs
    get_current_time = current_date.strftime("%H:%M:%S")
    every_15_secs = current_date+ timedelta(seconds=15)
    get_reference_time = every_15_secs.strftime("%H:%M:%S")
    

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


    count_it = 0
    while True:
        # Set the current time to live current time        
        current_date = datetime.now()
        get_date = current_date.strftime("%Y-%m-%d")
        get_date = current_date.strftime("%Y-%m-%d")
        get_current_time = current_date.strftime("%H:%M:%S")
        start_time = "00:00:00"

        #data need from the live current time
        data = get_date, start_time, get_current_time
        # print(f"Current Timestamp: {get_date} - {start_time} - {get_current_time}", end="\r")
        
        # Update list_attendance from the device response

        list_attendance = []
        attendance_container = []

           
        def device_method(tuple_data: tuple):
            location = tuple_data[2]
            temp_attendance = []
            Device = BiometricDevice(tuple_data[0], login=tuple_data[1]) 
            print(data)
            get_response_list = Device.get_response(data)
            temp_attendance+= Device.get_attendance(get_list=get_response_list, department=location)
            # return temp_attendance                    
            insert_message = website_data_insertion(temp_attendance, location )
            print(f"\nAPI: {location} {insert_message}\n")

<<<<<<< Updated upstream
        # DONE: Concurrent 
        # with concurrent.futures.ThreadPoolExecutor() as executor:
=======
            website_data_insertion(temp_attendance, location )
            db_save()
            sort_list()
>>>>>>> Stashed changes

        #     for api in API_URL:
        #         # c = executor.submit(continues_clock)
        #         f = executor.submit(device_method, api)
        #         # list_attendance.append(f)

        if __name__ == '__main__':
            # Create a list to store the thread instances
            threads = []

            # Create and start a thread for each number
            for api in API_URL:
<<<<<<< Updated upstream
                thread = threading.Thread(target=device_method, args=[api])
                threads.append(thread)
                thread.start()
            
            for thread in threads:
                thread.join()
       
        # if __name__ == '__main__':
        #     # Create a list to store the thread instances
        #     threads = []

        #     # Create and start a thread for each number
        #     for api in API_URL:
        #         thread = multiprocessing.Process(target=device_method, args=[api])
        #         # threads.append(thread)
        #         thread.start()
        
=======
                f = executor.submit(device_method, api)
                threads.append(f)
                    
            # Process and print results
            for future in concurrent.futures.as_completed(threads):
                result = future.result()
                for details in result:
                    # Process each detail as needed
                    database_data_insertion(details)
        time.sleep(120)
>>>>>>> Stashed changes

        # for container in list_attendance:
        #     attendance_container = container.result()

        #     print(attendance_container)
            
        
        # for container in list_attendance:
        #     attendance_container = container.result()

        #     # print(attendance_container)
        #     insert_message = website_data_insertion(attendance_container)
        #     print(f"\n{insert_message}\n")

        # time.sleep(15)

        insert_message = ""
        if msvcrt.kbhit():
        
            key_pressed = msvcrt.getch()
            if key_pressed == b'3':
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
                if list_attendance != []:
                    [print(record) for record in list_attendance]
                    show_instruction()
                else:
                    print("\nThere are no attendance record for today\n")
            else:
                print(f"Cannot recognize the key: {key_pressed.decode()}")

                show_instruction()


# START EXECUTION
loop_menu()

