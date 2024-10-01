import requests, os
from dotenv import find_dotenv, load_dotenv 

data = find_dotenv()
load_dotenv(data)
key_web_api = os.getenv('website_authorization')

def store_to_web(details: tuple):

    id_, timestamp, department, status, on_break, shift = details
    base_url=f'http://192.168.10.130:8080/api/method/hrms.hr.doctype.employee_checkin.employee_checkin.add_log_based_on_employee_field?Key=Value&employee_field_value={id_}&timestamp={timestamp}&device_id={department}&log_type={status}&is_break={on_break}&shift={shift}'
    header_content = {'Authorization' : key_web_api}
    response = requests.post(base_url, headers=header_content)

    return response # Returns either error or json string


# This method returns a tuple
def get_attendance_list():
    base_url = "http://192.168.10.130:8080/api/method/frappe.desk.reportview.get"

    form_data = {
        'doctype': "Employee Checkin",
        'fields': '["`tabEmployee Checkin`.`name`","`tabEmployee Checkin`.`employee_name`","`tabEmployee Checkin`.`employee`","`tabEmployee Checkin`.`log_type`","`tabEmployee Checkin`.`time`"]',
        'filters': [],
        'order_by': "`tabEmployee Checkin`.`modified` asc",
        'start': 0,
        'page_length': 2500,
        'view': "Report",
        'with_comment_count': 1
    }
    
    header_content = {'Authorization' : 'token 5c32c12c5a4874b:3ee7b2e3d7155ff'}

    response = requests.post(url=base_url, data=form_data, headers=header_content)
    response_json = response.json()

    return (response, response_json)


# This method returns a list
def print_website_list(set_response):
    details = set_response

    if details['message'] == []:
        print("No data in the list")
    else:
        set_values  = details['message']['values'] # This returns a list
        
        # Print each list
        for list_ in set_values:
            print(list_)

