#import datetime
from pathlib import Path
import productos
import vendedores
import ventas

lista_productos = []

lista_vendedores = []

lista_ventas = []

# print_matriz
# matriz: la matriz que quieres desplegar en la terminal
# nombre_columnas: una lista con los nombres de cada columna de la matriz
def print_matriz(matriz, nombre_columnas):
    bigger_size = []
    for nombre in nombre_columnas:
        bigger_size.append(len(nombre))
    
    for idx, fila in enumerate(matriz):
        for element in fila:
            if len(str(element)) > bigger_size[idx]:
                bigger_size[idx] = len(str(element))

    for i in range(len(nombre_columnas)):
        print(nombre_columnas[i].center(bigger_size[i] + 2), end = "")
    print()
    
    for i in range(len(matriz[0])):
        for j in range(len(nombre_columnas)):
            print(str(matriz[j][i]).title().center(bigger_size[j] + 2), end = "")
        print()

# buscar_elemento
# matriz: la tabla en la que deseas buscar
# columna: la columna de la tabla en la que deseas buscar
# valor: el valor que deseas buscar
# return: el indice del valor en la tabla o -1 si no esta
#              lista_vendedores, 1, mariana lopez
def buscar_elemento(matriz, columna, valor):
    if valor in matriz[columna]:
        return matriz[columna].index(valor)
    else:
        return -1

# obtener_id
# matriz: la tabla en la que deseas encontrar el identificador
# indice: el indice del elemento del que deseas encontrar el identificador o -1 si el indice es incorrecto
def obtener_id(matriz, indice):
    if indice < len(matriz[0]) and indice >= -len(matriz[0]):
        return matriz[0][indice]
    else:
        return -1

def menu():
    print()
    print("  Elija una de las siguientes opciones:")
    print("    1. Registrar ventas")
    print("    2. Registrar artículos")
    print("    3. Consultar inventario")
    print("    4. Consultar ventas")
    print("    5. Reporte de ventas por vendedor")
    print("    6. Reporte de ventas por artículo")
    print("    0. Guardar y salir")
    return int(input(">> "))

def registrar_venta():
    print("Registra venta")

def registar_articulo():
    print("Registra artículo")

def consultar_inventario():
    n=True
    while n:
        nombre_libro=input('Ingrese nombre del libro: ')
        for idx, linea in enumerate(lista_productos):
            if idx==1:
                if (str(nombre_libro.title()) in linea):
                    indice=linea.index(nombre_libro.title())
                    datos=[]
                    for i in lista_productos:
                        datos.append(i[indice])
                    for elemento in datos:
                        if datos.index(elemento)==0 or datos.index(elemento)==5:
                            print('', end="")
                        else:
                            print(elemento, end = "     ")
                    print()
                    n=False
                    #print( print_matriz(lista_productos, productos.COLUMNAS))
                else:
                    print('Libro no encontrado') 
                    continue 
    

def consultar_ventas():
    print("Consulta venta")

def reporte_ventas_vendedor():
<<<<<<< HEAD
    while True:
        nombre_vendedor=input('Ingrese nombre del vendedor: ')
        vendedor_idx= buscar_elemento(lista_vendedores, vendedores.NOMBRE, nombre_vendedor.title())
        if vendedor_idx != -1:
            break
        else:
            print('El vendedor no esta regitrado')
    vendedor_id= obtener_id(lista_vendedores, vendedor_idx)
    ventas_vendedor = []
    for idx, id in enumerate(lista_ventas[ventas.VENDEDOR_ID]):
        if vendedor_id == id:
            ventas_vendedor.append(idx)
    report_vendedor=[[],[],[]]
    for idx in ventas_vendedor:
        producto_id= lista_ventas[ventas.TITULO][idx]
        report_vendedor[0].append(producto_id)
        cantidad=lista_ventas[ventas.CANTIDAD][idx]
        report_vendedor[1].append(cantidad)
        total=lista_ventas[ventas.TOTAL][idx]
        report_vendedor[2].append(total)
    print_matriz(report_vendedor, ["TITULO", "CANTIDAD", "TOTAL"])
