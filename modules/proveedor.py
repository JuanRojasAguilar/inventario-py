from . import corefiles as cf

def Add_Proveedor(dataInventario):
    nit = input('Ingrese el Nit')
    nombrePro = input('Ingrese el Nombre')
    tipo = input('Ingrese el Tipo de persona Natura o Juridica')
    ciudad = input('Ingrese la Ciudad')
    ubicacion = input('Ingrese la Ubicacion')
    longitud = float(input('Ingrese la Longitud'))
    latitud = float(input('Ingrese la Latitud'))
    proveedor={
        'nit':nit,
        'nombrePro':nombrePro,
        'tipo':tipo,
        'direccion':{
            'ciudad':ciudad,
            'ubicacion':ubicacion,
            'longitud':longitud,
            'latitud':latitud
        }
    }
    dataInventario.get('proveedores').update({nit:proveedor})
    cf.createData('inventario.json',dataInventario)

def searchProv(data):
    valor = input("Ingrese el Nit del proveedor a buscar -> ")
    result= data['proveedores'].get(valor)
    nit,nombrePro,tipo,direccion = result.values()
    ciudad,ubicacion,longitud,latitud = direccion.values()
    print(f'Nit {nit}:')
    cf.pausar_pantalla()

