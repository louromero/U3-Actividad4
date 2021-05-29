from typing import Collection
from Menu import Menu
from Coleccion import Coleccion

if __name__=='__main__':
    menu=Menu()
    salir=False
    dimension=int(input("\nIngrese dimension del arreglo: "))
    coleccion=Coleccion(dimension)
    while not salir:
        print("\n-------------------MENU------------------")
        print("1. Registrar horas.")
        print("2. Consultar total de tareas.")
        print("3. Ayuda.")
        print("4. Calcular sueldo.")
        print("0. Salir.")
        print("--------------------------------------------\n")
        opcion=int(input("Ingrese opcion: "))
        menu.opcion(opcion,coleccion)
        salir=opcion==0