#!/usr/bin/python3
"""
Module 0-gather_data_from_an_API
"""
import requests
import sys

if __name__ == '__main__':

    employee_ID = int(sys.argv[1])
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        employee_ID)
    employee_response = requests.get(user_url)
    employee_json = employee_response.json()
    employee_name = employee_json.get('name')
    user_id = employee_json.get('id')
    todo_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        employee_ID)
    todo_json = requests.get(todo_url).json()
    total_tasks = 0
    num_completed_tasks = 0
    completed_tasks = []

    for task in todo_json:
        total_tasks += 1
        if task.get('completed') is True:
            completed_tasks.append(task.get('title'))
            num_completed_tasks += 1

    print("Employee {} is done with tasks({}/{}):".format(employee_name,
          num_completed_tasks, total_tasks))
    for item in completed_tasks:
        print("\t {}".format(item))
