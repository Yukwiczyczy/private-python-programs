from datetime import datetime
import time 


def store_log_txt(text: str):
    path = "log.txt"
    file_open = open(path, "r")
    data = file_open.read()
    file_input = open(path, 'a')
    file_input.write(f"{text}\n")

    file_open.close()

current_date = datetime.now()
def calculate_execution(start_time, method):
    end_time = time.time()
    execution = end_time -  start_time

    log_statement = f"[{current_date}] Execution of {method} takes {execution: .3f} seconds"
    print(f"\n{log_statement}\n")
    store_log_txt(log_statement)
    


def calculate_execution_insertion(start_time, method, update_number, department):
    end_time = time.time()
    execution = end_time -  start_time

    log_statement = f"[{current_date}] Execution of {method} in {department} takes {execution: .3f} seconds. Total of list updated: {update_number}\n"
    print(f"\n{log_statement}\n")
    store_log_txt(log_statement)
    