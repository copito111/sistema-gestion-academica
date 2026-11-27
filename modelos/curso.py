from modelos.profesor import Profesor


MODALIDADES = {
    "1": "Formación titulada",
    "2": "Formación complementaria",
}


class Curso:
    def __init__(
        self, codigo: str, nombre: str, descripcion: str, horas: int,
        modalidad: str, profesor: Profesor,
    ):
        if not all(campo.strip() for campo in (codigo, nombre, descripcion)):
            raise ValueError("El código, el nombre y la descripción son obligatorios.")
        if type(horas) is not int or horas <= 0:
            raise ValueError("La duración debe ser un número entero de horas mayor que cero.")
        if modalidad not in MODALIDADES:
            raise ValueError("La modalidad seleccionada no existe.")
        self.__codigo = codigo.strip()
        self.__nombre = nombre.strip()
        self.__descripcion = descripcion.strip()
        self.__horas = horas
        self.__modalidad = modalidad
        self.__profesor = profesor

    @property
    def codigo(self) -> str:
        return self.__codigo

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def profesor(self) -> Profesor:
        return self.__profesor

    def mostrar_informacion(self) -> str:
        return (
            f"{self.codigo} | {self.nombre} | {MODALIDADES[self.__modalidad]} | "
            f"{self.__horas} h | Profesor {self.profesor.nombre} | {self.__descripcion}"
        )
