from BD import Constantes_BD as c
from sqlalchemy import create_engine, text

def Crear_Schema():
     try:
        cadena_con = f"mysql+mysqlconnector://{c.USER}:{c.PASSWORD}@{c.HOST}"
        engine = create_engine(cadena_con)
        with engine.connect() as conexion:
            conexion.execute(text("CREATE SCHEMA  `MANGA`;"))
     except:
         print("""---------------------------------
    La base de datos ya existe
    ---------------------------------""")

def Crear_Tablas():
    try:
        cadena_con = f"mysql+mysqlconnector://{c.USER}:{c.PASSWORD}@{c.HOST}/{c.DATABASE}"
        engine = create_engine(cadena_con)
        with open("DataSet/BD_MANGA.sql", "r", encoding="utf-8") as archivo:
            query = archivo.read()
        sentencias = query.split(";")
        with engine.connect() as conexion:
            for sentencia in sentencias:
                if sentencia.strip():
                    conexion.execute(text(sentencia))
    except:
        print("""---------------------------------
Error Selecciona otra opcion
---------------------------------""")
