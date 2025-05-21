class Persona:
    def __init__(self, nombre: str, direccion: str):
        self._nombre = nombre
        self._direccion = direccion

    def getNombre(self) -> str:
        return self._nombre

    def getDireccion(self) -> str:
        return self._direccion

    def setNombre(self, nombre: str):
        self._nombre = nombre

    def setDireccion(self, direccion: str):
        self._direccion = direccion


class Estudiante(Persona):
    def __init__(self, nombre: str, direccion: str, carrera: str, semestre: int):
        super().__init__(nombre, direccion)
        self._carrera = carrera
        self._semestre = semestre

    def getCarrera(self) -> str:
        return self._carrera

    def getSemestre(self) -> int:
        return self._semestre

    def setCarrera(self, carrera: str):
        self._carrera = carrera

    def setSemestre(self, semestre: int):
        self._semestre = semestre


class Profesor(Persona):
    def __init__(self, nombre: str, direccion: str, departamento: str, categoria: str):
        super().__init__(nombre, direccion)
        self._departamento = departamento
        self._categoria = categoria

    def getDepartamento(self) -> str:
        return self._departamento

    def getCategoria(self) -> str:
        return self._categoria

    def setDepartamento(self, departamento: str):
        self._departamento = departamento

    def setCategoria(self, categoria: str):
        self._categoria = categoria


if __name__ == "__main__":
    e = Estudiante("María", "Calle 123", "Ingeniería Industrial", 5)
    print("Estudiante")
    print("Nombre =", e.getNombre())
    print("Dirección =", e.getDireccion())
    print("Carrera =", e.getCarrera())
    print("Semestre =", e.getSemestre())

    print()

    p = Profesor("Juan", "Avenida Central 45", "Matemáticas", "Titular")
    print("Profesor")
    print("Nombre =", p.getNombre())
    print("Dirección =", p.getDireccion())
    print("Departamento =", p.getDepartamento())
    print("Categoría =", p.getCategoria())
