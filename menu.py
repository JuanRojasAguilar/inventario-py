from tabulate import tabulate
import modules.corefiles as cf
import sys
from modules import proveedor as pv
from modules import productos as pp

inventario = None
inventario = cf.checkFile("inventario.json", inventario)

def main_menu():
    def wrapper(func):
        cf.borrar_pantalla()
        func()
        main_menu()
    
    cf.borrar_pantalla()
    titulo = """
    ++++++++++++++++++++++++
    +  MENU DE INVENTARIO  +
    ++++++++++++++++++++++++
    """
    print(titulo)
    menu =[["1.", "Administrar productos"], ["2.", "Administrar proveedores"], ["3.", "Compras"], ["4.", "Ventas"], ["5.", "Salir"]]
    print(tabulate(menu, tablefmt="grid"))
    opcion = input("\n>> ")
    if opcion == "1":
       wrapper(menu_productos) # <---- siempre llamar menus así
    elif opcion == "2":
        wrapper(menu_proveedores)
    elif opcion == "3":
        pass
    elif opcion == "4":
        pass
    elif opcion == "5":
        sys.exit("Vuelva pronto!")
    else:
        main_menu()

def menu_productos():
    titulo = """
    +++++++++++++++
    +  PRODUCTOS  +
    +++++++++++++++
    """
    print(titulo)
    menu = [["1.", "Agregar"],["2.","Editar"],["3.", "Eliminar"],["4.","Buscar"],["5.","Salir"]]
    print(tabulate(menu, tablefmt="grid"))
    opcion = input("\n>> ")
    if opcion == "1":
        pp.Add_Producto(inventario)
    elif opcion == "2":
        palabra = input('Ingrese el Nro de identificacion del producto a modificar')
        cf.updateData(inventario.get('productos').get(palabra,{}),inventario,"id","productos")
    elif opcion == "3":
        cf.delData(inventario,"nit","proveedores")
    elif opcion == "4":
        pp.searchProduct(inventario)
    elif opcion == "5":
        main_menu()
    else:
        menu_productos()

def menu_proveedores():
    titulo = """
    +++++++++++++++
    +  PROVEEDORES  +
    +++++++++++++++
    """
    print(titulo)
    menu = [["1.", "Agregar"],["2.","Editar"],["3.", "Eliminar"],["4.","Buscar"],["5.","Salir"]]

    print(tabulate(menu, tablefmt="grid"))
    opcion = input("\n>> ")
    if opcion == "1":
        pv.Add_Proveedor(inventario)
    elif opcion == "2":
        palabra = input('Ingrese el Nro de identificacion del proveedor a modificar')
        cf.updateData(inventario.get('proveedores').get(palabra,{}),inventario,"nit","proveedores")
    elif opcion == "3":
        cf.delData(inventario,"nit","proveedores")
    elif opcion == "4":
        pv.searchProv(inventario)
    elif opcion == "5":
        main_menu()
    else:
        menu_proveedores()

