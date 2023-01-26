#!/usr/bin/python3
"""
Module 0-gather_data_from_an_API
"""

import json
import requests
from sys import argv

if __name__ == '__main__':

    ID = argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(
        ID)).json()
    username = user.get('username')
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(ID)).json()
    json_filename = ID + ".json"

    tasks = []

    for task in todo:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = username
        tasks.append(task_dict)

    dictionary = {}
    dictionary[ID] = tasks

    with open(json_filename, "w") as json_file:
        json.dump(dictionary, json_file)
