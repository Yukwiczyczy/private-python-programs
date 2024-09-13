from Database import store_to_db
from main_calculate import calculate_execution_insertion
import time


def database_data_insertion(list_attendance, department):
    start_time = time.time()
    """ Check if there is a not existent data inserted. """
    if_any_false = []
    success_counter = 0
    success = "No message modified"
    not_success = "No message modified"

    for details in list_attendance:
        response_status = store_to_db(response=details)

        if response_status == 200:
            success_counter += 1
            if_any_false += [True]    
        else:
            if_any_false += [False]
            
    if_has_true = any(true for true in if_any_false)

    if if_has_true:
        success = "successfully inserted.\n"
        success = f"{success_counter} list/s " + success
        calculate_execution_insertion(start_time, "data insertion", f"{success_counter} list/s", department)
        return success
    else:
        calculate_execution_insertion(start_time, "data insertion", f"{success_counter} list/s", department)
