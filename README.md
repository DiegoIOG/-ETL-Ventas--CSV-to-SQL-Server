# ETL Ventas -CSV to SQL Server

En el proyecto realizado se resolvio un problema comun que se tiene en muchas empresas realconado con archivos .csv sin procesar dentro de una base de datos ,lo mas comun es recibir archivos sin procesar que deben ser movidos a un base de datos para que se tenga el historial de esto, por lo cual mediante este proyecto se tubo la idea de colocar estos archivos .csv en una carpeta raw para luego ser subidos a sql enseguida tambien a una carpeta procesada para diferenciar entre lo que se le se  esta subido, en cuanto el procesamiento este se llevara cada que la produccion lo necesite en nuestro caso cada 5 min, de esta manera mantenemos los datos conforme a tiempo y forma.para solucionar al autoamtizacion se considero el programdor de tareas ("task schedule") aunque dependiendo de donde se trabaje se puede usar el crotnab de linux, de esta manera se automatiza el proceso.

## Flujo ETL
1-Generacion de los .csv en python
2-Lectura de archivos desde al carpeta 'raw'
3-Insercion de datos en SQL Server usando pyodbc
4-movimiento de archivos procesados a carpeta 'processed'

## Video del funcionamiento 
https://youtu.be/396isNS27aE


## ¿Que se busca con este proyecto?
-Reduccion de tiempo automatizando las cargas de .csv automaticamente a sql
-Reduccion de espacio al poder decidir si mantener los archivos .csv o la informacion dnetro de sql 
-Ingest de datos constante 
-Mejor visualizacion de dashboard debido a la constante ingesta que nos permite tomar decisiones de manera mas rapida





