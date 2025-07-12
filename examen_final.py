productos = {
   '8475HD': ['HP',15.6,'8 GB','DD', '1T','intel core i5', 'Nvidia GtTX1050'],
'2175HD': ['lenovo',14 ,'4 GB','SSD','512 GB','intel core i5 ', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14,'16 GB','SSD','256GB','Intel core I7','Nvidia RTX2080TI']
}

stock ={'8475HD':[38799,10],'217HD':[327990,4],'jJfFHD':[424990,1],
'fgdxFHD':[664990,21],'123FHD':[290890,32],'342FHD':[444990,7],
'GF75HD':[749990,2], 'UWU131HD':[349990,1],'FS1230HD':[249990,0],
}

def menu ():
 while True:
    print('\n...menu...')
    print('1. Stock marca ')
    print('2. Buscar por precio ') 
    print('3. Actualizar precio')   
    print('4. Salir')

    min_precio = 0
    max_precio = 0
    marca = 0

def stock_marca(marca):
    total = 0
for codigo, datos in productos.items():
    if datos[1] == stock:
       total+= stock.get(codigo,[0,0])[1]
    print(f"cantidad total de stock disponible por marca{marca}:{total}")

def buscar_por_precio(min_precio,max_precio):   
   print(f"modelos con precio entrte {min_precio}y {max_precio}:")

for codigo,precio,in stock.items():
   if min_precio <= precio <= max_precio:
      print(f"{codigo}: $ {precio}")

def actualizar_precio(modelo):
   if codigo not in stock:
      print("codigo no encontrado.")
      return
print("¿que desea actualizar?")
print("1.precio.")
print("2. cantida.")
opcion = input("seleccione una opcion: ")
if opcion == "1":
   nuevo_precio = int(input("ingrerse nuevo precio: "))

stock[codigo] [0] = nuevo_precio
print("precio actualizado.")
elif opcion == "2":

nueva_cantidad = int(input("ingrese nueva cantidad:"))
stock[codigo][1] = nueva_cantidad
print("cantidad actualizada.")

else:
print("opcion invalida!..")

opcion = input("seleccione una opcion")
if opcion == "1":
   stock_marca = int(input("ingrese el stock marca"))
 
elif opcion == "2":
  min_precio = int(input("precio minimo: "))
  max_precio = int(input("precio maximo: "))

elif opcion == "3":
   
   actualizar_precio = int(input("actualizar precio:"))
   print("saliendo del programa.")

   break:
   print("opcion invalida intente otra vez")

























               












































































































































































