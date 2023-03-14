# repair-suite
Software de propósito general orientado a talleres mecánicos.

## Manual de instalacion
 - Python3
 - Mysql
 
 ### Luego de hacer las instalaciones mencionadas anteriormente de realizar los sigientes pasos:
 
 1. git clone https://github.com/ediazgarcia/repair-suite.git
 2. cd repair-suite
 3. Instalar y Crear el entorno virtual:
  - pip install virtualenv
  - python3 -m venv venv
 
 4. pip install -r requirements.txt
 
 5.  Antes de ejecutar la aplicación, debe crear las siguientes variables de entorno:
- Crear el archivo .env en la raiz del proyecto y colocar estas variables y los datos correspondientes 

MYSQL_USER=

MYSQL_PASSWORD=

MYSQL_DATABASE=

MYSQL_HOST=

MYSQL_PORT=


 
 6. python index.py
 


