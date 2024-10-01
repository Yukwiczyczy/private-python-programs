from Database import store_to_db, get_view_list
from main_calculate import calculate_execution_insertion
import time


def database_data_insertion(tuppled_data):
    
    # print(tuppled_data)
    store_to_db(tuppled_data)
        

