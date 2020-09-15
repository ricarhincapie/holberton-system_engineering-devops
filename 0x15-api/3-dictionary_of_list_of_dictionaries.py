#!/usr/bin/python3
"""Module to fetch data from
https://jsonplaceholder.typicode.com/ API
"""


if __name__ == '__main__':

    import json
    import requests

    apiurl = "https://jsonplaceholder.typicode.com/"

    response = requests.get(apiurl + "todos")
    json_response = response.json()
    # All user info fetching
    response_usr = requests.get(apiurl + "users")
    usr_json_response = response_usr.json()
    # Brings user name
    user_id = 1
    user_dic = {}
    # Create users dict {userId: username}
    for user in usr_json_response:
        if user.get('id') == user_id:
            user_dic.update({user_id: user.get('username')})
            user_id += 1
    # Create .json file
    json_f = open('todo_all_employees.json', 'w')
    # Dictionary structure to populate with data
    cnt_usr = 1
    my_list = []
    my_dic = {}
    for task in json_response:
        if task.get('userId') == cnt_usr:
            username = user_dic.get(task.get('userId'))
            tmp_dic = {}
            tmp_dic.update({'username': username})
            tmp_dic.update({'task': task.get('title')})
            tmp_dic.update({'completed': task.get('completed')})
            my_list.append(tmp_dic)
        else:
            cnt_usr += 1
            my_dic.update({cnt_usr - 1: my_list})  # Update to each user id
            my_list = []
            username = user_dic.get(task.get('userId'))
            tmp_dic = {}
            tmp_dic.update({'username': username})
            tmp_dic.update({'task': task.get('title')})
            tmp_dic.update({'completed': task.get('completed')})
            my_list.append(tmp_dic)
    my_dic.update({cnt_usr: my_list})
    json.dump(my_dic, json_f)
