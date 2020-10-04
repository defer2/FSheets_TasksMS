import os
from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
import requests
import controllers
import configparser
view_blueprint = Blueprint('view_blueprint', __name__)


config = configparser.ConfigParser()
config_path = os.path.join('conf', 'config.ini')
config.read(config_path)
api_projects_url = config.get('FTIMESHEETS', 'API_PROJECTS_URL')



@view_blueprint.route('/', methods=['GET'])
@cross_origin()
def hello_world():
    return controllers.hello_world()


@view_blueprint.route('/create', methods=['POST'])
@cross_origin()
def create_task():
    task_name = request.args.get("name")
    return jsonify(controllers.create_task(task_name))


@view_blueprint.route('/view', methods=['GET'])
@cross_origin()
def get_tasks():
    return jsonify(controllers.get_tasks())


@view_blueprint.route('/view/<int:task_id>', methods=['GET'])
@cross_origin()
def get_task(task_id):
    task = controllers.get_task(task_id)
    try:
        projectResponse = requests.get(api_projects_url+'/view/' + str(task[0]['project_id']))
        project = projectResponse.json()
        task[0]['project'] = project[0]
    except:
        task[0]['project'] = '{}'

    return jsonify(task)


@view_blueprint.route('/view/project/<int:task_id>', methods=['GET'])
@cross_origin()
def get_task_project(task_id):
    task = controllers.get_task(task_id)
    try:
        projectResponse = requests.get(api_projects_url+'/view/' + str(task[0]['project_id']))
        project = projectResponse.json()
        return jsonify(project[0])
    except:
        return jsonify('{}')


@view_blueprint.route('/view/<string:task_name>', methods=['GET'])
@cross_origin()
def get_task_by_name(task_name):
    return jsonify(controllers.get_task_by_name(task_name))


@view_blueprint.route('/delete/<int:task_id>', methods=['DELETE'])
@cross_origin()
def delete_task_by_id(task_id):
    return jsonify(controllers.delete_task_by_id(task_id))


@view_blueprint.route('/update/<int:task_id>', methods=['PUT'])
@cross_origin()
def update_task(task_id):
    task_name = request.args.get("name")
    task_status = request.args.get("status")
    task_description = request.args.get("description")
    task_project_id = request.args.get("project_id")
    return jsonify(controllers.update_task(task_id, task_name, task_status, task_description, task_project_id))
