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
    app_tasks.config['CORS_HEADERS'] = 'Content-Type'

    db.init_app(app_tasks)
    app_tasks.register_blueprint(view_blueprint, url_prefix='')
    return app_tasks


def setup_database(app_tasks):
    with app_tasks.app_context():
        db.create_all()


app = create_app()
cors = CORS(app)

if __name__ == '__main__':
    if not os.path.isfile('database/tasks.db'):
        setup_database(app)

    app.run(host='0.0.0.0', port=5011)

