Tercera Pre-Entrega Daniel Diaz - CoderHose Proyect Django


Simularemos un sistema simple de gestion de biblioteca

Las funcionalidades de la página y la forma de actuar es la siguiente:

1. Clonar repo en tu máquina local.

2. Ejecutar terminal en la raiz del proyecto

3. Crear y activar el entorno virtual:	python -m venv nombre_del_entorno
										
										En Windows: .\nombre_del_entorno\Scripts\activate.
										En Linux/Mac: source ./nombre_del_entorno/bin/activate.

    
4. Instala las dependencias del proyecto: pip install -r requirements.txt.

5. En la terminal, navega hasta la carpeta del proyecto con cd djangoLibrary

6. Ejecuta las migraciones de Django con el comando: python manage.py migrate

7. Ejecuta las migraciones de Django con el comando: python manage.py makemigrations

8. Ejecuta el servidor con el comando: python manage.py runserver.

9. Abre un navegador y navega hasta http://127.0.0.1:8000/AppLibrary/ para ver la página principal.

10. En el NavBar -> Opcion "Agregar" podremos agregar Clientes, Empleados, Libros y material audiovisual en la DB

11. En el NavBar -> Opcion "Buscar" podremos Buscar Clientes, Empleados, Libros y material audiovisual en la DB

12. En el NavBar -> Opcion "Listar" podremos ver los Clientes, Empleados, Libros y material audiovisual cargados en la DB

13. En el NavBar -> Opcion "links" se agregaron algunos enlaces externos

14. Para acceder al administrador de la página, dirigirse a http://127.0.0.1:8000/admin y tipear el usuario: "LibAdmin" y la contraseña "Admin1234".

