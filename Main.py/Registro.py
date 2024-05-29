from Paciente import Paciente
from Urgencia import MinHeap

class Registro:
    def __init__(self, minHeap: MinHeap):
        self.minHeap = minHeap

    def registrarPaciente(self):
        numeroPaciente: str = input("Ingresa el número del paciente: ")
        genero: str = input("Ingresa el género del paciente: ")
        nombre: str = input("Ingresa el nombre del paciente: ")
        edad: int = int(input("Ingresa la edad del paciente: "))
        triaje: int = int(input("Ingresa el triaje del paciente: "))

        paciente = Paciente(numeroPaciente, genero, nombre, edad, triaje)

        self.minHeap.registrarPaciente(paciente)

        print("\n===================== Registro exitoso =====================\n")