from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import time

def sacar_varios_datos(lista):
    ln1 = list(lista[1].split(","))
    lf = []
    for l in ln1:
        ln2 = list(l.strip().split("\n"))
        if ln2[0] not in lf:
            lf.append(ln2[0])
    return lf

def manga(rank_manga):
    manga = {"Volumenes": [], "Capitulos": [], "Status": [], "Año": [], "Generos": [],"Temas":[],
             "Demografia": [], "Editorial": [], "Autor": [], "Lectores": []}
    for ra in (rank_manga["Link"]):
        driver = ChromeDriverManager().install()
        s = Service(driver)
        opc = Options()
        opc.add_argument("--window-size=1020,1200")
        navegador = webdriver.Chrome(service=s, options=opc)
        navegador.get(ra)
        time.sleep(5)
        soup = BeautifulSoup(navegador.page_source, "html.parser")
        info = soup.find_all("div", attrs={"class": "spaceit_pad"})
        time.sleep(10)
        lista_dic = [None, None, None, None, None, None, None, None, None, None]
        for i in info:
            lista=i.text.strip().split(":")
            if lista[0]=="Volumes":
                lista_dic[0]=lista[1]
            elif lista[0]=="Chapters":
                lista_dic[1]=lista[1]
            elif lista[0]=="Status":
                lista_dic[2]=lista[1]
            elif lista[0]=="Published":
                lista_dic[3]=lista[1]
            elif lista[0] == "Genres":
                dato=sacar_varios_datos(lista)
                lista_dic[4]=dato
            elif lista[0] == "Genre":
                dato = sacar_varios_datos(lista)
                lista_dic[4]=dato
            elif lista[0] == "Theme":
                dato=sacar_varios_datos(lista)
                lista_dic[5]=dato
            elif lista[0] == "Themes":
                dato = sacar_varios_datos(lista)
                lista_dic[5]=dato
            elif lista[0] == "Demographic":
                dato=sacar_varios_datos(lista)
                lista_dic[6]=dato
            elif lista[0] == "Demographics":
                dato = sacar_varios_datos(lista)
                lista_dic[6]=dato
            elif lista[0] == "Serialization":
                lista_dic[7] = lista[1]
            elif lista[0]=="Authors":
                lista_dic[8]=lista[1]
            elif lista[0]=="Author":
                lista_dic[8]=lista[1]
            elif lista[0]=="Members":
                lista_dic[9]=lista[1]
            else:
                continue
        manga["Volumenes"].append(lista_dic[0])
        manga["Capitulos"].append(lista_dic[1])
        manga["Status"].append(lista_dic[2])
        manga["Año"].append(lista_dic[3])
        manga["Generos"].append(lista_dic[4])
        manga["Temas"].append(lista_dic[5])
        manga["Demografia"].append(lista_dic[6])
        manga["Editorial"].append(lista_dic[7])
        manga["Autor"].append(lista_dic[8])
        manga["Lectores"].append(lista_dic[9])
        lista_dic = [None, None, None, None, None, None, None, None, None, None]
        navegador.close()
    df = pd.DataFrame(manga)
    df.to_csv("DataSet/data_manga.csv",sep=";")
