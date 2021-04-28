#!/usr/bin/env python3
#-*- coding: utf8 -*-
"""Sample app"""

from flask import Flask,request, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URL"] = "sqlite:///mydb.db"
db = SQLAlchemy(app)

from app.database import *

