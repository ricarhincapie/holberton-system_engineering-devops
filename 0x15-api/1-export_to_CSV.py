#!/usr/bin/python3

"""Module to fetch data from
https://jsonplaceholder.typicode.com/ API
"""


if __name__ == '__main__':

    import csv
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
        # Creates csv file and gets the writer on
        file_title = empid + ".csv"
        csv_file = open(file_title, 'w')
        header = ['USER_ID', 'USERNAME', 'TASK_COMPLETED', 'TASK_TITLE']
        csv_writer = csv.DictWriter(csv_file, fieldnames=header,
                                    quoting=csv.QUOTE_ALL)

        # Orders data into a dictionary to pass it to csv writter
        my_dict = {"USER_ID": {}, "USERNAME": {},
                   "TASK_COMPLETED": {}, "TASK_TITLE": {}}
        tmp = {}
        print(json_response)
        count = 0
        for task in json_response:
            my_dict.get('USER_ID').update({count: empid})
            my_dict.get('USERNAME').update({count: name})
            my_dict.get('TASK_COMPLETED').update({count:
                                                  task.get('completed')})
            my_dict.get('TASK_TITLE').update({count: task.get('title')})
            count += 1
        # Writes dictionary data in csv format
        goal = 0
        q = "\""
        while goal < count:
            # tmp1 = '"%s"' % str(my_dict.get('USER_ID').get(goal))
            tmp1 = my_dict.get('USER_ID').get(goal)
            tmp2 = my_dict.get('USERNAME').get(goal)
            tmp3 = my_dict.get('TASK_COMPLETED').get(goal)
            tmp4 = my_dict.get('TASK_TITLE').get(goal)
            csv_writer.writerow({'USER_ID': tmp1,
                                'USERNAME': tmp2,
                                'TASK_COMPLETED': tmp3,
                                'TASK_TITLE': tmp4})
            goal += 1
