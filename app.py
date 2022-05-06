#imports
from flask import (
    Flask,
    jsonify, 
    redirect, 
    render_template, 
    request, 
    url_for,
    abort
)
import random
from flask_sqlalchemy import SQLAlchemy
import sys
from flask_migrate import Migrate
from sqlalchemy import FLOAT, Column, Integer, false








#configuration
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:1234@localhost:5432/home'



app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False



db = SQLAlchemy(app)
migrate = Migrate(app, db)



class Menu(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(), nullable=False)

    contraseña=db.Column(db.String(), primary_key=False)


    def __repr__(self):
        return f'Todo: id={self.id}, name={self.name}'


db.create_all()

#controller  para pasar lista al html



@app.route('/')
def index():
    return render_template('inicio_0.html', data=Menu.query.all())

 
@app.route('/usuario/create', methods=['POST'])
def create_usuario_post():
    error = False
    response = {}



   
    try:
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
        return render_template('entro.html', da=[name])
    


#run
if __name__ == '__main__':
    app.run(debug=True, port=5002)





     
