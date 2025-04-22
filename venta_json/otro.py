from components import Menu,Valida
from utilities import borrarPantalla,gotoxy
from utilities import reset_color,red_color,green_color,yellow_color,blue_color,purple_color,cyan_color
from clsJson import JsonFile
from company  import Company
from customer import RegularClient
from sales import Sale
from product  import Product
from iCrud import ICrud
import datetime
import time,os
from functools import reduce

path, _ = os.path.split(os.path.abspath(__file__))
# Procesos de las Opciones del Menu Facturacion
class CrudClients(ICrud):
    def create(self):
        validar = Valida()
        borrarPantalla()
        gotoxy(2,1);print("Ingreso de Cliente")
        gotoxy(2,2);nombre = input("Nombre: ")
        gotoxy(2,3);apellido = input("Apellido: ")
        gotoxy(2,4);dni = validar.solo_numeros("Error: Solo números", 10, 4)

        client = RegularClient(nombre, apellido, dni)
        json_file = JsonFile(path+'/archivos/clients.json')
        clientes = json_file.read()
        clientes.append(client.getJson())
        json_file.save(clientes)
        print("Cliente guardado con éxito")
        time.sleep(2)

    def update(self):
        validar = Valida()
        borrarPantalla()
        gotoxy(2,1);print("Actualizar Cliente")
        gotoxy(2,2);dni = validar.solo_numeros("Error: Solo números", 10, 2)

        json_file = JsonFile(path+'/archivos/clients.json')
        clientes = json_file.read()
        for c in clientes:
            if c['dni'] == dni:
                gotoxy(2,3);nombre = input("Nuevo Nombre: ")
                gotoxy(2,4);apellido = input("Nuevo Apellido: ")
                c['nombre'] = nombre
                c['apellido'] = apellido
                json_file.save(clientes)
                print("Cliente actualizado")
                break
        else:
            print("Cliente no encontrado")
        time.sleep(2)

    def delete(self):
        validar = Valida()
        borrarPantalla()
        gotoxy(2,1);print("Eliminar Cliente")
        gotoxy(2,2);dni = validar.solo_numeros("Error: Solo números", 10, 2)

        json_file = JsonFile(path+'/archivos/clients.json')
        clientes = json_file.read()
        clientes = [c for c in clientes if c['dni'] != dni]
        json_file.save(clientes)
        print("Cliente eliminado si existía")
        time.sleep(2)

    def consult(self):
        borrarPantalla()
        print("Lista de Clientes")
        json_file = JsonFile(path+'/archivos/clients.json')
        clientes = json_file.read()
        for c in clientes:
            print(f"{c['dni']} - {c['nombre']} {c['apellido']}")
        input("Presione una tecla para continuar...")

class CrudProducts(ICrud):
    def create(self):
        validar = Valida()
        borrarPantalla()
        gotoxy(2,1);print("Ingreso de Producto")
        gotoxy(2,2);id = int(validar.solo_numeros("Error: Solo números", 10, 2))
        gotoxy(2,3);descripcion = input("Descripción: ")
        gotoxy(2,4);precio = float(validar.solo_decimales("Error: Solo decimales", 10, 4))
        gotoxy(2,5);stock = int(validar.solo_numeros("Error: Solo números", 10, 5))

        product = Product(id, descripcion, precio, stock)
        json_file = JsonFile(path+'/archivos/products.json')
        productos = json_file.read()
        productos.append(product.getJson())
        json_file.save(productos)
        print("Producto guardado con éxito")
        time.sleep(2)

    def update(self):
        validar = Valida()
        borrarPantalla()
        gotoxy(2,1);print("Actualizar Producto")
        gotoxy(2,2);id = int(validar.solo_numeros("Error: Solo números", 10, 2))

        json_file = JsonFile(path+'/archivos/products.json')
        productos = json_file.read()
        for p in productos:
            if p['id'] == id:
                gotoxy(2,3);descripcion = input("Nueva Descripción: ")
                gotoxy(2,4);precio = float(validar.solo_decimales("Error: Solo decimales", 10, 4))
                gotoxy(2,5);stock = int(validar.solo_numeros("Error: Solo números", 10, 5))
                p['descripcion'] = descripcion
                p['precio'] = precio
                p['stock'] = stock
                json_file.save(productos)
                print("Producto actualizado")
                break
        else:
            print("Producto no encontrado")
        time.sleep(2)

    def delete(self):
        validar = Valida()
        borrarPantalla()
        gotoxy(2,1);print("Eliminar Producto")
        gotoxy(2,2);id = int(validar.solo_numeros("Error: Solo números", 10, 2))

        json_file = JsonFile(path+'/archivos/products.json')
        productos = json_file.read()
        productos = [p for p in productos if p['id'] != id]
        json_file.save(productos)
        print("Producto eliminado si existía")
        time.sleep(2)

    def consult(self):
        borrarPantalla()
        print("Lista de Productos")
        json_file = JsonFile(path+'/archivos/products.json')
        productos = json_file.read()
        for p in productos:
            print(f"{p['id']} - {p['descripcion']} - ${p['precio']} - Stock: {p['stock']}")
        input("Presione una tecla para continuar...")
