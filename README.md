# ENGLISH EXPRESS
* Nombre del grupo : 404-Error
* Integrantes: 
  + Jean Pierre Sotomayor - 202110660  (100%)
  + Diego Rivadeneyra -                    (100%)
  + Stuart Diego Arteaga Montes - 202110502 (100%)
* Descripcion : Desarrollamos una web de un curso de ingles que nos permite crear un usuario, seguidamente poner nuestros datos
  poder elegir el nivel de ingles que deseamos aprender y registrarlo exitosamente.
* Misión : Nuestra misión es brindar una buena pagina web que pueda registrar exitosamente a los usuarios que deseen aprender ingles.
* Visión : Queremos ser una  pagina web de lo que es enseñaza virtual del idioma inglés
* Objetivo : Nuestro principal objetivo es que nuestra pagina sea amigable para los usuarios y no tenga muchos errores.
* Informacion de librerias:
  + FLASK : Es micro Framework  que nos ayudo para simplificar la creacion de la pagima web 
  + SQLalchemy : Es un ORM que usamos para la creacion de la base de datos y manipularlo si usar lenguaje SQL 
  + Migrate : Ya que al momento de crear al aplicacion web siempre se aumentaban modelos por ende usamos el migrate para poder crearlas.
* Endpoints:
  + '/' : Nos redirecciona al incio del aplicacion .
  + '/registros/create' : Redirecciona los datos ingresado en el html hacia la base de datos y los guarda.
  + '/dificultad/create' : Redirecciona los datos de dificultad ingresada en el html hacia la base de datos y los guarda.
  + "/lists/1" : Extrae de la base de datos los datos de las sedes
  + "/lists/2" : Extrae de la base de datos los datos de los profesores
* Host : http://127.0.0.1:5000 
* Manejo de errores : Los errores que manejamos en los html fueron tratados con condicionales if como en el numero que tenga solo 9 digitos,
  que la edad no sea negativa y que no se deje ningun espacio en blanco, entre otros.En el caso del lb.py colocamos las condiciones de que si sucede un error entonces hace un rollback y muestra un error 500.