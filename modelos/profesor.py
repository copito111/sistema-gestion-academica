from modelos.persona import Persona


class Profesor(Persona):
    def __init__(self, nombre, documento, edad, profesion, codigo, especialidad):
        super().__init__(nombre, documento, edad)
        if not all(campo.strip() for campo in (profesion, codigo, especialidad)):
            raise ValueError("La profesión, el código y la especialidad son obligatorios.")
        self.__profesion = profesion.strip()
        self.__codigo = codigo.strip()
        self.__especialidad = especialidad.strip()

    @property
    def codigo(self) -> str:
        return self.__codigo

    def obtener_rol(self) -> str:
        return "Profesor"

    def mostrar_informacion(self) -> str:
        return (
            f"{self.obtener_rol()} {self.nombre} | Documento {self.documento} | "
            f"Edad {self.edad} | Código {self.codigo} | "
            f"Profesión {self.__profesion} | Especialidad {self.__especialidad}"
        )
