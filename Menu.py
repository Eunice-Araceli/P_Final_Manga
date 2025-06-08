import pandas as pd
from WebScrapping import WS_Manga as wm
from WebScrapping import WS_Rank as wr
from BD import Crear_BD as cbd
from BD import Cargar_BD as carbd


def opciones():
    print("""Menu:
1: WebScrapping
2: Base de Datos
3: Dashboard 
4: Salir 
    """)
    opc=int(input("Ingresa la opcion: "))
    return opc

def opciones_submenu_web():
        print("""Menu:
    1: Rank
    2: Manga Data
    3: Regresar
        """)
        sub_opc = int(input("Ingresa la opcion: "))
        return sub_opc

def opciones_submenu_bd():
    print("""Menu:
    1: Crear Base de Datos
    2: Crear Tablas
    3: Cargar Datos
    4: Regresar
        """)
    sub_opc = int(input("Ingresa la opcion: "))
    return sub_opc

def submenu_webscrapping():
    seguir=True
    while seguir==True:
        sub_opc = opciones_submenu_web()
        if sub_opc == 1:
            wr.web()
        elif sub_opc == 2:
            rank_manga=pd.read_csv("DataSet/rank_manga.csv",sep=";")
            wm.manga(rank_manga)
        elif sub_opc == 3:
            seguir=False
        else:
            print("Opcion invalida")

def submenu_bd():
    seguir = True
    while seguir == True:
        sub_opc = opciones_submenu_bd()
        if sub_opc == 1:
            cbd.Crear_Schema()
        elif sub_opc == 2:
            cbd.Crear_Tablas()
        elif sub_opc == 3:
            carbd.insertar()
        elif sub_opc == 4:
            seguir = False
        else:
            print("Opcion invalida")

def menu():
    seleccion = True
    while seleccion == True:
        opc = opciones()
        if opc==1:
            submenu_webscrapping()
        elif opc==2:
            submenu_bd()
        elif opc==3:
            print("opc3")
        elif opc==4:
            seleccion = False
        else:
            print("Opcion invalida")

if __name__ == "__main__":
    menu()