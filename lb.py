from flask import Flask, redirect, url_for
from flask import render_template,request,abort,jsonify 
from flask_sqlalchemy import SQLAlchemy 
import sys
from flask_migrate import Migrate
guardar=[]
mensaje=[]
#escribir
          
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
    

#db.create_all()
@lb.route('/')      
def index():    

     return render_template('inicio_0.html',mensaje=[''])

#direccion para contactos y nosotros
@lb.route('/contactos/',methods=['GET'])
def contactos():
     return render_template('contactos.html')  
     

@lb.route('/nosotros/',methods=['GET'])
def nosotros():
     return render_template('nosotros.html')   


@lb.route('/usuario/create', methods=['POST','GET'])
def create_prueba_post():
   error = False
   response = {}

   try:
        id= request.form.get('id','')
        name = request.form.get('name','')
        contraseña = request.form.get('contraseña','')
        if(name=='' or contraseña==''):
             return render_template('inicio_0.html',mensaje=['No dejes ningun espacio en blanco'])
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
     codigo=list(Menu.query.all())
     pasar_codigo=str(codigo[-1].codigo)
     guardar.append(pasar_codigo) 
     return render_template('datos_registrar.html',  da=Menu.query.all(),mensaje=[''])


#Segundo modelo
class registro(db.Model):
     __tablename__ = 'registros'
     id_r = db.Column(db.Integer, primary_key=True)
     nombre = db.Column(db.String(), nullable=False)
     apellido = db.Column(db.String(), nullable=False)
     edad = db.Column(db.Integer, nullable=False)
     colegio=db.Column(db.String(),nullable=False)
     numero=db.Column(db.Integer, nullable=False)

     def __repr__(self):
          return f'nombre={self.nombre}, apellido={self.apellido}, edad={self.edad}, colegio={self.colegio}, numero={self.numero}'
#db.create_all()
@lb.route('/registros/create', methods=['POST','GET'])
def create_registro_post():

   error = False
   response = {}
   try:
          edad=request.form.get('edad','')
          colegio=request.form.get('colegio','')
          nombre= request.form.get('nombre','')
          apellido= request.form.get('apellido','')
          numero=request.form.get('numero','')

          if(nombre=='' or colegio=='' or apellido=='' ):
               return render_template('datos_registrar.html',mensaje=['No dejes ningun espacio en blanco'])

          for a in str(edad):
               if(a=='-'):
                    return render_template('datos_registrar.html',mensaje=['No ingreses valores negativos'])
 
          if(len(str(numero))!= 9 ):
                return render_template('datos_registrar.html',mensaje=['El numero debe tener 9 dijitos'])
          if (len(str(edad)) !=  2):
               return render_template('datos_registrar.html',mensaje=['La edad debe tener 2 digitos'])
    
          for a in str(numero):
               if(a=='-'):
                    return render_template('datos_registrar.html',mensaje=['No ingreses valores negativos'])
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
        
     return render_template('tipoElegir.html')



#Tercer modelo
class Tipo(db.Model):
     __tablename__ = 'dificultad'
     id = db.Column(db.Integer, primary_key=True)
     dificultad= db.Column(db.String(), nullable=False)
     id_usuario=db.Column(db.String(), nullable=False)

     def __repr__(self):
          return f'dificultad={self.dificultad}'
#db.create_all()

@lb.route('/dificultad/create', methods=['POST','GET'])
def create_dificultad_post():

   error = False
   response = {}
   dificultad= request.form.get('dificultad','')

   id_usuario=guardar[-1]
   try:
          dificultad= request.form.get('dificultad','')
          pasar = Tipo(dificultad=dificultad,id_usuario=id_usuario)
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
        
     return render_template('final.html',registro=registro.query.all(),
     dificultad=Tipo.query.all() )


class Sede(db.Model):
     __tablename__ = 'sedes'
     id = db.Column(db.Integer, primary_key=True)
     Distrito= db.Column(db.String(), nullable=False)
     Direccion= db.Column(db.String(), nullable=False)
     list_id=db.Column(db.Integer,db.ForeignKey('listas.id'), nullable=False)
     
     def __repr__(self):
        return f'Lista: id={self.id}, name={self.Direccion}'

#db.create_all()


class Lista(db.Model):
     __tablename__ = 'listas'
     id = db.Column(db.Integer, primary_key=True)
     name= db.Column(db.String(), nullable=False)
     sedes=db.relationship('Sede', backref='list', lazy= True)
     profesores = db.relationship('Profesor', backref = 'list',lazy =True)
     def __repr__(self):
        return f'Lista: id={self.id}, name={self.name}'

#db.create_all()

#4to modelo

class Profesor(db.Model):
     __tablename__ = 'profesores'
     id = db.Column(db.Integer, primary_key=True)
     nombre = db.Column(db.String(), nullable=False)
     apellido = db.Column(db.String(), nullable=False)
     dificultad = db.Column(db.String(), nullable=False)
     list_id=db.Column(db.Integer,db.ForeignKey('listas.id'), nullable=False)
     def __repr__(self):
        return f'Lista: id={self.id}, nombre={self.nombre},apellido={self.apellido},dificultad={self.dificultad}'

@lb.route("/lists/2")
def mostrar():
     return render_template('tipoElegir.html',data=Profesor.query.all()) # obtenemos todos los objetos de todo
@lb.route("/lists/1")
def mostrar2():
     return render_template('tipoElegir.html',data2=Sede.query.all()) # obtenemos todos los objetos de todo
#db.create_all()

 
if __name__ == '__main__':
    lb.run(debug=True, port= 5000)