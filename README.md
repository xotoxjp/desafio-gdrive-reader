# desafio-gdrive-reader
Desarrollar una aplicacion para inventariar en una Base de Datos todos los archivos pertenecientes a la unidad de Drive de un usuario

La base de datos debe ser creada desde la aplicación, pudiendose utilizar cualquier motor (por ejemplo MySQL o Redis). Dicha base deberá almacenar el nombre del archivo, la extensión, el owner del archivo, la visibilidad (público o privado) y la fecha de última modificación.

En el caso de encontrar archivos que estén configurados como públicos y puedan ser accedidos por cualquier persona, deberá modificar dicha configuración para establecer el archivo como privado y enviar un e-mail al owner notificacndo el cambio realizado.

La aplicación deberá tener la lógica necesaria para guardar en la base sólo aquellos archivos que no hayan sido almacenados en alguna corrida anterior o actualizar la fecha de modificación o cualquier otro dato en caso de corresponder. Asimismo, deberá mantener un inventaio histórico de todos los archivos que fueron en algún momento públicos.

Esta aplicación debe ser desarrollada en Python y deberá contar con tests que verifiquen su buen funcionamiento.

### Bonus:
- Aplicar buenas prácticas de programación
- Documentación y bibliografía consultada
- Tratamiento seguro de las credenciales utilizadas
- Dockerizar la aplicación

## Objetivos de Desarrollo
- Conexion google drive API
  - [x] Acceso a unidad gdrive
  - [X] Lectura de contenido gdrive

- Conexion base de datos
  - [X] Acceso a DB
  - [ ] Si no existe Tabla crear una

- Discriminar archivos publicos o privados
  - [ ] si archivo es publico pasar cambiar visibility a privado
  - [ ] guardar registro de archivo con cambio de visibility en DB
  - [ ] enviar e-mail a owner notificando cambio

- Guardar registros obtenidos de gdrive
  - [X] si no existe hacer insert de lo obtenido
  - [ ] si existe y fecha de modificacion es diferente hacer UPDATE a la version mas reciente
  - [ ] sino ignorar el registro

## Desarrollo del desafío
### Aplicar buenas prácticas de programación
Se utiliza modularidad separando entre funciones las distintas funcionalidades

### Tratamiento seguro de las credenciales utilizadas
se utiliza gitignore para no exponer credenciales en github
se utilizan archivos externos para almacenar credenciales

### Documentación y bibliografía consultada
https://programmerclick.com/article/32241570742/

https://swharden.com/blog/2021-05-15-python-credentials/
https://stackoverflow.com/questions/25501403/storing-the-secrets-passwords-in-a-separate-file

https://developers.google.com/drive/api/v3/quickstart/python
https://developers.google.com/drive/api/v3/about-sdk
https://developers.google.com/drive/api/guides/about-files
https://developers.google.com/drive/api/v3/reference/files/list
https://developers.google.com/drive/api/v3/reference/permissions
https://stackoverflow.com/questions/62858395/list-google-drive-files-metadata

https://www.w3schools.com/python/python_mysql_getstarted.asp
https://pynative.com/python-mysql-insert-data-into-database-table/

https://towardsdatascience.com/how-do-i-extract-nested-data-in-python-4e7bed37566a

https://developers.google.com/drive/api/guides/about-auth
