from __init__ import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    birthday = db.Column(db.String(100))
    country = db.Column(db.String(100))
    gender = db.Column(db.String(100))
    date_registered = db.Column(db.String(1000))
    courses_id = db.Column(db.String, db.ForeignKey('course.id'))


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    user_id = db.Column(db.String, db.ForeignKey('user.id'))
    provider_id = db.Column(db.String, db.ForeignKey('provider.id'))


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(100))
    provider = db.Column(db.String(100))
    user_hospital_id = db.Column(db.String, db.ForeignKey('provider.id'))


class CourseManager(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rank = db.Column(db.Integer, primary_key=True)
    courses_id = db.Column(db.String, db.ForeignKey('course.id'))
    users_id = db.Column(db.String, db.ForeignKey('user.id'))


class Provider(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    country = db.Column(db.String(100))
    category = db.Column(db.String(100))
    manager_id = db.Column(db.String, db.ForeignKey('user.id'))
