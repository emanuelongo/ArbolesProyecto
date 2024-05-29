from Urgencia import MinHeap

class Atencion:
    def __init__(self, minHeap: MinHeap):
        self.minHeap = minHeap
    
    def atenderPaciente(self):
        if self.minHeap.leftchild == None:
            self.minHeap.data == None
            print("\nPaciente atendido\n")
        elif self.minHeap.leftchild != None and self.minHeap.rightchild == None:
            self.minHeap.data = self.minHeap.leftchild
            print("\nPaciente atendido\n")
        elif self.minHeap.leftchild != None and self.minHeap.rightchild != None:
            if self.minHeap.leftchild.value.triaje < self.minHeap.rightchild.value.triaje:
                self.minHeap.data = self.minHeap.leftchild
                self.minHeap.leftchild = self.minHeap.rightchild
                print("\nPaciente atendido\n")
            elif self.minHeap.leftchild.value.triaje > self.minHeap.rightchild.value.triaje:
                self.minHeap.data = self.minHeap.rightchild
                self.minHeap.rightchild = None
                print("\nPaciente atendido\n")
            else:
                self.minHeap.data = self.minHeap.rightchild
                self.minHeap.rightchild = None
                