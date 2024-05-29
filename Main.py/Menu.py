from Urgencia import MinHeap
from Registro import Registro
from Consulta import Consulta
from Atencion import Atencion
from Eliminacion import Eliminacion

class Menu:
    def __init__(self):
        self.minHeap = MinHeap()
        self.mostrarMenu()
        
    def mostrarMenu(self):
        print("\n====================================================")
        print("BIENVENIDO AL MENÚ DE LA SALA DE URGENCIAS")
        print("====================================================\n")
        
        if self.minHeap.data == None:
            self.mostrarOpcionesArbolVacio()
        elif self.minHeap.data != None:
            self.mostrarOpcionesArbolIniciado()

        self.mostrarMenu()

    def mostrarOpcionesArbolVacio(self):    
        print("1. Registrar un paciente.")
        seleccionarOpcion: int = int(input("\nIngresa tu opción: "))
    
        if seleccionarOpcion == 1:
            self.opcionSeleccionada1()
        else:
            print("\nIngresa una opción válida.\n")
            self.mostrarOpcionesArbolVacio()
    
    def mostrarOpcionesArbolIniciado(self):
        print("1. Registrar un paciente.")
        print("2. Consultar próximo paciente a atender.")
        print("3. Consultar pacientes en espera en general.")
        print("4. Consultar apcientes en espera por triaje.")
        print("5. Atender próximo paciente.")
        print("6. Eliminar paciente.")
        
        seleccionarOpcion: int = int(input("\nIngresa tu opción: "))

        if seleccionarOpcion == 1:
            self.opcionSeleccionada1()
        elif seleccionarOpcion == 2:
            self.opcionSeleccionada2()
        elif seleccionarOpcion == 3:
            self.opcionSeleccionada3()
        elif seleccionarOpcion == 4:
            self.opcionSeleccionada4()
        elif seleccionarOpcion == 5:
            self.opcionSeleccionada5()
        elif seleccionarOpcion == 6:
            self.opcionSeleccionada6()
        else:
            print("\nIngresa una opción válida\n")
            self.mostrarOpcionesArbolIniciado()

    def opcionSeleccionada1(self):
        print("\n================= Registrar paciente =================")
        registroPaciente = Registro(self.minHeap)
        registroPaciente.registrarPaciente()

    def opcionSeleccionada2(self):
        print("\n================= Consultar próximo paciente a atender =================")
        consulta = Consulta(self.minHeap)
        consulta.consultarPacienteProximo()
    
    def opcionSeleccionada3(self):
        print("\n================= Consultar pacientes en espera en general =================")
        consulta = Consulta(self.minHeap)
        consulta.consultarPacientesEsperandoGeneral()

    def opcionSeleccionada4(self):
        print("\n================= Consultar pacientes en espera por triaje =================")
        consulta = Consulta(self.minHeap)
        consulta.consultarPacientesTriaje()

    def opcionSeleccionada5(self):
        print("\n================= Atender el próximo paciente =================")
        atencion = Atencion(self.minHeap)
        atencion.atenderPaciente()

    def opcionSeleccionada6(self):
        print("\n================= Eliminar un paciente =================")
        eliminacion = Eliminacion(self.minHeap)
        eliminacion.eliminarPaciente()

menu = Menu()
menu