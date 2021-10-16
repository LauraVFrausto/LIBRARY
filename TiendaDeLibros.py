from datetime import date, datetime, timedelta
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
    while True:
        nombre_vendedor=input('Nombre del vendedor: ')
        nombre_articulo=input('Ingrese el titulo: ')
        vendedor_idx= buscar_elemento(lista_vendedores, vendedores.NOMBRE, nombre_vendedor.title())
        articulo_idx= buscar_elemento(lista_productos, ventas.TITULO,nombre_articulo.title())
        if articulo_idx != -1 and nombre_vendedor!=-1:
            break
        else:
            print('El vendedor o articulo no esta regitrado')
    cantidad=int(input('Cantidad que desea adquirir: '))
    if int(lista_productos[productos.EXISTENCIA][articulo_idx])>cantidad:
        total=cantidad*int(lista_productos[productos.PRECIO][articulo_idx])
        print(f'Cantidad suficiente, el total de la compra es {total}')
        existecia_nueva=int(lista_productos[productos.EXISTENCIA][articulo_idx])-cantidad
        lista_productos[productos.EXISTENCIA][articulo_idx]=str(existecia_nueva)
        hoy= date.today()
        format = hoy.strftime('%d/%m/%Y')
        lista_ventas[ventas.VENDEDOR_ID].append(str(vendedor_idx+1)) #Cambios en ventas
        lista_ventas[ventas.TITULO].append(nombre_articulo.title())
        lista_ventas[ventas.FECHA].append(format)
        lista_ventas[ventas.CANTIDAD].append(str(cantidad))
        lista_ventas[ventas.TOTAL].append(str(total))
        lista_productos[productos.EXISTENCIA].append(str(existecia_nueva)) #cambia la existencia del producto (-)
        print(lista_productos)
        
    elif int(lista_productos[productos.EXISTENCIA][articulo_idx])<cantidad and int(lista_productos[productos.EXISTENCIA][articulo_idx])>0:
        print(f'En existencia hay: {lista_productos[productos.EXISTENCIA][articulo_idx]}')
        continuar_compra=input('Cantidad no suficiente, desea continuar con la compra S/N:')
        if continuar_compra=='S':
            print(f'El total de la compra es {int(lista_productos[productos.EXISTENCIA][articulo_idx])*int(lista_productos[productos.PRECIO][articulo_idx])}')
            total=int(lista_productos[productos.EXISTENCIA][articulo_idx])*int(lista_productos[productos.PRECIO][articulo_idx])
            existencia_actual=int(lista_productos[productos.EXISTENCIA][articulo_idx])
            existecia_nueva=int(lista_productos[productos.EXISTENCIA][articulo_idx])-int(lista_productos[productos.EXISTENCIA][articulo_idx])
            lista_productos[productos.EXISTENCIA][articulo_idx]=str(existecia_nueva)
            hoy= date.today()
            format = hoy.strftime('%d/%m/%Y')
            lista_ventas[ventas.VENDEDOR_ID].append(str(vendedor_idx+1)) #Cambios en ventas
            lista_ventas[ventas.TITULO].append(nombre_articulo.title())
            lista_ventas[ventas.FECHA].append(format)
            lista_ventas[ventas.CANTIDAD].append(str(existencia_actual))
            lista_ventas[ventas.TOTAL].append(str(total))
            lista_productos[productos.EXISTENCIA].append(str(existecia_nueva)) #cambia la existencia del producto (-)
        else:
            print('Compra cancelada')
    else:
        print(f'No hay en existencia de este producto, se estima que llegara nuevo producto el {lista_productos[productos.FECHA_RESURTIDO][articulo_idx]}')
    
    lista_str= ""
    for lines in lista_productos:
        for idx, element in enumerate(lines):
            if idx == len(lines) - 1:
                lista_str += str(element) + "\n"
            else:
                lista_str += str(element) + "," 

    lista_str= lista_str.strip()
    ruta_prod=Path("archivos","productos.csv")
    archivo_prod=(open(ruta_prod,"w"))
    archivo_prod.write(lista_str)
    archivo_prod.close()

    lista_st= ""
    for lines in lista_ventas:
        for idx, element in enumerate(lines):
            if idx == len(lines) - 1:
                lista_st += str(element) + "\n"
            else:
                lista_st += str(element) + "," 

    lista_st= lista_st.strip()
    ruta_prod=Path("archivos","ventas.csv")
    archivo_prod=(open(ruta_prod,"w"))
    archivo_prod.write(lista_st)
    archivo_prod.close()
    

