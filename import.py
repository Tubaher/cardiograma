import csv
import os

from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    f = open("Patologias.csv")
    reader = csv.reader(f, delimiter = ';')
    for id, ritmo, pato_nombre, r1, r2, r3, r4,\
        rate, p_wave, pr_interval, qrs_complex, t_wave,\
        qt_interval, other, descripcion, recomendaciones in reader:
        patologia = Patologia(id=id, ritmo=ritmo, pato_nombre=pato_nombre, r1=r1, r2=r2, r3=r3, r4=r4, rate=rate, p_wave=p_wave,\
            pr_interval=pr_interval, qrs_complex=qrs_complex, t_wave=t_wave,\
            qt_interval= qt_interval, other = other, descripcion= descripcion,\
            recomendaciones= recomendaciones )
        db.session.add(patologia)
        #print(f"Added flight from {origin} to {destination} lasting {duration} minutes.")
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        main()