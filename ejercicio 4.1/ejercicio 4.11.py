class Cuenta:
    def __init__(self, saldo=0.0, tasa_anual=0.0, comision_mensual=0.0):
        self._saldo = saldo
        self._num_consignaciones = 0
        self._num_retiros = 0
        self._tasa_anual = tasa_anual
        self._comision_mensual = comision_mensual

    def consignar(self, monto):
        self._saldo += monto
        self._num_consignaciones += 1

    def retirar(self, monto):
        if monto <= self._saldo:
            self._saldo -= monto
            self._num_retiros += 1

    def calcular_interes(self):
        return self._saldo * (self._tasa_anual / 12)

    def extracto_mensual(self):
        interes = self.calcular_interes()
        self._saldo += interes
        self._saldo -= self._comision_mensual
        return interes, self._saldo

class CuentaAhorros(Cuenta):
    def __init__(self, saldo=0.0, tasa_anual=0.0, comision_mensual=0.0):
        super().__init__(saldo, tasa_anual, comision_mensual)

if __name__ == "__main__":
    print("Cuenta de ahorros")
    saldo_inicial = float(input("Ingrese saldo inicial= $"))
    tasa_str = input("Ingrese tasa de interés: ")
    tasa = float(tasa_str.replace(',', '.'))
    cons = float(input("Ingresar cantidad a consignar: $"))
    ret = float(input("Ingresar cantidad a retirar: $"))

    ca = CuentaAhorros(saldo_inicial, tasa, 0.0)
    ca.consignar(cons)
    ca.retirar(ret)
    num_trans = ca._num_consignaciones + ca._num_retiros
    interes_mensual, saldo_final = ca.extracto_mensual()

    print(f"Saldo = $ {saldo_final:.3f}")
    print(f"Comisión mensual = $ {ca._comision_mensual}")
    print(f"Número de transacciones = {num_trans}")
