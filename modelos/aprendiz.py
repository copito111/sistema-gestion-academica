from modelos.persona import Persona


class Aprendiz(Persona):
    def __init__(self, nombre, documento, edad, contacto):
        super().__init__(nombre, documento, edad)
        if not contacto.strip():
            raise ValueError("El contacto es obligatorio.")
        self.__contacto = contacto.strip()

    def obtener_rol(self) -> str:
        return "Aprendiz"

    def mostrar_informacion(self) -> str:
        return (
            f"{self.obtener_rol()} {self.nombre} | Documento {self.documento} | "
            f"Edad {self.edad} | Contacto {self.__contacto}"
        )





