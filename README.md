# Instrucciones


## Django

Para poder correr el proyecto es recomendable crear un entorno virtual para descargar las dependencias de nuestro proyecto.

Para crear un entorno virtual se tiene que ejecutar el comando 

    python3 -m venv [nombre-env]

### `[nombre-env] es una variable, es decir, puedes poner cualquier nombre que gustes, como 'entorno', 'env', etc`

Una vez creado se deberán activar el entorno virtual
    source nombre-env/bin/activate

Ya activado se deberan instalar las dependencias del archivo requeriments.txt
    pip3 install -r requirements.txt

## Base de datos

Dentro del proyecto hay un archivo de docker compose que contiene la base de datos y el usuario necesaria para el proyecto.

Para levantar el contenedor hay que introducir el siguiente comando:

    docker compose up -d

ya levantado nuestra base de datos se harán las migraciones con los siguientes comandos: 

    python3 manage.py makemigrations
    python3 manage.py migrate

## Backup

Ahora cargaremos los datos de las tablas catálogo, ejecutamos el siguiente comando (estando dentro de la carpeta del proyecto).

Nombre del backup
### `backup.txt`

Comando para acceder a la base de datos

    docker exec -it postgres_santillana psql db_santillana usr_santillana

---

### `Paso 1: Entrar a la base de datos con el comando para acceder a la base de datos. `

### `Paso 2: Copiar el contenido del archivo backup.txt y pegarlo en la terminal recíen iniciada.`

### `Paso 3: Para salir de la consola de SQL '\q'`

## Cargar el servidor

correremos la aplicación con el comando:

    python manage.py runserver

## Borrar Docker Compose

Para borrar el contenedor y lo relacionado use el comando.

    docker compose down -v

## Swagger y Redoc

Tambien se añadio swagger para que pueda ver los endpoints generados en el proyecto y pueda probarlos desde ahi. Se encuentra en la ruta: 

### `http://127.0.0.1:8000/docs/`
### `http://127.0.0.1:8000/redoc/`
