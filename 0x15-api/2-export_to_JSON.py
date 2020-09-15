#!/usr/bin/python3
"""Module to fetch data from
https://jsonplaceholder.typicode.com/ API
"""


if __name__ == '__main__':

    import json
    import requests
    import sys

    empid = sys.argv[1]
    apiurl = "https://jsonplaceholder.typicode.com/"

    if int(empid):
        payload = {'userId': empid}
        response = requests.get(apiurl + "todos", params=payload)
        json_response = response.json()
        # All user info fetching
        response_usr = requests.get(apiurl + "users")
        usr_json_response = response_usr.json()
        # Brings user name
        for user in usr_json_response:
            if user.get('id') == int(empid):
                name = user.get('username')
        # Create .json file
        file_title = empid + ".json"
        json_f = open(file_title, 'w')
        # Dictionary structure to populate with data
        my_dict = {empid: []}
        for task in json_response:
            tmp_dic = {}
            tmp_dic.update({'task': task.get('title')})
            tmp_dic.update({'completed': task.get('completed')})
            tmp_dic.update({'username': name})
            my_dict.get(empid).append(tmp_dic)

        json.dump(my_dict, json_f)
