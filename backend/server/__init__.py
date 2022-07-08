from flask import(
    Flask,
    abort,
    jsonify,
    request
)

from flask_cors import CORS
from flask_sqlalchemy import Pagination

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, logout_user, login_required,current_user

from models import setup_db, Usuario,datos_usuario,sede

usuarios_PER_PAGE=5
def paginate(request, selection, isDescendent):
    if isDescendent:
        start = len(selection) - usuarios_PER_PAGE
        end = len(selection)
    else:
        page = request.args.get('page', 1, type=int)
        start = (page - 1)*usuarios_PER_PAGE
        end = start + usuarios_PER_PAGE
    travels = [travel.format() for travel in selection]
    current_travels = travels[start:end]
    return current_travels

def create_app(test_config=None):
    app = Flask(__name__)

    login_manager = LoginManager()
    login_manager.init_app(app)

    setup_db(app)
    CORS(app,origins=['*'],max_age=10)
    app.secret_key = "123"
    @login_manager.user_loader
    def load_user(id):
        return Usuario.query.get(int(id))
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers','Content-Type, Authorizations, true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
        return response
    
    @app.route('/usuarios/<int:rol>', methods=['GET'])
    
    def get_usuarios(rol):
        print("aqui")
        try:
            print("aqui 2")
            if rol == 1:
                selection = datos_usuario.query.order_by('id').all() 
                usuarios = paginate(request, selection, False) #paginamos en formato json
                print("aqui 3")
                if len(usuarios) == 0:
                    abort(404) # 404 not found

                return jsonify({
                    'success': True, #exitosamente
                    'Usuarios': usuarios, #todos los elementos de todos
                    'total_usuarios': len(selection) #cantidad de elementos todos
                })
            else:
                usuario = datos_usuario.query.filter(datos_usuario.id == current_user.id).one_or_none()
                
                usuario_info = usuario.format()
                return jsonify({
                'success': True,
                'info_usuario': usuario_info
                })
        except Exception as e:
        
            print(e)
    
    
    @app.route('/registros', methods=['POST'])
    def create_usuarios():
        body = request.get_json()
        codigo = body.get('codigo',None)
        password = body.get('password',None)
        nombres = body.get('nombres',None)
        apellidos = body.get('apellidos',None)
        telefono = body.get('telefono',None)
        edad = body.get('edad',None)
        colegio = body.get('colegio',None)
        dificultad = body.get('dificultad',None)
        nombre_sede = body.get('sede',None)

        try:
            usuario = Usuario(codigo = codigo,nombres=nombres,password = generate_password_hash(password, method='sha256'))
            datos_usuarios = datos_usuario(nombres=nombres,apellidos=apellidos,telefono=telefono,edad=edad,colegio=colegio,dificultad=dificultad,nombre_sede=nombre_sede)
            new_usuario_id = usuario.insert()
            new_datos_usuario_id = datos_usuarios.insert()


            selection = Usuario.query.order_by('id').all()
            todos = paginate(request, selection, True)

            return jsonify({
                'success': True,
                'created': new_datos_usuario_id,
                'usuarios': todos,
                'total_usuarios': len(selection)
            })
        except Exception as e:
            print(e)
            abort(500)    


    
    @app.route('/usuarios/<usuarios_id>', methods=['PATCH'])
    def update_todo(usuario_id):
        error_404 = False
        try:
            usuario = Usuario.query.filter(Usuario.id == usuario_id).one_or_none()
            if usuario is None:
                error_404 = True
                abort(404)


            body = request.get_json()
            if 'description' in body:
                usuario.description = body.get('description')

            usuario.update()
            
            return jsonify({
                'success': True,
                'id': usuario_id
            })
        except:
            if error_404:
                abort(404)
            else:
                abort(500)
    @app.route('/usuarios/<usuario_id>', methods=['DELETE'])
    @login_required
    def delete_todo2(usuario_id):
        error_404 = False
        error_403 = False
        try:
            
            if int(current_user.rol) != 1:
                error_403 = True
                abort(403)
            todo = Usuario.query.filter(Usuario.id == usuario_id).one_or_none()
            if todo is None:
                error_404 = True
                abort(404)

            todo.delete()

            selection = Usuario.query.order_by('id').all()
            todos = paginate(request, selection, True)
            print('xd')
            return jsonify({
                'success': True,
                'deleted': usuario_id,
                'Usuario': todos,
                'total_usuarios': len(selection)
            })

        except Exception as e:
            print(e)
            if error_403:
                abort(403)
            elif error_404:
                abort(404)
            else:
                abort(500)
    @app.route('/sedes', methods=['GET'])
    @login_required
    def get_todos():
        selection = sede.query.all() 
        todos = paginate(request, selection, False) #paginamos en formato json

        if len(todos) == 0:
            abort(404) # 404 not found

        return jsonify({
            'success': True, #exitosamente
            'sedes': todos, #todos los elementos de todos
            'total_sedes': len(selection) #cantidad de elementos todos
        })
    
    @app.route('/sedes', methods=['POST'])
    def create_sedes():
        body = request.get_json()
        distrito = body.get('distrito',None)
        direccion = body.get('direccion',None)
        try:
            usuario = sede(distrito = distrito, direccion=direccion)
            new_todo_id = usuario.insert()

            selection = sede.query.order_by('id').all()
            todos = paginate(request, selection, True)

            return jsonify({
                'success': True,
                'created': new_todo_id,
                'sedes': todos,
                'total_sedes': len(selection)
            })
        except Exception as e:
            print(e)
            abort(500)    
    @app.route('/sedes/<sede_nombre>', methods=['PATCH'])
    def update_todo2(sede_id):
        error_404 = False
        try:
            todo = sede.query.filter(sede.nombre == sede_id).one_or_none()
            if todo is None:
                error_404 = True
                abort(404)


            body = request.get_json()
            if 'description' in body:
                todo.description = body.get('description')

            todo.update()
            
            return jsonify({
                'success': True,
                'id': sede_id
            })
        except:
            if error_404:
                abort(404)
            else:
                abort(500)


    @app.route('/sedes/<sedes_nombre>', methods=['DELETE'])
    @login_required
    def delete_todo(sede_id):
        error_404 = False
        error_403 = False
        try:
            if current_user.rol == 1:
                error_403 = True
                abort(403)
            todo = sede.query.filter(sede.nombre == sede_id).one_or_none()
            if todo is None:
                error_404 = True
                abort(404)

            todo.delete()

            selection = sede.query.order_by('id').all()
            todos = Pagination(request, selection, True)

            return jsonify({
                'success': True,
                'deleted': sede_id,
                'Sedes': todos,
                'total_sedes': len(selection)
            })

        except Exception as e:
            print(e)
            if error_403:
                abort(403)
            elif error_404:
                abort(404)
            else:
                abort(500)
    @app.route('/login', methods=['GET'])
    def login():
        error_403 = False
        error_404 = False
        try:
            body = request.get_json()
            codigo = body.get('codigo',None)
            verificacion = Usuario.query.filter(Usuario.codigo == codigo).one_or_none()
            if verificacion is None:
                error_404 = True
                abort(404)
            password = body.get('password',None)
            if not check_password_hash(verificacion.password,password):
                error_403 = True
                abort(403)
            login_user(verificacion)
            return jsonify({
                'success': True,
                "message" : 'Acceso concedido'
            })
        except Exception as e:
            print(e)
            if error_404:
                abort(404)
            elif error_403:
                abort(403)
            else:
                abort(500)

    @app.route('/logout', methods=['GET'])
    @login_required
    def logout():
        logout_user()
        return jsonify({
            'success': True,
            'message': "Closed session"
        })

    @app.route('/login', methods=['POST'])
    def login2():
        error404=False
        try:
            body = request.get_json()
            codigo = body.get('codigo',None)
            password = body.get('password',None)
            usuario=Usuario.query.filter(codigo==codigo).one_or_none()
            if(usuario is None):
                error404=True
                abort(404)
            if usuario:
                if check_password_hash(usuario.password,password):
                    return jsonify({
                    'success': True,
                    'usuarios': usuario.format(),
                    })
                else:
                    return jsonify({
                        'success':False,
                        'message':'contraseña errónea'
                    })
        except Exception as e:
            if error404==True:
                abort(404)
            else:
                print(e)
                abort(500)


    @app.errorhandler(403) #manejamos el error 404 , se debe mandar algo al cliente 
    def not_found(error):
        return jsonify({
            'success': False,
            'code': 403,
            'message': 'Acceso denegado'
        }), 403
     #manejo de errores
    @app.errorhandler(404) #manejamos el error 404 , se debe mandar algo al cliente 
    def not_found(error):
        return jsonify({
            'success': False,
            'code': 404,
            'message': 'resource not found'
        }), 404

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            'success': False,
            'code': 500,
            'message': 'internal server error'
        }), 500


    @app.errorhandler(405)
    def server_error(error):
        return jsonify({
            'success': False,
            'code': 405,
            'message': 'method not allowed'
        }), 405
   
    @app.errorhandler(422)
    def server_error(error):
        return jsonify({
            'success': False,
            'code': 422,
            'message': 'unprocessable'
        }), 422
    @app.errorhandler(413)
    def server_error(error):
        return jsonify({
            'success': False,
            'code': 413,
            'message': 'Request Entity too Large'
        }), 413
    @app.errorhandler(401)
    def server_error(error):
        return jsonify({
            'success': False,
            'code': 401,
            'message': 'Autenticacion requerida'
        }), 401  
        







    return app