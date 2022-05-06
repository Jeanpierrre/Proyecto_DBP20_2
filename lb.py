from token import LBRACE
from unicodedata import name
from flask import Flask, redirect, url_for
from flask import render_template,request,abort,jsonify 
from flask_sqlalchemy import SQLAlchemy 
import sys
from flask_migrate import Migrate
lb = Flask(__name__)
lb.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://postgres:1234@localhost:5432/proyecto'
lb.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(lb) 
migrate = Migrate(lb, db)
#primer modelo
class Menu(db.Model):
    __tablename__ = 'usuario'
    codigo = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(), nullable=False)

    contraseña=db.Column(db.String(), primary_key=False)
    
    #age = db.Column(db.Integer, nullable =False) 
    #telefono = db.Column(db.Integer, nullable =False) 

    #def __init__(self,name,contraseña) -> None:
        #self.name = name
        #self.contraseña=contraseña

    def __repr__(self):
        return f'Registro: name={self,name}'
    

db.create_all()

@lb.route('/')      
def index():    

 return render_template('inicio_0.html', data=Menu.query.all())

@lb.route('/usuario/create', methods=['POST'])
def create_prueba_post():
   error = False
   response = {}

   try:
        id= request.form.get('id','')
        name = request.form.get('name','')

        
        contraseña = request.form.get('contraseña','')

        pasar = Menu(name=name,contraseña=contraseña)
        
        db.session.add(pasar)
        db.session.commit()
   except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
   finally:
        db.session.close()
   if error:
        abort(500)

   else:
     return render_template('entro.html',  da=Menu.query.filter_by(name=name).all())




if __name__ == '__main__':
    lb.run(debug=True, port= 5000)