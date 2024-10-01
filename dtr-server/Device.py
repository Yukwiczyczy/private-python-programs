import requests, requests.auth, json
from Website import store_to_web, get_attendance_list, print_website_list


class BiometricDevice:

    def __init__(self, base_url, login: tuple) -> None:
        self.url = base_url
        self.username, self.password = login


    def get_attendance(self, get_list, department):

        temp_list = []
        for get_record in get_list:
            employee_id = get_record['employeeNoString']
            if employee_id == '00000001':
                employee_id = 2638

            is_break = 0
            label = get_record['label']
            if label == 'Check In':
                label = 'IN'
            elif label == 'Check Out':
                label = 'OUT'
            elif label == 'Break Out':
                label = 'OUT'
                is_break = 1
            elif label == 'Break In':
                label = 'IN'
                is_break = 1

            time = get_record['time']
            date = time[0:10]
            time_get = time[11:18]
            timestamp = f"{date} {time_get}"

            temp_list += [(employee_id, timestamp, department, label, is_break, "Standard Shift")]
        return temp_list

    def get_response(self, timestamp_: tuple):
        date, time_start, time_end = timestamp_

        attendance_list = []

        index = 0        
        index_loop = True        
        # for i in range(stop_position):
        while index_loop:
            data = {
                "AcsEventCond": {
                    "searchID": "320ff782f36c43219fbf7a5f135df0b4",
                    "searchResultPosition": index,
                    "maxResults": 500,
                    "major": 5,
                    "minor": 75,
                    # "startTime": f"2024-07-07T{time_start}+08:00",
                    "startTime": f"{date}T{time_start}+08:00",
                    "endTime": f"{date}T{time_end}+08:00"
                    }
            }

            data_body = json.dumps(data)
            authorization = requests.auth.HTTPDigestAuth(self.username, self.password)
            header_content = {'Content-type': 'application/json'}

            try:
                response = requests.post(url=self.url, headers=header_content, auth=authorization, data=data_body, timeout=5)
                json_data = response.json()
            
                # print(f"Index: {index} Status: {json_data['AcsEvent']['responseStatusStrg']}")
                if response.status_code == 200:
                    if json_data['AcsEvent']['responseStatusStrg'] == "MORE":
                        no_match_counter = 0
                        attendance_list += json_data['AcsEvent']['InfoList']
                    elif json_data['AcsEvent']['responseStatusStrg'] == "OK":
                        no_match_counter = 0
                        attendance_list += json_data['AcsEvent']['InfoList']
                        index_loop = False
                    else:
                        break
                index += 1
            except requests.exceptions.ConnectTimeout:
                return []


            
        return attendance_list

# class1 = BiometricDevice("http://10.10.130.14/ISAPI/AccessControl/AcsEvent?format=json&iv=5109f52944ea77b54529d271f993", ("admin", "icto2024"))
# class1 = BiometricDevice("http://192.168.1.250/ISAPI/AccessControl/AcsEvent?format=json&iv=5109f52944ea77b54529d271f993", ("admin", "icto2024"))
# # class1 = BiometricDevice("http://10.10.130.15/ISAPI/AccessControl/AcsEvent?format=json&iv=5109f52944ea77b54529d271f993", ("admin", "icto2024"))

# response = class1.get_response(("2024-08-27", "00:00:00", "18:00:00"))
# print(response)
# [print(response_) for response_ in response]