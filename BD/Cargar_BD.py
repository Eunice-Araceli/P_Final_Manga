from sqlalchemy import create_engine
from BD import Constantes_BD as c
from BD import Limpieza as limp

def insertar():
    try:
        cadena_con = f"mysql+mysqlconnector://{c.USER}:{c.PASSWORD}@{c.HOST}/{c.DATABASE}"
        engine = create_engine(cadena_con)
        with engine.connect() as conexion:
            df_Manga = limp.df_manga_limpio()
            df_Manga.to_sql("mangas", con=conexion, if_exists="append", index=False)
            df_rank = limp.transformar_df_rank()
            df_rank.to_sql("ranks", con=conexion, if_exists="append", index=False)
            df_Esc, df_Man_Esc, df_Art, df_Man_Art = limp.separar_artista_escritor()
            df_Esc.to_sql("escritores", con=conexion, if_exists="append", index=False)
            df_Man_Esc.to_sql("manga_escritor", con=conexion, if_exists="append", index=False)
            df_Art.to_sql("artistas", con=conexion, if_exists="append", index=False)
            df_Man_Art.to_sql("manga_artista", con=conexion, if_exists="append", index=False)
            df_1_Gen,df_2_Gen,df_1_Tem,df_2_Tem,df_1_Dem,df_2_Dem= limp.nuevo_df()
            df_1_Gen.to_sql("generos",con=conexion,if_exists="append", index=False)
            df_2_Gen.to_sql("manga_genero", con=conexion, if_exists="append", index=False)
            df_1_Tem.to_sql("temas", con=conexion, if_exists="append", index=False)
            df_2_Tem.to_sql("manga_tema", con=conexion, if_exists="append", index=False)
            df_1_Dem.to_sql("demografias", con=conexion, if_exists="append", index=False)
            df_2_Dem.to_sql("manga_demografia", con=conexion, if_exists="append", index=False)
    except:
        print("""---------------------------------
Error Selecciona otra opcion
---------------------------------""")