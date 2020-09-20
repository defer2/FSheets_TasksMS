import os.path
from flask import Flask
from database import db
from views import view_blueprint
from flask_cors import CORS


def create_app():
    app_tasks = Flask(__name__)
    app_tasks.config['DEBUG'] = True
    app_tasks.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/tasks.db'
    app_tasks.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    cors = CORS(app_tasks, resources={r"/*": {"origins": "localhost:5015"}})

    db.init_app(app_tasks)
    app_tasks.register_blueprint(view_blueprint, url_prefix='')
    return app_tasks


def setup_database(app_tasks):
    with app_tasks.app_context():
        db.create_all()


if __name__ == '__main__':
    app = create_app()

    if not os.path.isfile('database/tasks.db'):
        setup_database(app)

    app.run(app.run(port=5002))
