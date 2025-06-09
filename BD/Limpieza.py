import pandas as pd

def leer_csv():
    df=pd.read_csv("DataSet/data_manga.csv",sep=";")
    return df

def separar_listas(df:pd.DataFrame,colum):
    df[colum] = df[colum].bfill()
    borrar_1= df[colum].str.replace("'", "").str.replace("]", "").str.replace("[", "").str.replace("'", "").str.upper()
    colum = list(borrar_1.str.split(","))
    Unica = {"NOMBRE": []}
    Manga_Agregacion={"ID_MANGA": [], "COLUMNA": []}
    for c_indice, c_item in enumerate(colum):
        for cc_indice, cc_item in enumerate(c_item):
            item=cc_item.strip()
            if item not in Unica["NOMBRE"]:
                Unica["NOMBRE"].append(item)
            Manga_Agregacion["ID_MANGA"].append(c_indice)
            Manga_Agregacion["COLUMNA"].append(Unica["NOMBRE"].index(item))
            df_Manga_Agregacion=pd.DataFrame(Manga_Agregacion)
            df_Unica=pd.DataFrame(Unica)
    return  df_Unica,df_Manga_Agregacion

def nuevo_df():
    df = leer_csv()
    colum = "Generos"
    df_1_Gen, df_2_Gen = separar_listas(df, colum)
    df_2_Gen.rename(columns={"COLUMNA": "ID_GENERO"}, inplace=True)
    colum = "Temas"
    df_1_Tem, df_2_Tem = separar_listas(df, colum)
    df_2_Tem.rename(columns={"COLUMNA": "ID_TEMA"}, inplace=True)
    colum = "Demografia"
    df_1_Dem,df_2_Dem = separar_listas(df, colum)
    df_2_Dem.rename(columns={"COLUMNA": "ID_DEMOGRAFIA"}, inplace=True)
    df_1_Gen["ID_GENERO"] = df_1_Gen.index
    df_2_Gen["ID_MANGA_GENERO"] = df_2_Gen.index
    df_1_Tem["ID_TEMA"] = df_1_Tem.index
    df_2_Tem["ID_MANGA_TEMA"] = df_2_Tem.index
    df_1_Dem["ID_DEMOGRAFIA"] = df_1_Dem.index
    df_2_Dem["ID_MANGA_DEMOGRAFIA"] = df_2_Dem.index
    return df_1_Gen,df_2_Gen,df_1_Tem,df_2_Tem,df_1_Dem,df_2_Dem

def transformar_fecha(df:pd.DataFrame):
    borrar_1= df.Año.str.replace(",", "")
    colum = list(borrar_1.str.split("to"))
    Estreno=[]
    Fecha = ""
    for c in colum:
        l=list(c[0].strip().split(" "))
        if len(l)==4:
            Fecha+=l[2]
            if l[0]=="Jan":
                Fecha+="/01/"
            elif l[0] == "Feb":
                Fecha += "/02/"
            elif l[0] == "Mar":
                Fecha += "/03/"
            elif l[0] == "Apr":
                Fecha += "/04/"
            elif l[0] == "May":
                Fecha += "/05/"
            elif l[0] == "Jun":
                Fecha += "/06/"
            elif l[0] == "Jul":
                Fecha += "/07/"
            elif l[0] == "Aug":
                Fecha += "/08/"
            elif l[0] == "Sep":
                Fecha += "/09/"
            elif l[0] == "Oct":
                Fecha += "/10/"
            elif l[0] == "Nov":
                Fecha += "/11/"
            elif l[0] == "Dec":
                Fecha += "/12/"
            else:
                Fecha += ""
            Fecha += l[3]
            Estreno.append(Fecha)
        elif len(l) == 1:
            Estreno.append(l[0])
        else:
            Estreno.append(None)
        Fecha=""
    df.Año=Estreno
    df.Año = pd.to_datetime(df.Año, errors="coerce",dayfirst=True)
    df.rename(columns={"Año": "Estreno"}, inplace=True)
    return df

def transformar_datos_simples(df:pd.DataFrame):
    df.Volumenes= pd.to_numeric(df.Volumenes,errors="coerce")
    df.Capitulos = pd.to_numeric(df.Capitulos, errors="coerce")
    df.Lectores = df.Lectores.str.replace(",", "")
    df.Lectores = pd.to_numeric(df.Lectores, errors="coerce")
    df.Status = df.Status.str.replace("On Hiatus","Hiatus")
    df.Editorial = df.Editorial.str.replace("\n","")
    return df

def transformar_df_rank():
    df = pd.read_csv("DataSet/rank_manga.csv", sep=";")
    df.Rank = pd.to_numeric(df.Rank, errors="coerce")
    df.Titulo = df.Titulo.str.strip().str.upper()
    df.Calificacion = pd.to_numeric(df.Calificacion, errors="coerce")
    df.Link = df.Link.str.strip().str.upper()
    df["ID_RANK"] = df.index
    df["ID_MANGA"] = df.index
    df.drop(columns='Unnamed: 0',inplace=True)
    return df

def separar_artista_escritor():
    df = leer_csv()
    df.Autor = df.Autor.str.replace("\n", "").str.replace(",", "").str.replace(")", "(").str.strip()
    lista=list(df.Autor)
    Escritor={"NOMBRE":[]}
    Artista={"NOMBRE":[]}
    Manga_Escritor={"ID_MANGA":[],"ID_ESCRITOR":[]}
    Manga_Artista={"ID_MANGA":[],"ID_ARTISTA":[]}
    for l_indice, l_item in enumerate(lista):
        lista_lista=list(l_item.split("("))
        for ll_indice, ll_item in enumerate(lista_lista):
            lista_lista[ll_indice] = ll_item.strip()
            if "Story" in ll_item:
                if lista_lista[ll_indice-1] not in Escritor["NOMBRE"]:
                    Escritor["NOMBRE"].append(lista_lista[ll_indice - 1])
                Manga_Escritor["ID_MANGA"].append(l_indice)
                Manga_Escritor["ID_ESCRITOR"].append(Escritor["NOMBRE"].index(lista_lista[ll_indice - 1]))
            if "Art" in ll_item:
                if lista_lista[ll_indice-1] not in Artista["NOMBRE"]:
                    Artista["NOMBRE"].append(lista_lista[ll_indice - 1])
                Manga_Artista["ID_MANGA"].append(l_indice)
                Manga_Artista["ID_ARTISTA"].append(Artista["NOMBRE"].index(lista_lista[ll_indice - 1]))

    df_Esc=pd.DataFrame(Escritor)
    df_Man_Esc=pd.DataFrame(Manga_Escritor)
    df_Art=pd.DataFrame(Artista)
    df_Man_Art=pd.DataFrame(Manga_Artista)
    df_Esc["ID_ESCRITOR"] = df_Esc.index
    df_Man_Esc["ID_MANGA_ESCRITOR"] = df_Man_Esc.index
    df_Art["ID_ARTISTA"] = df_Art.index
    df_Man_Art["ID_MANGA_ARTISTA"] = df_Man_Art.index
    return df_Esc,df_Man_Esc,df_Art,df_Man_Art

def df_manga_limpio():
    df = leer_csv()
    df = transformar_fecha(df)
    df = transformar_datos_simples(df)
    df_new=df.drop(columns=['Unnamed: 0','Generos', 'Demografia','Temas','Autor'])
    df_new["ID_MANGA"] =df_new.index
    return df_new