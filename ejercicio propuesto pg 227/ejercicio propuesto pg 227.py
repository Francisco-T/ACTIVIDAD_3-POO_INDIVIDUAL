from abc import ABC, abstractmethod

class Mascota(ABC):
    def __init__(self, nombre: str, edad: int, color: str):
        self.nombre = nombre
        self.edad = edad
        self.color = color

    @abstractmethod
    def imprimir(self):
        pass

class Perro(Mascota):
    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool):
        super().__init__(nombre, edad, color)
        self.peso = peso
        self.muerde = muerde

    @staticmethod
    def sonido():
        print("Los perros ladran")

    def imprimir(self):
        raza = type(self).__name__
        mordida = "sí" if self.muerde else "no"
        print(f"Perro ({raza}): {self.nombre}, edad {self.edad}, color {self.color}, peso {self.peso} kg, muerde: {mordida}")

class PerroPequeno(Perro):
    pass

class PerroMediano(Perro):
    pass

class PerroGrande(Perro):
    pass

class Caniche(PerroPequeno):
    pass

class YorkshireTerrier(PerroPequeno):
    pass

class Schnauzer(PerroPequeno):
    pass

class Chihuahua(PerroPequeno):
    pass

class Collie(PerroMediano):
    pass

class Dalmata(PerroMediano):
    pass

class Bulldog(PerroMediano):
    pass

class Galgo(PerroMediano):
    pass

class Sabueso(PerroMediano):
    pass

class PastorAleman(PerroGrande):
    pass

class Doberman(PerroGrande):
    pass

class Rottweiler(PerroGrande):
    pass

class Gato(Mascota):
    categoria: str = "Desconocida"

    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float):
        super().__init__(nombre, edad, color)
        self.altura_salto = altura_salto
        self.longitud_salto = longitud_salto

    @staticmethod
    def sonido():
        print("Los gatos maúllan y ronronean")

    def imprimir(self):
        raza = type(self).__name__
        print(f"Gato ({raza}, {self.categoria}): {self.nombre}, edad {self.edad}, color {self.color}, salta {self.altura_salto} m de alto, {self.longitud_salto} m de largo")

class GatoSinPelo(Gato):
    categoria = "sin pelo"

class GatoPeloLargo(Gato):
    categoria = "pelo largo"

class GatoPeloCorto(Gato):
    categoria = "pelo corto"

class Esfinge(GatoSinPelo):
    pass

class Elfo(GatoSinPelo):
    pass

class Donskoy(GatoSinPelo):
    pass

class Angora(GatoPeloLargo):
    pass

class Himalayo(GatoPeloLargo):
    pass

class Balines(GatoPeloLargo):
    pass

class Somali(GatoPeloLargo):
    pass

class AzulRuso(GatoPeloCorto):
    pass

class Britanico(GatoPeloCorto):
    pass

class Manx(GatoPeloCorto):
    pass

class DevonRex(GatoPeloCorto):
    pass

if __name__ == "__main__":
    p1 = Caniche("Toby", 2, "blanco", 5.0, False)
    p2 = Collie("Max", 4, "marrón", 20.0, True)
    g1 = Angora("Luna", 3, "gris", 0.5, 1.2)

    Perro.sonido()
    p1.imprimir()
    Perro.sonido()
    p2.imprimir()

    Gato.sonido()
    g1.imprimir()
