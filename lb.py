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
    
    def __repr__(self):
        return f'codigo={self.codigo}, name={self.name}'
    

db.create_all()

@lb.route('/')      
def index():    
     return render_template('inicio_0.html')

@lb.route('/usuario/create', methods=['POST','GET'])
def create_prueba_post():
   error = False
   response = {}
   name = request.form.get('name','')
   contraseña = request.form.get('contraseña','')
   if(contraseña==''):
        return render_template('inicio_0.html')
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
        
     return render_template('datos_registrar.html',  da=Menu.query.all())


#Segundo modelo
class registro(db.Model):
     __tablename__ = 'registros'
     id_r = db.Column(db.Integer, primary_key=True)
     nombre = db.Column(db.String(), nullable=False)
     apellido = db.Column(db.String(), nullable=False)
     edad = db.Column(db.Integer, nullable=False)
     colegio=db.Column(db.String(),nullable=False)
     numero=db.Column(db.Integer, nullable=False)
     #id_curso=db.Column(db.Integer,db.ForeignKey('Menu.codigo'),nullable=False)
     def __repr__(self):
        return "Incripcion realizada"

db.create_all()


@lb.route('/registros/create', methods=['POST','GET'])
def create_registro_post():

   error = False
   response = {}
   nombre= request.form.get('nombre','')
   apellido= request.form.get('apellido','')
   edad=request.form.get('edad','')
   colegio=request.form.get('colegio','')
   numero=request.form.get('numero','')
   try:
          edad=request.form.get('edad','')
          colegio=request.form.get('colegio','')
          nombre= request.form.get('nombre','')
          apellido= request.form.get('apellido','')
          numero=request.form.get('numero','')
        
          pasar = registro(nombre=nombre,apellido=apellido,edad=edad,colegio=colegio,numero=numero)
        
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
        
     return render_template('tipoElegir.html',  da=[nombre,apellido])



#Segundo modelo
class Tipo(db.Model):
     __tablename__ = 'dificultad'
     id = db.Column(db.Integer, primary_key=True)
     dificultad= db.Column(db.String(), nullable=False)
    
     #id_curso=db.Column(db.Integer,db.ForeignKey('Menu.codigo'),nullable=False)
     def __repr__(self):
        return "Incripcion realizada"

db.create_all()


@lb.route('/dificultad/create', methods=['POST','GET'])
def create_dificultad_post():

   error = False
   response = {}
   dificultad= request.form.get('dificultad','')

   try:
          dificultad= request.form.get('dificultad','')

        
          pasar = Tipo(dificultad=dificultad)
        
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
        
     return render_template('intermedio.html')


  




if __name__ == '__main__':
    lb.run(debug=True, port= 5000)