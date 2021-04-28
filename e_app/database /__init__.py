#!/usr/bin/env python3
#-*- coding: utf8 -*-
"""Database models"""

from app import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=True)
    description = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    quantity = db.Column(db.Integer, nullable=True)
    unique_tag = db.Column(db.String, nullable=False)
    active = db.Column(db.String, nullable=False)

    def __repr__(self):
        return "<Product %r>" % self.full_name