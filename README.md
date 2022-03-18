# desafio-gdrive-reader
Desarrollar una aplicacion para inventariar en una Base de Datos todos los archivos pertenecientes a la unidad de Drive de un usuario

La base de datos debe ser creada desde la aplicación, pudiendose utilizar cualquier motor (por ejemplo MySQL o Redis). Dicha base deberá almacenar el nombre del archivo, la extensión, el owner del archivo, la visibilidad (público o privado) y la fecha de última modificación.

En el caso de encontrr archivos que estén configurados como públicos y puedan ser accedidos por cualquier persona, deberá modificar dicha configuración para establecer el archivo como privado y enviar un e-mail al owner notificacndo el cambio realizado.

La aplicación deberá tener la lógica necesaria para guardar en la base sólo aquellos archivos que no hayan sido almacenados en alguna corrida anterior o actualizar la fecha de modificación o cualquier otro dato en caso de corresponder. Asimismo, deberá mantener un inventaio histórico de todos los archivos que fueron en algún momento públicos.

Esta aplicación debe ser desarrollada en Python y deberá contar con tests que verifiquen su buen funcionamiento.

### Bonus:
- Aplicar buenas prácticas de programación
- Documentación y bibliografía consultada
- Tratamiento seguro de las credenciales utilizadas
- Dockerizar la aplicación