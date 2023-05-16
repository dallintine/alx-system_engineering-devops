#!/usr/bin/python3
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 21c35ece6033d103b3c189a01f16aaaae15e1f54
"""Exports to-do list information for a given employee ID to JSON format."""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todos]}, jsonfile)
<<<<<<< HEAD
=======
=======
"""Exports data in the JSON format"""

if __name__ == "__main__":

    import json
    import requests
    import sys

    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}/'.format(user_id)
    todos_url = url + 'todos'
    user = requests.get(url).json()
    todos = requests.get(todos_url).json()

    todo_list = []
    for todo in todos:
        new_dict = {}
        new_dict['task'] = todo.get('title')
        new_dict['completed'] = todo.get('completed')
        new_dict['username'] = user.get('username')
        todo_list.append(new_dict)

    todo_dict = {user.get('id'): todo_list}

    file_name = '{}.json'.format(user.get('id'))

    with open(file_name, mode='w') as outfile:
        json.dump(todo_dict, outfile)
>>>>>>> f76b6430d14c5b3cfa515ade96aecd5011262cd8
>>>>>>> 21c35ece6033d103b3c189a01f16aaaae15e1f54
