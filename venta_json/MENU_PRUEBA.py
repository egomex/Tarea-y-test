# from components import Menu, Valida
# from utilities import borrarPantalla, gotoxy
# from utilities import reset_color, red_color, green_color, yellow_color, blue_color, purple_color, cyan_color
# from clsJson import JsonFile
# from company import Company
# from customer import RegularClient
# from sales import Sale
# from product import Product
# from iCrud import ICrud
# import datetime
# import time, os
# from functools import reduce

# path, _ = os.path.split(os.path.abspath(__file__))

# # CRUD de Clientes
# class CrudClients(ICrud):
#     def create(self):
#         borrarPantalla()
#         gotoxy(10, 2); print("Ingreso de Cliente")
#         validar = Valida()
#         gotoxy(10, 4); nombre = input("Nombre: ")
#         gotoxy(10, 5); apellido = input("Apellido: ")
#         gotoxy(10, 6); print("DNI: ") 
#         dni = validar.solo_numeros("Error: Solo numeros", 15, 6)  # El DNI debe ser un número
#         client = RegularClient(nombre, apellido, int(dni))  # Asegurarse de convertir el DNI a int
#         json_file = JsonFile(path + '/archivos/clients.json')
#         clientes = json_file.read()
#         clientes.append(client.getJson())
#         json_file.save(clientes)
#         gotoxy(10, 8); print("Cliente guardado correctamente")
#         input("Presione una tecla para continuar...")

#     def update(self):
#         borrarPantalla()
#         gotoxy(10, 2); print("Actualizar Cliente")
#         validar = Valida()
#         gotoxy(10, 4); print("DNI: ") 
#         dni = validar.solo_numeros("Error: Solo numeros", 15, 4)
#         json_file = JsonFile(path + '/archivos/clients.json')
#         clientes = json_file.read()
#         for cli in clientes:
#             if cli['dni'] == dni:
#                 gotoxy(10, 5); nuevo_nombre = input("Nuevo Nombre: ")
#                 gotoxy(10, 6); nuevo_apellido = input("Nuevo Apellido: ")
#                 cli['nombre'] = nuevo_nombre
#                 cli['apellido'] = nuevo_apellido
#                 json_file.save(clientes)
#                 gotoxy(10, 8); print("Cliente actualizado correctamente")
#                 input("Presione una tecla para continuar...")
#                 return
#         gotoxy(10, 8); print("Cliente no encontrado")
#         input("Presione una tecla para continuar...")

#     def delete(self):
#         borrarPantalla()
#         gotoxy(10, 2); print("Eliminar Cliente")
#         validar = Valida()
#         gotoxy(10, 4); print("DNI: ")  
#         dni = validar.solo_numeros("Error: Solo numeros", 15, 4)
#         json_file = JsonFile(path + '/archivos/clients.json')
#         clientes = json_file.read()
        
#         # Filtrar clientes por el DNI que no coincidan con el DNI ingresado
#         nuevos_clientes = [cli for cli in clientes if cli['dni'] != dni]
        
#         # Verificar si se encontró el cliente
#         if len(nuevos_clientes) == len(clientes):
#             gotoxy(10, 6); print("Cliente no encontrado.")
#         else:
#             json_file.save(nuevos_clientes)
#             gotoxy(10, 6); print("Cliente eliminado correctamente.")
        
#         input("Presione una tecla para continuar...")

#     def consult(self):
#         borrarPantalla()
#         gotoxy(10, 2); print("Consulta de Clientes")
#         json_file = JsonFile(path + '/archivos/clients.json')
#         clientes = json_file.read()
#         for cli in clientes:
#             print(cli)
#         input("Presione una tecla para continuar...")

# # CRUD de Productos
# class CrudProducts(ICrud):
#     def create(self):
#         borrarPantalla()
#         gotoxy(10, 2); print("Ingreso de Producto")
#         validar = Valida()
#         gotoxy(10, 4); print("ID: ")  
#         id = int(validar.solo_numeros("Error: Solo numeros", 15, 4))  # Asegura que el ID sea un número entero
#         gotoxy(10, 5); descrip = input("Descripcion: ")
        
#         # Solicita el precio y verifica que sea un número válido
#         gotoxy(7, 6)
#         print("Precio: ")
#         precio = float(validar.solo_numeros("Error: Solo números", 15, 6))  # Asegura que el precio sea float
        
#         # Solicita el stock y verifica que sea un número válido
#         gotoxy(7, 7)
#         print("Stock: ")
#         stock = int(validar.solo_numeros("Error: Solo números", 15, 7))  # Asegura que el stock sea un número entero
        
