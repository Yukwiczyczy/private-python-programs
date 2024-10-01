import sqlite3

connection = sqlite3.connect("isapi_device.db")
cursor = connection.cursor()
sql_query = """SELECT name FROM sqlite_master  
  WHERE type='table';"""

cursor.execute(sql_query)

print(cursor.fetchall())

# import requests
# from Device import BiometricDevice
# icto_api = "http://192.168.1.250/ISAPI/AccessControl/AcsEvent?format=json"
# API_USERNAME =  "admin"
# API_PASSWORD = "cvsu1906"

# login_credentials = (API_USERNAME, API_PASSWORD)

# test = BiometricDevice(icto_api, login_credentials)
# response = test.get_response(('2024-09-16', '00:00:00', '14:36:10', '2024-09-16'))
# data=test.get_attendance(response, "ICTO")


def print_view_list():
    cursor.execute("SELECT * FROM attendance WHERE 1;")
    data = cursor.fetchall() # This returns a list




def get_view_list():
    cursor.execute("SELECT * FROM attendance WHERE 1;")
    data = cursor.fetchall() # This returns a list
    
    return data



def delete_content():
    cursor.execute("DELETE FROM attendance")
    connection.commit()


def store_to_db(response: tuple):

    # TODO: Data insertion duplication check 
    cursor.execute("SELECT * FROM attendance WHERE 1;")
    data = cursor.fetchall() # This returns a list

    database_halfsize = int(len(data)/2)
    if data == []:
        employee_id, timestamp_, department, log_type, on_break, shift_ = response
        cursor.execute(f"INSERT INTO attendance VALUES({employee_id}, '{timestamp_}', '{department}', '{log_type}', {on_break}, '{shift_}');")
        connection.commit()
    else:
        # last_list = data[len(data)-1]
        employee_id, timestamp_, department, log_type, on_break, shift_ = response
        for details in data:
            if department == details[2] and employee_id == details[0] and timestamp_ == details[1]:
<<<<<<< Updated upstream
                continue
            else:
                cursor.execute(f"INSERT INTO attendance VALUES({employee_id}, '{timestamp_}', '{department}', '{log_type}', {on_break}, '{shift_}');")
                connection.commit()



def store_log(log_statement):
    cursor.execute(f"INSERT INTO logs VALUES('{log_statement}')")
    connection.commit()
=======
                print("Data exists")
                return 413
            else:
                cursor.execute(f"INSERT INTO attendance VALUES({employee_id}, '{timestamp_}', '{department}', '{log_type}', {on_break}, '{shift_}');")
                connection.commit()
                print("Successful")
                return 200


def sort_list():
    data = get_view_list()
    
    sorted_data = sorted(data, key=lambda x: x[1])
    delete_content()
    
    for details in sorted_data:
        store_to_db(details)
        
    print("List sorted!")
        

delete_content()
>>>>>>> Stashed changes
