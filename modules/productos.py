from . import corefiles as cf 

def Add_Producto(data):
    codigo = input('Ingrese el codigo del producto: ')
    nombre = input('Ingrese el nombre: ')
    stockMin = int(input('Ingrese el stock minimo: '))
    stockActual = int(input('Ingrese el stock actual: '))
    stockMax = int(input('Ingrese el stock minimo: '))
    listaProveedor = []
    while True:
        proveedor = input(f"Ingresa el proveedor de {nombre}: ")
        listaProveedor.append(proveedor)
        opcion = input("Quieres ingresar otro proveedor? S(si) Enter(no)").upper()
        if opcion == "S":
            continue
        else:
            break

    if stock < stockMin and stock != 0:
        estado = "BAJO VOLUMEN"
    elif stock >= stockMin:
        estado = "DISPONIBLE"
    elif stock == 0:
        estado = "AGOTADO"

    producto={
        'codigo': codigo,
        'nombre': nombre,
        'stock': {
            'stockMin': stockMin,
            'stockActual': stockActual,
            'stockMax': stockMax
            },
        'estado' : estado,
        'proveedor': listaProveedor
    }
    data.get("productos").update({id:produto})
    cf.createData("inventario.json", data)

def searchProduct(data):
    identificador = input("Ingrese el ID exacto del producto: ")
    result = data["productos"].get(identificador)
    codigo, nombre, stock, estado, proveedor = result.values()
    stockMin, stockActual, stockMax = stock.values()
    print(f"ID: {codigo}")
