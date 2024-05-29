from Urgencia import MinHeap

class Consulta:
    def __init__(self, minHeap: MinHeap):
        self.minHeap = minHeap

    def consultarPacienteProximo(self):
        print(f"Paciente próximo a atender tiene el nombre de {self.minHeap.data.value.nombre}, el identificor {self.minHeap.data.value.numeroPaciente} y el triaje {self.minHeap.data.value.triaje}")
        

    def consultarPacientesEsperandoGeneral(self):
        print(f"Paciente {self.minHeap.data.value.nombre} esperando")
        if self.minHeap.leftchild != None:
            print(f"Paciente {self.minHeap.leftchild.value.nombre} esperando")
        else:
            pass
        if self.minHeap.rightchild != None:
            print(f"Paciente {self.minHeap.rightchild.value.nombre} esperando")
        else:
            pass

    def consultarPacientesTriaje(self):
        print(f"Paciente {self.minHeap.data.value.nombre} esperando")
        if self.minHeap.leftchild != None:
            print(f"Paciente {self.minHeap.leftchild.value.nombre} esperando")
        else:
            pass
        if self.minHeap.rightchild != None:
            print(f"Paciente {self.minHeap.rightchild.value.nombre} esperando")
        else:
            pass