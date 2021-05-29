class Menu:
    __switcher:None

    def __init__(self):
        self.__switcher={1:self.opcion1,
                        2: self.opcion2,
                        3: self.opcion3,
                        4: self.opcion4,
                        0: self.salir}

    def getSwitcher(self):
        return self.__switcher

    def opcion(self,opcion,coleccion):
        funcion=self.__switcher.get(opcion,lambda:print("\nOpcion no valida."))
        funcion(coleccion)

    #---------------------------------------------------------OPCION 1
    def opcion1(self,coleccion):
        dni=int(input("\nIngrese DNI: "))
        cantHoras=int(input("\nIngrese cantidad de horas: "))
        coleccion.registrarHoras(dni,cantHoras)

    #---------------------------------------------------------OPCION 2
    def opcion2(self,coleccion):
        tarea=input("\nIngrese tarea: ")
        tarea=tarea.lower()
        if tarea not in ['carpinteria','plomeria','electricidad']:
            print("\nTarea no encontrada.\nLas tareas son: carpinteria, plomeria, electricidad")
        else:
            coleccion.totalTarea(tarea)

    #---------------------------------------------------------OPCION 3
    def opcion3(self,coleccion):
        coleccion.listarAyuda()

    #---------------------------------------------------------OPCION 4
    def opcion4(self,coleccion):
        coleccion.listarEmpleados()

    #---------------------------------------------------------SALIR
    def salir(self,coleccion):
        print("\nChau :)")