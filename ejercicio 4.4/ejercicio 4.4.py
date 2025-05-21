class Profesor:
    def imprimir(self):
        print("Es un profesor.")

class ProfesorTitular(Profesor):
    def imprimir(self):
        print("Es un profesor titular.")

if __name__ == "__main__":
    print("Polimorfismo")
    profesor1: Profesor = ProfesorTitular()
    profesor1.imprimir()