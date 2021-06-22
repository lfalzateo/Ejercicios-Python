"""
Fecha:18 Jun-2021
Nombre:Luis Felipe Alzate Osorio
"""

import funciones as f

espacios=60
print('*'*espacios)
print('Bienvenido al Reto de la Semana 7'.center(espacios))
print('*'*espacios)
'''
Es la primera parte del programa, donde se tendrán diferentes funciones como:
1. Ingresar Producto
2. Vender Producto
2. Imprimir el dataframe de el inventario total
3. Ver estadísticas en gráficos
'''

while True:
  opcion=input('''El menú del reto tiene las siguientes opciones, escoja la deseada:
  1. Ingresar Producto
  2. Vender Producto
  3. Imprimir DataFrame del inventario
  4. Ver Estadísticas Gráficas
  0. Salir
  
  ¿Qué opción desea? ----- ''').strip()[0]

  if opcion=='0':
    break;
  elif opcion=='1':
    f.ingresar_producto()
  elif opcion=='2':
    f.vender_producto()
  elif opcion=='3':
    print(f.mostrar_dataframe())
  elif opcion=='4':
    f.graficar_estadisticas()
  else:
    print('!!Opción incorrecta¡¡')