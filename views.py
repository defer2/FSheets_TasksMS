from flask import Blueprint, jsonify, request
from flask_cors import cross_origin, CORS
import requests
import controllers

view_blueprint = Blueprint('view_blueprint', __name__)
CORS(view_blueprint, resources={r'/*': {"origins": "localhost:5015"}})


@view_blueprint.route('/', methods=['GET'])
def hello_world():
    return controllers.hello_world()


@view_blueprint.route('/create', methods=['POST'])
def create_task():
    task_name = request.args.get("name")
    return jsonify(controllers.create_task(task_name))


@view_blueprint.route('/view', methods=['GET'])
def get_tasks():
    return jsonify(controllers.get_tasks())


@view_blueprint.route('/view/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = controllers.get_task(task_id)
    projectResponse = requests.get('http://localhost:5010/view/' + str(task[0]['project_id']))
    project = projectResponse.json()
    task[0]['project'] = project[0]
    return jsonify(task)


@view_blueprint.route('/view/project/<int:task_id>', methods=['GET'])
def get_task_project(task_id):
    task = controllers.get_task(task_id)
    projectResponse = requests.get('http://localhost:5010/view/' + str(task[0]['project_id']))
    project = projectResponse.json()

    return jsonify(project[0])


@view_blueprint.route('/view/<string:task_name>', methods=['GET'])
def get_task_by_name(task_name):
    return jsonify(controllers.get_task_by_name(task_name))


@view_blueprint.route('/delete/<int:task_id>', methods=['DELETE'])
def delete_task_by_id(task_id):
    return jsonify(controllers.delete_task_by_id(task_id))


@cross_origin()
@view_blueprint.route('/update/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task_name = request.args.get("name")
    task_status = request.args.get("status")
    task_description = request.args.get("description")
    task_project_id = request.args.get("project_id")
    return jsonify(controllers.update_task(task_id, task_name, task_status, task_description, task_project_id))
