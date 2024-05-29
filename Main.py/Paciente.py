class Paciente:
    def __init__(self, numeroPaciente: str, genero: str, nombre: str, edad: int, triaje: int):
        self.numeroPaciente = numeroPaciente
        self.genero = genero
        self.nombre = nombre
        self.edad = edad
        self.triaje = triaje