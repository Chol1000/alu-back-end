#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    # Get the employee's information
    url_user = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(url_user)
    user = user_response.json()

    # Get the employee's TODO list
    url_todos = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todos_response = requests.get(url_todos)
    todos = todos_response.json()

    # Employee name
    employee_name = user.get('name')

    # Completed tasks and total tasks
    completed_tasks = [task.get('title') for task in todos if task.get('completed')]
    total_tasks = len(todos)

    # Display the output
    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task}")

