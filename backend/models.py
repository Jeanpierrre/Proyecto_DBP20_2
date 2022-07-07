from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

database_name = 'apiproyecto'
database_path = 'postgresql://{}@{}/{}'.format('postgres:dev123', 'localhost:5432', database_name)
#'postgresql://postgres:1234@localhost:5432/todoapp10'
db = SQLAlchemy()
#Models

def setup_db(app, database_path = database_path):
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app=app
    db.init_app(app)
    db.create_all()

class Usuario(UserMixin,db.Model):
    _tablename_ = 'usarios'
    id = db.Column(db.Integer, primary_key = True,autoincrement=True)
    codigo = db.Column(db.String(200), unique=True)
    password= db.Column(db.String(200), nullable = False)
    rol = db.Column(db.Integer,nullable = False, default = 0)
    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except:
            db.session.rollback()
        finally:
            db.session.close()

    def update(self):
        try:
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()

    def format(self):
        return {
            'id': self.id,
            'codigo': self.codigo,
            'password':self.password,
            'rol': self.rol,
        }
class datos_usuario(db.Model):
    _tablename_ = 'datos_usuarios'
    id = db.Column(db.Integer , primary_key = True)
    nombres = db.Column(db.String(200), nullable = False)
    apellidos = db.Column(db.String(200), nullable = False)
    telefono = db.Column(db.String(200), nullable = False)
    edad = db.Column(db.Integer, nullable = False)
    colegio = db.Column(db.String(200), nullable = False)
    dificultad = db.Column(db.String(200), nullable = False)
    nombre_sede = db.Column(db.String(200),db.ForeignKey('sede.nombre'), nullable = False)

    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except:
            db.session.rollback()
        finally:
            db.session.close()

    def update(self):
        try:
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()

    def format(self):
        return {
            'id': self.id,
            'nombres': self.nombres,
            'apellidos': self.apellidos,
            'telefono': self.telefono,
            'edad': self.edad,
            'colegio': self.colegio,
            'dificultad': self.dificultad,
            'sede' : self.nombre_sede
        }


class sede(db.Model):
    _tablename_ = 'sedes'
    nombre = db.Column(db.String(200) , primary_key = True)
    distrito = db.Column(db.String(200), nullable = False)
    direccion = db.Column(db.String(200), nullable = False)
    datos = db.relationship('datos_usuario', backref='datos', lazy=True)
    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except:
            db.session.rollback()
        finally:
            db.session.close()

    def update(self):
        try:
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()

    def format(self):
        return {
            'nombre_sede': self.nombre,
            'distrito': self.distrito,
            'direccion': self.direccion,
        }

