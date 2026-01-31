Create Database ETL_project;
GO

Use ETL_project;
GO

Create table ventas(
id int IDENTITY (1,1) PRIMARY KEY ,
fecha date,
producto VARCHAR(50),
cantidad INT ,
precio Decimal (10,2)
);