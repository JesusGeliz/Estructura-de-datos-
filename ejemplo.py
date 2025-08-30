class persona:
    def _init_(self, nombre: str, edad,: int):
        self.nombre = nombre
        self.edad = edad
    
    def saludar (self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad}"
    
    @staticmethod
    def esMayor():
        return self.edad >= 18