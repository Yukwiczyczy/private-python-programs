import sqlite3

connection = sqlite3.connect("isapi_device.db")
cursor = connection.cursor()
print(cursor.fetchall())

def print_view_list():
    cursor.execute("SELECT * FROM attendance WHERE 1;")
    data = cursor.fetchall() # This returns a list

    for details in data:
        print(details)


def get_view_list():
    cursor.execute("SELECT * FROM attendance WHERE 1;")
    data = cursor.fetchall() # This returns a list
    
    return data


def store_to_db(response: tuple):

    cursor.execute("SELECT * FROM attendance WHERE 1;")
    data = cursor.fetchall() # This returns a list
    print(response)

    employee_id, timestamp_, department, log_type, on_break, shift_ = response
    cursor.execute(f"INSERT INTO attendance VALUES({employee_id}, '{timestamp_}', '{department}', '{log_type}', {on_break}, '{shift_}');")
    connection.commit()

    if data == []:
        employee_id, timestamp_, department, log_type, on_break, shift_ = response
        cursor.execute(f"INSERT INTO attendance VALUES({employee_id}, '{timestamp_}', '{department}', '{log_type}', {on_break}, '{shift_}');")
        connection.commit()
    else:
        employee_id, timestamp_, department, log_type, on_break, shift_ = response
        for details in data:
            if department == details[2] and employee_id == details[0] and timestamp_ == details[1]:
                return 413
            else:
                cursor.execute(f"INSERT INTO attendance VALUES({employee_id}, '{timestamp_}', '{department}', '{log_type}', {on_break}, '{shift_}');")
                connection.commit()
                return 200