def registar_articulo():
    print("Registra artículo")
    articulo = str(input("Escriba el nombre del articulo: "))
    articulo = articulo.title()
    cantidad = int(input("Escriba la cantidad: "))
    lenght = int(len(lista_productos[1]))
    if articulo in lista_productos[1]:
        for i in range(0,lenght):
            if  articulo in lista_productos[1][i]:
                    idx = i       
        numero_en_inv= int(lista_productos[6][idx])
        nuevo_num= numero_en_inv+cantidad
        lista_productos[6][idx] = nuevo_num
    else:
        print("Articulo no en inventario, desea registrarlo?")
        respuesta = str(input(">>>"))
        respuesta.title()
        if respuesta == "Si":
            nuevo_id= int(len(lista_productos[0])) +1
            lista_productos[0].append(nuevo_id)
            lista_productos[1].append(articulo)
            autor=str(input("Escriba el nombre del autor: "))
            autor.title()
            lista_productos[2].append(autor)
            editorial=str(input("Escriba el nombre de la editorial: "))
            lista_productos[3].append(editorial)
            genero=str(input("Escriba el genero del libro: "))
            genero.title()
            lista_productos[4].append(genero)
            precio=str(input("Escriba el precio del libro: "))
            lista_productos[5].append(precio)
            lista_productos[6].append(cantidad)
            fecha=str(input("Escriba la fecha de resurtido (dd/mm/yy): "))
            lista_productos[7].append(fecha)
    lista_str= ""
    for lines in lista_productos:
        for idx, element in enumerate(lines):
            if idx == len(lines) - 1:
                lista_str += str(element) + "\n"
            else:
                lista_str += str(element) + "," 

    lista_str= lista_str.strip()
    ruta_prod=Path("archivos","productos.csv")
    archivo_prod=(open(ruta_prod,"w"))
    archivo_prod.write(lista_str)
    archivo_prod.close()

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
    fecha_inicio=input('Ingrese fecha de inicio (YYYY,mm,dd): ')
    fecha_final=input('Ingrese fecha final (YYYY,mm,dd): ')
    f_i=fecha_inicio.split('/')
    f_f=fecha_final.split('/')
    f_inicio=[]
    f_final=[]
    for i in f_i:
        f_inicio.append(int(i))
    for j in f_f:
        f_final.append(int(j))
    print(f_inicio, f_final)
    inicio=datetime(f_inicio)
    fin=datetime(f_final)
    diferencia = fin - inicio
    print (diferencia)
    lista_fecha = [inicio]
    lista_fecha = [fecha for fecha in (inicio, fin)]
    print(lista_fecha)

def reporte_ventas_vendedor():
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

def reporte_ventas_articulo():
    while True:
        nombre_artiuclo=input('Ingrese nombre del articulo: ')
        articulo_idx= buscar_elemento(lista_productos, ventas.TITULO,nombre_artiuclo.title())
        if articulo_idx != -1:
            break
        else:
            print('El articulo no esta regitrado')
    ventas_articulo = []
    for idx, id in enumerate(lista_ventas[ventas.TITULO]):
        if articulo_idx == idx:
            ventas_articulo.append(idx)
    report_articulo=[[],[],[]]
    for idx in ventas_articulo:
        vendedor_id= lista_ventas[ventas.VENDEDOR_ID][idx]
        vendedor=lista_vendedores[vendedores.NOMBRE][int(vendedor_id)-1]
        report_articulo[0].append(vendedor)
        cantidad=lista_ventas[ventas.CANTIDAD][idx]
        report_articulo[1].append(cantidad)
        total=lista_ventas[ventas.TOTAL][idx]
        report_articulo[2].append(total)
    print()
    print_matriz(report_articulo, ["VENDEDOR", "CANTIDAD", "TOTAL"])

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