from token import LBRACE
from unicodedata import name
from flask import Flask, redirect, url_for
from flask import render_template,request,abort,jsonify 
from flask_sqlalchemy import SQLAlchemy 
import sys

lb = Flask(__name__)
lb.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://postgres:1234@localhost:5432/dbp20'
lb.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(lb) 

#primer modelo
class Registro(db.Model):
    __tablename__='registros'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80),nullable = False)
    apellido = db.Column(db.String(80),nullable = False)
    #age = db.Column(db.Integer, nullable =False) 
    #telefono = db.Column(db.Integer, nullable =False) 

    def __init__(self,name,apellido) -> None:
        self.name = name
        self.apellido=apellido

    def __repr__(self):
        return f'Registro: name={self,name}'
    

db.create_all()

@lb.route('/')      
def index():    
    return render_template('index.html', data=Registro.query.all())

@lb.route('/registrar', methods=['POST'])
def create_prueba_post():
    error = None
    name = request.get_json()['name']
    apellido = request.get_json()['apellido']
    registro = Registro(name, apellido)
    if not name:
        error= 'Se necesita nombre'
    elif not apellido:
        error= 'Se necesita apellido'
    
    return render_template('index.html')




if __name__ == '__main__':
    lb.run(debug=True, port= 5001)