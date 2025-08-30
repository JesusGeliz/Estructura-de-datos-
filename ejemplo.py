class Persona:
    altura: float
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self) -> str:
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad}"
    
    @staticmethod
    def esMayor():
        return None
    
    def __str__(self) -> str:
        return f"Persona (nombre = {self.Persona}, edad = {self.edad})"
    
class Estudiante(Persona):
    __promedio: float
    def _init_(self,nombre: str, edad: int, carrera: str):
        super().__init__(nombre,edad)
        self.carrera = carrera
        
    def estudiar(self) -> str:
        return f"{self.nombre} está estudiando {self.carrera}."
        
    def __str__(self) -> str: 
        return f"Estudinate(nombre={self.nombre}, edad = {self.edad}, carrera = {self.carrera}.)"

    def getPromedio(self) -> float:
        return self.__promedio 
    
    def setPromedio(self, promedio: float) -> None: 
        self.__promedio = promedio 
    
juan = Persona("Juan", 30)
maria = Estudiante("Maria", 22, "Ingenieria")

print(juan.saludar())
print(maria.saludar())
print(maria.estudiar())
juan.altura = 1.75
print(juan)
print(maria)
