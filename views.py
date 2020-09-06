from flask import Blueprint, jsonify, request
import controllers
view_blueprint = Blueprint('view_blueprint', __name__)


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
    return jsonify(controllers.get_task(task_id))


@view_blueprint.route('/view/<string:task_name>', methods=['GET'])
def get_task_by_name(task_name):
    return jsonify(controllers.get_task_by_name(task_name))


@view_blueprint.route('/delete/<int:task_id>', methods=['DELETE'])
def delete_task_by_id(task_id):
    return jsonify(controllers.delete_task_by_id(task_id))


@view_blueprint.route('/update/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task_name = request.args.get("name")
    task_status = request.args.get("status")
    task_description = request.args.get("description")
    task_project_id = request.args.get("project_id")
    return jsonify(controllers.update_task(task_id, task_name, task_status, task_description, task_project_id))
