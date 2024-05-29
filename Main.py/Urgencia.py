from Paciente import Paciente

class Node:
  __slots__ = 'value', 'next'

  def __init__(self, value):
    self.value = value
    self.next = None

  def __str__(self):
    return str(self.value)

class MinHeap:
  def __init__(self, data = None):
    self.data = data
    self.leftchild = None
    self.rightchild = None

  def __str__(self, level=0):
    ret = "  " *level + str(self.data) + "\n"

    if self.leftchild:
      ret += self.leftchild.__str__(level+1)

    if self.rightchild:
      ret += self.rightchild.__str__(level+1)

    return ret
  
  def registrarPaciente(self, data: Paciente):
    node = Node(data)
    
    if self.data == None:
        self.data = node
    elif self.data != None and node.value.numeroPaciente < self.data.value.numeroPaciente:
      if self.leftchild == None:
        self.leftchild = self.data
        self.data = node
      elif self.leftchild != None:
        if self.rightchild == None:
            self.rightchild = self.data
            self.data = node
        elif self.rightchild != None:
            self.rightchild = self.data
            self.data = node
    elif self.data != None and node.value.numeroPaciente > self.data.value.numeroPaciente:
      if self.leftchild == None:
        self.leftchild = node
      elif self.leftchild != None:
        if self.rightchild == None:
            self.rightchild = node
        elif self.rightchild != None:
            self.rightchild = node
    else:
       self.leftchild = node

  def eliminarPaciente(self, numeroPaciente):
     if self.data.value.numeroPaciente == numeroPaciente:
        if self.leftchild.value.triaje < self.rightchild.value.triaje:
          self.data = self.minHeap.leftchild
          self.leftchild = self.rightchild
     elif self.leftchild.value.numeroPaciente == numeroPaciente:
        if self.leftchild.value.triaje > self.minHeap.rightchild.value.triaje:
          self.leftchild = self.rightchild
          self.rightchild = None
     elif self.rightchild.value.numeroPaciente == numeroPaciente:
        self.rightchild = None
            