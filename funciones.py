import pandas as pd
import matplotlib.pyplot as plt

inventario=[{
  'id':1245,
  'nombre':'Lomo de cerdo',
  'marca':'Carnes del campo',
  'categoria':'carnicos',
  'fecha_ingreso':'31/05/2021',
  'fecha_vencimiento':'17/07/2021',
  'precio':12500,
  'presentacion':'kilo',
  'existencias':120
},{
  'id':1246,
  'nombre':'Costilla de cerdo',
  'marca':'Carnes del campo',
  'categoria':'carnicos',
  'fecha_ingreso':'31/05/2021',
  'fecha_vencimiento':'17/07/2021',
  'precio':11200,
  'presentacion':'kilo',
  'existencias':32
}]

def ingresar_producto():
  id=int(input('Ingrese el id del producto: '))
  nombre=input('Ingrese el nombre del producto: ')
  marca=input('Ingrese la marca del producto: ')
  categoria=input('Ingrese la categoria del producto: ')
  fecha_ingreso=input('Ingrese la fecha de ingreso del producto [DD-MM-AAAA]: ')
  fecha_vencimiento=input('Ingrese la fecha de vencimiento del producto [DD-MM-AAAA]: ')
  precio=float(input('Ingrese el precio del producto: '))
  presentacion=input('Ingrese la presentación del producto: ')
  existencias=float(input('Ingrese las existencias del producto: '))
  producto={'id':id,'nombre':nombre,'marca':marca,'categoria':categoria,'fecha_ingreso':fecha_ingreso,'fecha_vencimiento':fecha_vencimiento,'precio':precio,'presentacion':presentacion,'existencias':existencias}
  for valores in range(len(inventario)):
    if inventario[valores].get('id')==id:
      inventario['existencias']+=existencias
      break
    else:
      inventario.append(producto)

def vender_producto():
  id=int(input('Ingrese el Id del producto: '))
  cantidad_vender=float(input('Ingrese la cantidad a vender del producto: '))
  for valores in range(len(inventario)):
    if inventario[valores].get('id')==id:
      if cantidad_vender<=inventario[valores].get('existencias'):
        inventario[valores]['existencias']-=cantidad_vender
        break
      else:
        print(f'Cuidado apenas tienes {inventario[valores].get("existencias")} del producto')

def mostrar_dataframe():
  df=pd.DataFrame(inventario)
  return df

def graficar_estadisticas():
  dataframe=mostrar_dataframe()
  while True:
        opcion=input('''Ingrese la opcion por la que desea ver la información:
                        0. Salir
                        1. Por Nombre de Producto
                        2. Por Marca de Producto
                        3. Por Categoría
                        
                        ¿Que opción desea conocer? ---- ''')
        if opcion=='0':
            break;
        elif opcion=='1':
            plt.bar(dataframe['nombre'],dataframe['existencias'])
            plt.title('Nombre de producto x Existencias')
            plt.show()
        elif opcion=='2':
            grupo=pd.groupby('marca')['existencias'].sum()
            plt.bar(grupo.index,grupo)
            plt.title('Marca x Existencias')
            plt.show()
        elif opcion=='3':
            grupo=pd.groupby('categoria')['existencias'].sum()
            plt.bar(grupo.index,grupo)
            plt.title('Categoría x Existencias')
            plt.show()
        else:
            print('!!Ingresó un número fuera de las opciones dadas¡¡')


