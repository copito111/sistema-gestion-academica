from datetime import date
from decimal import Decimal

from modelos.aprendiz import Aprendiz
from modelos.calificacion import Calificacion
from modelos.curso import Curso


ESTADOS_INSCRIPCION = ("activa", "cancelada")


class Inscripcion:
    def __init__(self, aprendiz: Aprendiz, curso: Curso):
        self.__aprendiz = aprendiz
        self.__curso = curso
        self.__fecha = date.today()
        self.__estado = "activa"
        self.__calificaciones: list[Calificacion] = []

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

    @property
    def notas(self) -> tuple[Decimal, ...]:
        return tuple(calificacion.valor for calificacion in self.__calificaciones)

    def cambiar_estado(self, estado: str) -> None:
        if estado not in ESTADOS_INSCRIPCION:
            raise ValueError("El estado debe ser activa o cancelada.")
        self.__estado = estado

    def registrar_nota(self, valor: str) -> None:
        self.__calificaciones.append(Calificacion(valor))

    def modificar_nota(self, posicion: int, valor: str) -> None:
        if type(posicion) is not int or not 1 <= posicion <= len(self.__calificaciones):
            raise ValueError("Esa posición de nota no existe.")
        self.__calificaciones[posicion - 1].cambiar_valor(valor)
