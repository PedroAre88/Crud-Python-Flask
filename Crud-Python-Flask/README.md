Pasos a seguir para ejecutar la aplicacion

1 Construir imagen de Docker con el comando docker build --tag nombredelaimagen .
#2 Ejecutar el contenedor de la imagen ya creada docker run -it -d -p 5000:5000 --name nombredelaimagen nombredelservicio 

Opcional: En caso de que se desee correr la aplicacion en el puerto ya definido pueden ejecutar el comando python main.py