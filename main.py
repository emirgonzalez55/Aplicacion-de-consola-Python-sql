import sys
from clases import Torneo, Participantes

class Menu:
    def __init__(self):
        self.clases = Torneo()
        self.elecciones = {
                "1" : self.mostrar_participantes,
                "2" : self.participantes,
                "3" : self.podio,
                "4" : self.promedio_disparos,
                "5" : self.cantidad_participantes,
                "6" : self.participntes_ordenados_por_edad, 
                "7" : self.quit
                } 

    def mostrar_menu(self):
        print("""
Menu Torneo

1 Mostrar participantes
2 Agregar participantes
3 Mostrar el top 3
4 Promedio de todos los diparos
5 Catidad de participantes
6 Participante ordenados por edad 
7 Salir
""")

    def run(self):
        while True:
            self.mostrar_menu()
            eleccion = input("Escribe una opción: ")
            accion = self.elecciones.get(eleccion)
            if accion:
                accion()
            else:
                print("{0} no es una elección válida".format(eleccion))

    

    def participantes(self):
        self.clases.participantes()
         

    def mostrar_participantes(self):  
    	self.clases.mostrar_participantes()

    def promedio_disparos(self):  
    	self.clases.promedio_disparos()	
    
    def cantidad_participantes(self):  
    	self.clases.cantidad_participantes()

    def podio(self):  
    	self.clases.podio()	

    def participntes_ordenados_por_edad(self):
    	self.clases.participntes_ordenados_por_edad()	
    		  
                

    def quit(self):
        print("Aplicacion cerrada.")
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()