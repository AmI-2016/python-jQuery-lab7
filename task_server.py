#!/usr/bin/python

"""
Created on Apr 13, 2015
@author: Luigi De Russis
"""

from flask import Flask, jsonify, abort, request, Response, render_template
from flask_bootstrap import Bootstrap  # needed for the simple web client, only

import db_interaction

app = Flask(__name__)

# ---------- SIMPLE CLIENT ----------
Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


# ---------- REST SERVER ----------
@app.route('/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    # init
    tasks = []

    # get the task list from the db
    task_list = db_interaction.get_tasks()

    # prepare the task list for jsonify
    for item in task_list:
        task = prepare_for_json(item)
        tasks.append(task)

    # return the task data
    return jsonify({'tasks': tasks})


@app.route('/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    # get the task
    task = db_interaction.get_task(int(task_id))

    # return 404 not found if no task has the given id
    if task is None:
        abort(404)
        # convert the task in a JSON representation
    return jsonify({'task': prepare_for_json(task)})


@app.route('/api/v1.0/tasks', methods=['POST'])
def insert_task():
    # get the request body
    add_request = request.json

    # check whether a task is present in the request or not
    if (add_request is not None) and ('description' in add_request) and ('urgent' in add_request):
        text = add_request['description']
        urgent = add_request['urgent']

        # insert in the database
        db_interaction.insert_task(text, urgent)

        return Response(status=200)

    # return an error in case of problems
    abort(403)


@app.route('/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):

    # get the request body
    add_request = request.json

    # check whether a task is present in the request or not
    if add_request is not None and ('description' and 'urgent') in add_request:
        text = add_request['description']
        urgent = add_request['urgent']
        # update the task
        task = db_interaction.update_task(int(task_id),text,urgent)

        return Response(status=200)

    # return an error in case of problems
    abort(403)


@app.route('/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):

    # delete the task
    task = db_interaction.remove_task_by_id(int(task_id))

    return Response(status=200)



def prepare_for_json(item):
    """
    Convert the task in a dictionary for easing the JSON creation
    """
    task = dict()
    task['id'] = item[0]
    task['description'] = item[1]
    task['urgent'] = item[2]
    return task


if __name__ == '__main__':
    app.run(debug=True)
