#!/usr/bin/python3.7

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_placeholder'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db.init_app(app)

from models import User, Patient, Course, CourseManager, Provider

from form import form as form_blueprint
app.register_blueprint(form_blueprint)

def create_app():
    return app