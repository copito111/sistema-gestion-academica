from datetime import date

from modelos.aprendiz import Aprendiz
from modelos.curso import Curso


ESTADOS_INSCRIPCION = ("activa", "cancelada")


class Inscripcion:
    def __init__(self, aprendiz: Aprendiz, curso: Curso):
        self.__aprendiz = aprendiz
        self.__curso = curso
        self.__fecha = date.today()
        self.__estado = "activa"

    @property
    def aprendiz(self) -> Aprendiz:
        return self.__aprendiz

    @property
    def curso(self) -> Curso:
        return self.__curso

    @property
    def fecha(self) -> date:
        return self.__fecha

    @property
    def estado(self) -> str:
        return self.__estado

    def cambiar_estado(self, estado: str) -> None:
        if estado not in ESTADOS_INSCRIPCION:
            raise ValueError("El estado debe ser activa o cancelada.")
        self.__estado = estado
