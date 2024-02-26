import sys
import os
import json

BASE="data/"

def borrar_pantalla():
    if sys.platform == "linux" or sys.platform == "darwin":
        os.system("clear")
    else:
        os.system("cls")

def pausar_pantalla():
    if sys.platform == "linux" or sys.platform == "darwin":
        x = input("Presione una tecla para continuar...")
    else:
        os.system("pause")

def checkFile(archivo:str,data):
    if os.path.isfile(BASE+ archivo):
        with open(BASE+archivo, "r") as file:
            return json.load(file)
    else:
        with open(BASE + archivo ,"w") as bw:
            data = {
                'proveedores':{},
                'productos':{},
            }
            json.dump(data,bw,indent=4)
            return data

def createData(archivo:str,data):
    with open(BASE+archivo,"w+") as rwf:
        json.dump(data,rwf,indent=4)

def updateData(data,srcData,id,diccionario):
    if (len(data) <=0):
        print('😎 No se encontro información 😎')
        os.system('pause')
    else:
        for key in data.keys():
            if(key != id):
                if(type(data[key]) == dict):
                    for key2 in data[key].keys():
                        if(bool(input(f'Desea modificar el {key2} s(si) o Enter No'))):
                            os.system('cls')
                            data[key][key2] = input(f'Ingrese el nuevo valor para {key2} :')
                else:
                    if(bool(input(f'Desea modificar el {key} s(si) o Enter No'))):
                        os.system('cls')
                        data[key] = input(f'Ingrese el nuevo valor para {key} :')
        srcData[diccionario].update({data[id]:data})
        UpdateFile('inventario.json',srcData)
    os.system('pause')

def UpdateFile(archivo,data):
    with open(BASE+ archivo,'w+') as fw:
        json.dump(data,fw,indent=4)

def delData(data, id:str, diccionario:str):
    delVal = input(f"Ingrese el {id} que desea borrar -> ")
    data[diccionario].pop(delVal)
    UpdateFile('inventario.json',data)

