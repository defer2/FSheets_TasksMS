from flask_marshmallow.sqla import SQLAlchemyAutoSchema
from database import db


class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    status = db.Column(db.Integer, nullable=False, default=1)
    description = db.Column(db.String(2000))
    project_id = db.Column(db.Integer)


class TasksSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Tasks
        include_relationships = True
        load_instance = True
