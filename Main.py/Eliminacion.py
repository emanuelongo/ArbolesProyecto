from Urgencia import MinHeap

class Eliminacion:
    def __init__(self, minHeap: MinHeap):
        self.minHeap = minHeap
    
    def eliminarPaciente(self):
        numeroPaciente = int(input("Ingresa el número del paciente a eliminar: "))

        if self.minHeap.data.value.numeroPaciente == numeroPaciente:
            self.minHeap.eliminarPaciente(numeroPaciente)
            print("\nPaciente eliminado\n")
        elif self.minHeap.leftchild != None and self.minHeap.leftchild.value.numeroPaciente == numeroPaciente:
            self.minHeap.eliminarPaciente(numeroPaciente)
            print("\nPaciente eliminado\n")
        elif self.minHeap.rightchild != None and self.minHeap.rightchild.value.numeroPaciente == numeroPaciente:
            self.minHeap.eliminarPaciente(numeroPaciente)
            print("\nPaciente eliminado\n")
        else:
            print("\nNo hay un paciente con ese número de paciente\n")
