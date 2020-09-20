from database import db
from models import Tasks, TasksSchema


def hello_world():
    return 'Hello World!'


def create_task(task_name):
    db.session.add(Tasks(name=task_name))
    db.session.commit()
    return TasksSchema(many=True).dump(Tasks.query.all())


def get_tasks():
    return TasksSchema(many=True).dump(Tasks.query.all())


def get_task(task_id):
    task = db.session.query(Tasks).filter(Tasks.id == task_id)
    return TasksSchema(many=True).dump(task)


def get_task_by_name(task_name):
    return TasksSchema(many=True).dump(db.session.query(Tasks).filter(Tasks.name == task_name))


def delete_task_by_id(task_id):
    one_task = db.session.query(Tasks).filter_by(id=task_id).one()
    db.session.delete(one_task)
    db.session.commit()
    return TasksSchema(many=True).dump(Tasks.query.all())


def update_task(task_id, task_name, task_status, task_description, project_id):
    one_task = db.session.query(Tasks).filter_by(id=task_id).one()
    one_task.name = task_name
    one_task.status = task_status or one_task.status
    one_task.description = task_description or one_task.description
    one_task.project_id = project_id or one_task.project_id
    db.session.add(one_task)
    db.session.commit()
    return TasksSchema(many=True).dump(Tasks.query.all())