#         producto = Product(id, descrip, precio, stock)
#         json_file = JsonFile(path + '/archivos/products.json')
#         productos = json_file.read()
#         productos.append(producto.getJson())
#         json_file.save(productos)
#         gotoxy(10, 9); print("Producto guardado correctamente")
#         input("Presione una tecla para continuar...")

#     def update(self):
#         borrarPantalla()
#         gotoxy(10, 2); print("Actualizar Producto")
#         validar = Valida()
#         gotoxy(10, 4); print("ID: ")
#         gotoxy(10, 4); id = int(validar.solo_numeros("Error: Solo numeros", 15, 4))  # Convertir el ID a entero
#         json_file = JsonFile(path + '/archivos/products.json')
#         productos = json_file.read()
#         for prod in productos:
#             if prod['id'] == id:
#                 gotoxy(10, 5); descrip = input("Nueva Descripcion: ")
#                 gotoxy(7, 6)
#                 print("Precio: ")
#                 precio = float(validar.solo_numeros("Error: Solo números", 15, 6))  # Convertir a float
#                 gotoxy(7, 7)
#                 print("Stock: ")
#                 stock = int(validar.solo_numeros("Error: Solo números", 15, 7))  # Convertir a entero
#                 prod['descripcion'] = descrip
#                 prod['precio'] = precio
#                 prod['stock'] = stock
#                 json_file.save(productos)
#                 gotoxy(10, 9); print("Producto actualizado correctamente")
#                 input("Presione una tecla para continuar...")
#                 return
#         gotoxy(10, 9); print("Producto no encontrado")
#         input("Presione una tecla para continuar...")

#     def delete(self):
#         borrarPantalla()
#         gotoxy(10, 2); print("Eliminar Producto")
#         validar = Valida()
#         gotoxy(10, 4); print("ID: ")  
#         gotoxy(10, 4); id = int(validar.solo_numeros("Error: Solo numeros", 15, 4))  # Convertir el ID a entero
#         json_file = JsonFile(path + '/archivos/products.json')
#         productos = json_file.read()
        
#         # Filtrar productos por ID que no coincidan con el ID ingresado
#         nuevos_productos = [prod for prod in productos if prod['id'] != id]
        
#         # Verificar si se encontró el producto
#         if len(nuevos_productos) == len(productos):
#             gotoxy(10, 6); print("Producto no encontrado.")
#         else:
#             json_file.save(nuevos_productos)
#             gotoxy(10, 6); print("Producto eliminado correctamente.")
        
#         input("Presione una tecla para continuar...")

#     def consult(self):
#         borrarPantalla()
#         gotoxy(10, 2); print("Consulta de Productos")
#         json_file = JsonFile(path + '/archivos/products.json')
#         productos = json_file.read()
#         for prod in productos:
#             print(prod)
#         input("Presione una tecla para continuar...")

# # Menú Principal con CRUDs Conectados
# opc = ''
# while opc != '4':  
#     borrarPantalla()      
#     menu_main = Menu("Menu Facturacion", ["1) Clientes", "2) Productos", "3) Ventas", "4) Salir"], 20, 10)
#     opc = menu_main.menu()

#     if opc == "1":
#         cliente_crud = CrudClients()
#         opc1 = ''
#         while opc1 != '5':
#             borrarPantalla()    
#             menu_clients = Menu("Menu Clientes", ["1) Ingresar", "2) Actualizar", "3) Eliminar", "4) Consultar", "5) Salir"], 20, 10)
#             opc1 = menu_clients.menu()
#             if opc1 == "1": cliente_crud.create()
#             elif opc1 == "2": cliente_crud.update()
#             elif opc1 == "3": cliente_crud.delete()
#             elif opc1 == "4": cliente_crud.consult()

#     elif opc == "2":
#         producto_crud = CrudProducts()
#         opc2 = ''
#         while opc2 != '5':
#             borrarPantalla()    
#             menu_products = Menu("Menu Productos", ["1) Ingresar", "2) Actualizar", "3) Eliminar", "4) Consultar", "5) Salir"], 20, 10)
#             opc2 = menu_products.menu()
#             if opc2 == "1": producto_crud.create()
#             elif opc2 == "2": producto_crud.update()
#             elif opc2 == "3": producto_crud.delete()
#             elif opc2 == "4": producto_crud.consult()

