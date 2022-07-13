import unittest

from server import create_app
from models import setup_db
import json

class TestPeliculasApi(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = 'proyectotest'
        self.database_path = 'postgresql://{}@{}/{}'.format('postgres:1234', 'localhost:5432', self.database_name)

        setup_db(self.app, self.database_path)

        self.new_sede={
            'nombre':'English-San Borja',
            'distrito':'San Borja',
            'direccion':'Javier Prado',
        }
        self.new_usuario={
            'id' : 10,
            'codigo' : 'Stuart',
            'nombres' : 'Stuart',
            'password' : '1234',
            'rol' : 1
        }
    def test_get_sedes_success(self):
        res = self.client().get('/sedes') 
        data = json.loads(res.data)  
       
        #assert significa validad 
        self.assertEqual(res.status_code, 200) 
        self.assertEqual(data['success'], True) 
        self.assertTrue(data['sedes']) 
        self.assertTrue((data['total_sedes']))#
    def test_get_sedes_sent_requesting_beyond_valid_page_404(self):
        res = self.client().get('/sedes?page=100000000') 
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404) 
        self.assertEqual(data['success'], False) 
        self.assertTrue(data['message'])
    def test_search_sedes_by_nombre(self):
        res = self.client().post('/sedes', json={'search': 'Avengers'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['sedes'])
        self.assertTrue(data['total_sedes']) 

    def test_update_sedes_success(self):
        res0 = self.client().post('/sedes', json=self.new_sede)
        data0 = json.loads(res0.data)
        updated_id = data0['created']

        res = self.client().patch('/sedes/' + str(updated_id), json={'nombre': 'ENGLISH-SJ'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['id'], str(updated_id))

    def test_update_sedes_failed(self):
        res = self.client().patch('/sedes/-100')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_delete_sedes_success(self):
        res0 = self.client().post('/sedes', json=self.new_sede)
        data0 = json.loads(res0.data)
        deleted_id = data0['created']

        res = self.client().delete('/sedes/' + str(deleted_id))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['sedes'])
        self.assertTrue(data['total_sedes'])
        self.assertEqual(data['deleted'], str(deleted_id))

    def test_delete_sedes_failed(self):
        res = self.client().patch('/sedes/-10')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')
    def test_create_sedes_success(self):
        res = self.client().post('/sedes', json=self.new_sede)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(len(data['sedes']))
        self.assertTrue(data['total_sedes'])

    def test_create_sedes_failed(self):
        res = self.client().post('/sedes', json={})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    def test_get_sedes_by_numero_de_sala(self):
        res = self.client().post('/salas', json={'search': 15})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['salas'])
        self.assertTrue(data['total_salas']) 

    def test_get_usuario_success(self):
        res = self.client().get('/usuarios') #cliente con el metoodo y el endopoint respuesta tipo json
        data = json.loads(res.data) # deserealizar  
       
        #assert significa validad 
        self.assertEqual(res.status_code, 200) # el numero  que espero 200 
        self.assertEqual(data['success'], True) #  que el succes sea true
        self.assertTrue(data['usuarios']) # si es mayor que 0 sera true, si es 0 sera falso
        self.assertTrue((data['total_usuarios']))

    def test_get_usuarios_sent_requesting_beyond_valid_page_404(self):
        res = self.client().get('/usuarios?page=10000') # probar error que me muestre la pagina 100 cuando no tengo 100 paginas .
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404) # el codigo deberia ser 404
        self.assertEqual(data['success'], False) # un succes falso ya que es erroneo
        self.assertTrue(data['message'])

    def test_search_usuarios_by_dia(self):
        res = self.client().post('/usuarios', json={'search': 'Stuart'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['usuarios'])
        self.assertTrue(data['total_usuarios'])

    def test_update_usuarios_success(self):
        res0 = self.client().post('/usuarios', json=self.new_usuario)
        data0 = json.loads(res0.data)
        updated_id = data0['created']

        res = self.client().patch('/usuarios/' + str(updated_id), json={'nombre': 'Stuart'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['id'], str(updated_id))

    def test_update_usuarios_failed(self):
        res = self.client().patch('/usuarios/-10', json={'nombre': 'Juan'})
        data = json.loads(res.data) #deserealizar
        #lo que envio en caso sea fallido 
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_delete_usuarios_success(self):
        res0 = self.client().post('/usuarios', json=self.new_usuario)
        data0 = json.loads(res0.data)
        deleted_id = data0['created']

        res = self.client().delete('/usuarios/' + str(deleted_id))
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['usuarios'])
        self.assertTrue(data['total_usuarios'])
        self.assertEqual(data['deleted'], str(deleted_id))

    def test_delete_usuarios_failed(self):
        res = self.client().patch('/usuarios/-10',json=self.new_funcion)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['message'], 'resource not found')
        self.assertEqual(data['success'], False)

    def test_create_usuarios_success(self):
        res = self.client().post('/usuarios', json=self.new_funcion)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(len(data['usuarios']))
        self.assertTrue(data['total_usuarios'])

    def test_create_usuarios_failed(self):
        res = self.client().post('/usuarios', json={})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    