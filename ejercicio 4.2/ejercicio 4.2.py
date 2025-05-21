from abc import ABC, abstractmethod

class Apartamento(ABC):
    def __init__(self, identificador, area, direccion, precio_venta):
        self._id = identificador
        self._area = area
        self._direccion = direccion
        self._precio = precio_venta

    @abstractmethod
    def imprimir(self):
        pass

class ApartamentoFamiliar(Apartamento):
    def __init__(self, identificador, area, direccion, precio_venta,
                 num_habitaciones, num_banos, valor_administracion):
        super().__init__(identificador, area, direccion, precio_venta)
        self.num_habitaciones = num_habitaciones
        self.num_banos = num_banos
        self.valor_administracion = valor_administracion

    def imprimir(self):
        print("Datos apartamento")
        print(f"Identificador inmobiliario = {self._id}")
        print(f"Area = {self._area}")
        print(f"Dirección = {self._direccion}")
        # precio en notación científica con un decimal y E mayúscula
        print(f"Precio de venta = ${self._precio:.1E}")
        print(f"Número de habitaciones = {self.num_habitaciones}")
        print(f"Número de baños = {self.num_banos}")
        print(f"Valor de la administración = ${self.valor_administracion}")
        print()

class ApartaEstudio(Apartamento):
    def __init__(self, identificador, area, direccion, precio_venta,
                 num_habitaciones, num_banos):
        super().__init__(identificador, area, direccion, precio_venta)
        self.num_habitaciones = num_habitaciones
        self.num_banos = num_banos

    def imprimir(self):
        print("Datos apartamento")
        print(f"Identificador inmobiliario = {self._id}")
        print(f"Area = {self._area}")
        print(f"Dirección = {self._direccion}")
        print(f"Precio de venta = ${self._precio:.1E}")
        print(f"Número de habitaciones = {self.num_habitaciones}")
        print(f"Número de baños = {self.num_banos}")
        print()

if __name__ == "__main__":
    # Primer apartamento (familiar)
    ap1 = ApartamentoFamiliar(
        identificador=103067,
        area=120,
        direccion="Avenida Santander 45-45",
        precio_venta=240_000_000,
        num_habitaciones=3,
        num_banos=2,
        valor_administracion=200_000
    )
    # Segundo apartamento (studio)
    ap2 = ApartaEstudio(
        identificador=12354,
        area=50,
        direccion="Avenida Caracas 30-15",
        precio_venta=75_000_000,
        num_habitaciones=1,
        num_banos=1
    )

    ap1.imprimir()
    ap2.imprimir()