#     elif opc == "3":
#         sales = CrudSales()
#         opc3 = ''
#         while opc3 != '5':
#             borrarPantalla()
#             menu_sales = Menu("Menu Ventas", ["1) Registro Venta", "2) Consultar", "3) Modificar", "4) Eliminar", "5) Salir"], 20, 10)
#             opc3 = menu_sales.menu()
#             if opc3 == "1":
#                 sales.create()
#             elif opc3 == "2":
#                 sales.consult() 
# borrarPantalla()
# input("Presione una tecla para salir...")



#***********************************************************************************************

# from components import Menu, Valida
# from utilities import borrarPantalla, gotoxy
# from utilities import reset_color, red_color, green_color, yellow_color, blue_color, purple_color, cyan_color
# from clsJson import JsonFile
# from company import Company
# from customer import RegularClient
# from sales import Sale
# from product import Product
# from iCrud import ICrud
# import datetime
# import time, os
# from functools import reduce

# path, _ = os.path.split(os.path.abspath(__file__))

# # CRUD de Clientes
# class CrudClients(ICrud):
#     def create(self):
#         borrarPantalla()
#         gotoxy(10, 2); print("Ingreso de Cliente")
#         validar = Valida()
#         gotoxy(10, 4); nombre = input("Nombre: ")
#         gotoxy(10, 5); apellido = input("Apellido: ")
#         gotoxy(10, 6); print("DNI: ") 
#         dni = validar.solo_numeros("Error: Solo numeros", 15, 6)  # El DNI debe ser un número
#         client = RegularClient(nombre, apellido, int(dni))  # Asegurarse de convertir el DNI a int
#         json_file = JsonFile(path + '/archivos/clients.json')
#         clientes = json_file.read()
#         clientes.append(client.getJson())
#         json_file.save(clientes)
#         gotoxy(10, 8); print("Cliente guardado correctamente")
#         input("Presione una tecla para continuar...")

#     def update(self):
#         borrarPantalla()
#         gotoxy(10, 2); print("Actualizar Cliente")
#         validar = Valida()
#         gotoxy(10, 4); print("DNI: ") 
#         dni = validar.solo_numeros("Error: Solo numeros", 15, 4)
#         json_file = JsonFile(path + '/archivos/clients.json')
#         clientes = json_file.read()
#         for cli in clientes:
#             if cli['dni'] == dni:
#                 gotoxy(10, 5); nuevo_nombre = input("Nuevo Nombre: ")
#                 gotoxy(10, 6); nuevo_apellido = input("Nuevo Apellido: ")
#                 cli['nombre'] = nuevo_nombre
#                 cli['apellido'] = nuevo_apellido
#                 json_file.save(clientes)
#                 gotoxy(10, 8); print("Cliente actualizado correctamente")
#                 input("Presione una tecla para continuar...")
#                 return
#         gotoxy(10, 8); print("Cliente no encontrado")
#         input("Presione una tecla para continuar...")

#     def delete(self):
#         borrarPantalla()
#         gotoxy(10, 2); print("Eliminar Cliente")
#         validar = Valida()
#         gotoxy(10, 4); print("DNI: ")  
#         dni = validar.solo_numeros("Error: Solo numeros", 15, 4)
#         json_file = JsonFile(path + '/archivos/clients.json')
#         clientes = json_file.read()
        
#         # Filtrar clientes por el DNI que no coincidan con el DNI ingresado
#         nuevos_clientes = [cli for cli in clientes if cli['dni'] != dni]
        
#         # Verificar si se encontró el cliente
#         if len(nuevos_clientes) == len(clientes):
#             gotoxy(10, 6); print("Cliente no encontrado.")
#         else:
#             json_file.save(nuevos_clientes)
#             gotoxy(10, 6); print("Cliente eliminado correctamente.")
        
#         input("Presione una tecla para continuar...")

#     def consult(self):
#         borrarPantalla()
#         gotoxy(10, 2); print("Consulta de Clientes")
#         json_file = JsonFile(path + '/archivos/clients.json')
#         clientes = json_file.read()
#         for cli in clientes:
#             print(cli)
#         input("Presione una tecla para continuar...")

# # CRUD de Productos
# class CrudProducts(ICrud):
#     def create(self):
#         borrarPantalla()
#         gotoxy(10, 2); print("Ingreso de Producto")
#         validar = Valida()
#         gotoxy(10, 4); print("ID: ")  
#         id = int(validar.solo_numeros("Error: Solo numeros", 15, 4))  # Asegura que el ID sea un número entero
#         gotoxy(10, 5); descrip = input("Descripcion: ")
        
