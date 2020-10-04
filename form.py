#!/usr/bin/python3.7
from flask import Blueprint, render_template, request, flash, redirect, url_for

from datetime import datetime, date

from models import User, Patient, Course, CourseManager, Provider

from __init__ import db

form = Blueprint('form', __name__)


@form.route('/')
@form.route('/home')
def home():
    return render_template('home.html')


@form.route('/warning')
def warning():
    return render_template('warning.html')


@form.route('/request-doctor')
def request_doctor():
    return render_template('request_doctor.html')


@form.route('/request-waiting')
def request_waiting():
    return render_template('request_waiting.html')


@form.route('/take-course')
def take_course():
    return render_template('take_course.html')


@form.route('/social-club-home')
def social_club_home():
    return render_template('social_club_home.html')


@form.route('/social-club-join-activity')
def social_club_join_activity():
    return render_template('social_club_join_activity.html')