=======
    print("Genera reporte")
    n=True
    while n:
        nombre_vendedor=input('Ingrese nombre del vendedor: ')
        for idx, linea in enumerate(lista_ventas):
            if idx==0:
                if (str(nombre_vendedor.title()) in linea):
                    indice=linea.index(nombre_vendedor.title())
                    datos=[]
                    for i in lista_ventas:
                        datos.append(i[indice])
                    for elemento in datos:
                        if datos.index(elemento)==0 or datos.index(elemento)==2:
                            print('', end="")
                        else:
                            print(elemento, end = "     ")
                    print()
                    n=False
                    #print( print_matriz(lista_productos, productos.COLUMNAS))
                else:
                    print('Vendedor no encontrado') 
                    continue 



>>>>>>> 93db178b685559f43de1806d234b16540628a3ef

def reporte_ventas_articulo():
    print("Genera reporte")
    print("Cual es el nombre del producto: ")
    producto = input(">>")

    while True:
        producto_idx = buscar_elemento(lista_productos,ventas.TITULO,producto.title)
        if producto_idx !=-1:
            break
        else:
            print(f"El producto {producto.title()} no esta registrado")
    
    product_id = obtener_id()

def cargarvendedores():
    ruta_prod=Path('archivos', 'vendedores.csv')
    archivo_prod=(open(ruta_prod))
    contenido_prod=archivo_prod.readlines()
    for line in contenido_prod:
        lista_vendedores.append(line.strip().split(','))
    archivo_prod.close()

def cargarVentas():
    ruta_prod=Path('archivos', 'ventas.csv')
    archivo_prod=(open(ruta_prod))
    contenido_prod=archivo_prod.readlines()
    for line in contenido_prod:
        lista_ventas.append(line.strip().split(','))
    archivo_prod.close()

def cargarProductos():
    ruta_prod=Path('archivos', 'productos.csv')
    archivo_prod=(open(ruta_prod))
    contenido_prod=archivo_prod.readlines()
    for line in contenido_prod:
        lista_productos.append(line.strip().split(','))
    archivo_prod.close()

def buscar_elemento(matriz, columna, valor):
    if valor in matriz[columna]:
        return matriz[columna].index(valor)
    else:
        return -1

# obtener_id
# matriz: la tabla en la que deseas encontrar el identificador
# indice: el indice del elemento del que deseas encontrar el identificador o -1 si el indice es incorrecto
def obtener_id(matriz, indice):
    if indice < len(matriz[0]) and indice >= -len(matriz[0]):
        return matriz[0][indice]
    else:
        return -1

# obtener_precio
# matriz: la tabla en la que deseas encontrar el precio
# indice: el indice del elemento del que deseas encontrar el precio o -1 si el indice es incorrecto
def obtener_precio(matriz, indice):
    if indice < len(matriz[productos.PRECIO]) and indice >= -len(matriz[productos.PRECIO]):
        return matriz[productos.PRECIO][indice]
    else:
        return -1

#Abrir el archivo de producto y guarda en el la informacion que hay en lista_productos

def guardarProductos():
    string_content = ""
    for lines in lista_productos:
        for idx, element in enumerate(lines):
            if idx == len(lines) - 1:
                string_content += element + "\n"
            else:
                string_content += element + ","

    string_content = string_content.strip()
    ruta_productos = Path('archivos', 'productos.csv')
    archivo_productos = open(ruta_productos, "w")
    archivo_productos.write(string_content)
    archivo_productos.close()

def main():

    print("-" * 30)
    print("| Bienvenid@ a l |")
    print("-" * 30)
    cargarProductos()
    cargarVentas()
    cargarvendedores()
    while True:
        selected = menu()
        if selected == 0:
            guardarProductos()
            print("Gracias por su visita")
            break
        elif selected == 1:
            registrar_venta()
        elif selected == 2:
            registar_articulo()
        elif selected == 3:
            consultar_inventario()
        elif selected == 4:
            consultar_ventas()
            print_matriz(lista_ventas, ventas.COLUMNAS)
        elif selected == 5:
            reporte_ventas_vendedor()
        elif selected == 6:
            reporte_ventas_articulo()
        else:
            print(f"La opción {selected} no es válida")

main()