#         # Solicita el precio y verifica que sea un número válido
#         gotoxy(7, 6)
#         print("Precio: ")
#         precio = float(validar.solo_numeros("Error: Solo números", 15, 6))  # Asegura que el precio sea float
        
#         # Solicita el stock y verifica que sea un número válido
#         gotoxy(7, 7)
#         print("Stock: ")
#         stock = int(validar.solo_numeros("Error: Solo números", 15, 7))  # Asegura que el stock sea un número entero
        
#         producto = Product(id, descrip, precio, stock)
#         json_file = JsonFile(path + '/archivos/products.json')
#         productos = json_file.read()
#         productos.append(producto.getJson())
#         json_file.save(productos)
#         gotoxy(10, 9); print("Producto guardado correctamente")
#         input("Presione una tecla para continuar...")

#     def update(self):
#         borrarPantalla()
#         gotoxy(10, 2); print("Actualizar Producto")
#         validar = Valida()
#         gotoxy(10, 4); print("ID: ")
#         gotoxy(10, 4); id = int(validar.solo_numeros("Error: Solo numeros", 15, 4))  # Convertir el ID a entero
#         json_file = JsonFile(path + '/archivos/products.json')
#         productos = json_file.read()
#         for prod in productos:
#             if prod['id'] == id:
#                 gotoxy(10, 5); descrip = input("Nueva Descripcion: ")
#                 gotoxy(7, 6)
#                 print("Precio: ")
#                 precio = float(validar.solo_numeros("Error: Solo números", 15, 6))  # Convertir a float
#                 gotoxy(7, 7)
#                 print("Stock: ")
#                 stock = int(validar.solo_numeros("Error: Solo números", 15, 7))  # Convertir a entero
#                 prod['descripcion'] = descrip
#                 prod['precio'] = precio
#                 prod['stock'] = stock
#                 json_file.save(productos)
#                 gotoxy(10, 9); print("Producto actualizado correctamente")
#                 input("Presione una tecla para continuar...")
#                 return
#         gotoxy(10, 9); print("Producto no encontrado")
#         input("Presione una tecla para continuar...")

#     def delete(self):
#         borrarPantalla()
#         gotoxy(10, 2); print("Eliminar Producto")
#         validar = Valida()
#         gotoxy(10, 4); print("ID: ")  
#         gotoxy(10, 4); id = int(validar.solo_numeros("Error: Solo numeros", 15, 4))  # Convertir el ID a entero
#         json_file = JsonFile(path + '/archivos/products.json')
#         productos = json_file.read()
        
#         # Filtrar productos por ID que no coincidan con el ID ingresado
#         nuevos_productos = [prod for prod in productos if prod['id'] != id]
        
#         # Verificar si se encontró el producto
#         if len(nuevos_productos) == len(productos):
#             gotoxy(10, 6); print("Producto no encontrado.")
#         else:
#             json_file.save(nuevos_productos)
#             gotoxy(10, 6); print("Producto eliminado correctamente.")
        
#         input("Presione una tecla para continuar...")

#     def consult(self):
#         borrarPantalla()
#         gotoxy(10, 2); print("Consulta de Productos")
#         json_file = JsonFile(path + '/archivos/products.json')
#         productos = json_file.read()
#         for prod in productos:
#             print(prod)
#         input("Presione una tecla para continuar...")

# # CRUD de Ventas
# class CrudSales(ICrud):
#     def create(self):
#         borrarPantalla()
#         gotoxy(10, 2); print("Registro de Venta")
#         validar = Valida()

#         gotoxy(10, 4); print("DNI Cliente: ", end="")
#         cliente_dni = validar.solo_numeros("Error: Solo numeros", 26, 4)

#         gotoxy(10, 5); print("ID Producto: ", end="")
#         producto_id = int(validar.solo_numeros("Error: Solo numeros", 26, 5))

#         gotoxy(10, 6); print("Cantidad: ", end="")
#         cantidad = int(validar.solo_numeros("Error: Solo numeros", 26, 6))

#         cliente_json_file = JsonFile(path + '/archivos/clients.json')
#         clientes = cliente_json_file.read()
#         producto_json_file = JsonFile(path + '/archivos/products.json')
#         productos = producto_json_file.read()

#         cliente = next((cli for cli in clientes if cli['dni'] == cliente_dni), None)
#         producto = next((prod for prod in productos if prod['id'] == producto_id), None)

#         if cliente and producto:
#             venta = Sale(cliente, producto, cantidad)
#             ventas_json_file = JsonFile(path + '/archivos/sales.json')
#             ventas = ventas_json_file.read()
#             ventas.append(venta.getJson())
#             ventas_json_file.save(ventas)
#             gotoxy(10, 8); print("Venta registrada correctamente")
#         else:
#             gotoxy(10, 8); print("Cliente o producto no encontrado")

