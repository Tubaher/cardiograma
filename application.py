import os
import requests
from models import *

from flask import Flask, session, redirect, render_template, request, flash, jsonify, make_response
from flask_session import Session

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


lista = ['Regular', 'Irregular']

dic_enf_reg = {"Idioventricular rhythms":(30,40),\
    "Sinus bradycardia":(41,59),\
    "Normal sinus rhythm": (60,100),\
    "Sinus tachycardia": (100,109,121,149),\
    "Junctional tachycardia": (11,120),\
    "Atrial tachycardia": (150,179,191,250),\
    "Ventricular tachycardia": (180,190),\
    "Atrial flutter": (250,350),\
    }

dic_enf_irr = {
    "Premature atrial contractions": (85,95),\
    "Premature junctional contraction": (96,119),\
    "Atrial fibrillation": (120,140)
}

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    #Search box
    r = make_response(render_template("index.html"))
    return r


@app.route("/main")
def main():
    r = make_response(render_template("main.html", lista = lista))
    return r

@app.route("/info", methods=['GET'])
def info():
    
    ritmo = request.args.get("ritmo")
    
    if not request.args.get("bpm"):
        return render_template("error.html", message="invalid bpm, please enter a new on in the right range")
    
    try:
        bpm = int(request.args.get("bpm"))
    except:
        return render_template("error.html", message="invalid bpm, please enter a new on in the right range")

    
    if ritmo == "Regular":
        Patologias = Patologia.query.filter_by(ritmo=ritmo).all()
        enfermedad = None

        for patologia in Patologias:
            if (bpm >= patologia.r1 and bpm <= patologia.r2):
                    enfermedad = patologia
                    break
                    
            elif patologia.r3 != 0:
                if (bpm >= patologia.r3 and bpm <= patologia.r4):
                    enfermedad = patologia
                    break
        if enfermedad == None:
            return render_template("error.html", message="invalid bpm, please enter a new on in the right range")
    else:
        Patologias = Patologia.query.filter_by(ritmo=ritmo).all()
        enfermedad = None
        for patologia in Patologias:
            if (bpm >= patologia.r1 and bpm <= patologia.r2):
                    enfermedad = patologia
        if enfermedad == None:
            return render_template("error.html", message="invalid bpm, please enter a new on in the right range")
    r = make_response(render_template("info.html", enfermedad = enfermedad, bpm=bpm))
    return r
