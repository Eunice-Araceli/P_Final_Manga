import pandas as pd
from WebScrapping import WS_Manga as wm
from WebScrapping import WS_Rank as wr


def opciones():
    print("""Menu:
1: WebScrapping
2: Base de Datos
3: Dashboard 
4: Salir 
    """)
    opc=int(input("Ingresa la opcion: "))
    return opc

def opciones_submenu():
        print("""Menu:
    1: Rank
    2: Manga Data
    3: Ventas (Japon)
    4: Regresar
        """)
        sub_opc = int(input("Ingresa la opcion: "))
        return sub_opc

def submenu():
    seguir=True
    while seguir==True:
        sub_opc = opciones_submenu()
        if sub_opc == 1:
            wr.web()
        elif sub_opc == 2:
            rank_manga=pd.read_csv("DataSet/rank_manga.csv",sep=";")
            wm.manga(rank_manga)
        elif sub_opc == 3:
            print("opc33")
        elif sub_opc == 4:
            seguir=False
        else:
            print("Opcion invalida")

def menu():
    seleccion = True
    while seleccion == True:
        opc = opciones()
        if opc==1:
            submenu()
        elif opc==2:
            print("opc2")
        elif opc==3:
            print("opc3")
        elif opc==4:
            seleccion = False
        else:
            print("Opcion invalida")

if __name__ == "__main__":
    menu()