#         input("Presione una tecla para continuar...")

#     def consult(self):
#         borrarPantalla()
#         gotoxy(10, 2); print("Consultar Ventas")
#         ventas_json_file = JsonFile(path + '/archivos/sales.json')
#         ventas = ventas_json_file.read()
#         for venta in ventas:
#             print(venta)
#         input("Presione una tecla para continuar...")

#     def update(self):
#         borrarPantalla()
#         gotoxy(10, 2); print("Modificar Venta")
#         validar = Valida()

#         gotoxy(10, 4); print("ID Venta: ", end="")
#         venta_id = int(validar.solo_numeros("Error: Solo numeros", 21, 4))
#         ventas_json_file = JsonFile(path + '/archivos/sales.json')
#         ventas = ventas_json_file.read()
#         venta = next((v for v in ventas if v['id'] == venta_id), None)

#         if venta:
#             gotoxy(10, 5); print(f"Venta encontrada: {venta}")
#             gotoxy(10, 6); print("Nueva cantidad: ", end="")
#             cantidad = int(validar.solo_numeros("Error: Solo numeros", 27, 6))
#             venta['cantidad'] = cantidad
#             ventas_json_file.save(ventas)
#             gotoxy(10, 8); print("Venta modificada correctamente")
#         else:
#             gotoxy(10, 8); print("Venta no encontrada")

#         input("Presione una tecla para continuar...")

#     def delete(self):
#         borrarPantalla()
#         gotoxy(10, 2); print("Eliminar Venta")
#         validar = Valida()

#         gotoxy(10, 4); print("ID Venta: ", end="")
#         venta_id = int(validar.solo_numeros("Error: Solo numeros", 21, 4))
#         ventas_json_file = JsonFile(path + '/archivos/sales.json')
#         ventas = ventas_json_file.read()
#         nuevas_ventas = [v for v in ventas if v['id'] != venta_id]

#         if len(nuevas_ventas) == len(ventas):
#             gotoxy(10, 6); print("Venta no encontrada.")
#         else:
#             ventas_json_file.save(nuevas_ventas)
#             gotoxy(10, 6); print("Venta eliminada correctamente.")

#         input("Presione una tecla para continuar...")

# # Menú Principal con CRUDs Conectados
# opc = ''
# while opc != '4':  
#     borrarPantalla()      
#     menu_main = Menu("Menu Facturacion", ["1) Clientes", "2) Productos", "3) Ventas", "4) Salir"], 20, 10)
#     opc = menu_main.menu()

#     if opc == "1":
#         cliente_crud = CrudClients()
#         opc1 = ''
#         while opc1 != '5':
#             borrarPantalla()    
#             menu_clients = Menu("Menu Clientes", ["1) Ingresar", "2) Actualizar", "3) Eliminar", "4) Consultar", "5) Salir"], 20, 10)
#             opc1 = menu_clients.menu()
#             if opc1 == "1": cliente_crud.create()
#             elif opc1 == "2": cliente_crud.update()
#             elif opc1 == "3": cliente_crud.delete()
#             elif opc1 == "4": cliente_crud.consult()

#     elif opc == "2":
#         producto_crud = CrudProducts()
#         opc2 = ''
#         while opc2 != '5':
#             borrarPantalla()    
#             menu_products = Menu("Menu Productos", ["1) Ingresar", "2) Actualizar", "3) Eliminar", "4) Consultar", "5) Salir"], 20, 10)
#             opc2 = menu_products.menu()
#             if opc2 == "1": producto_crud.create()
#             elif opc2 == "2": producto_crud.update()
#             elif opc2 == "3": producto_crud.delete()
#             elif opc2 == "4": producto_crud.consult()

#     elif opc == "3":
#         sales = CrudSales()
#         opc3 = ''
#         while opc3 != '5':
#             borrarPantalla()    
#             menu_sales = Menu("Menu Ventas", ["1) Registro Venta", "2) Consultar", "3) Modificar", "4) Eliminar", "5) Salir"], 20, 10)
#             opc3 = menu_sales.menu()
#             if opc3 == "1": sales.create()
#             elif opc3 == "2": sales.consult()
#             elif opc3 == "3": sales.update()
#             elif opc3 == "4": sales.delete()

# borrarPantalla()
# input("Presione una tecla para salir...")

#********************************************************************************************

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
