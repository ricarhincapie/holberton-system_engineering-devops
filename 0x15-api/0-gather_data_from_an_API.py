#!/usr/bin/python3
"""Module to fetch data from
https://jsonplaceholder.typicode.com/ API"""


if __name__ == '__main__':

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
                name = user.get('name')
        # List with done tasks
        mydone_list = [task for task in json_response
                       if task.get('completed') is True]
        #print(mydone_list)
        print("Employee {} is done with tasks({}/{}):".
              format(name, len(mydone_list), len(json_response)))
        for task in mydone_list:
            print("\t {}".format(task.get('title')))
