import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Patologia(db.Model):
    __tablename__ = "patologias"
    id = db.Column(db.String, primary_key=True)
    ritmo = db.Column(db.String, nullable=False)
    pato_nombre = db.Column(db.String, nullable=False)
    r1 = db.Column(db.Integer, nullable=False)
    r2 = db.Column(db.Integer, nullable=False)
    r3 = db.Column(db.Integer, nullable=False)
    r4 = db.Column(db.Integer, nullable=False)
    rate = db.Column(db.String, nullable=False)
    p_wave = db.Column(db.String, nullable=False)
    pr_interval = db.Column(db.String, nullable=False)
    qrs_complex = db.Column(db.String, nullable=False)
    t_wave = db.Column(db.String, nullable=False)
    qt_interval = db.Column(db.String, nullable=False)
    other = db.Column(db.String, nullable=False)
    descripcion = db.Column(db.String, nullable=False)
    recomendaciones = db.Column(db.String, nullable=False)
    



