"""Contrato común de profesores y aprendices."""

from abc import ABC, abstractmethod


class Persona(ABC):
    # Camilo y Santiago: acuerden el constructor, los atributos privados y sus validaciones.

    @abstractmethod
    def mostrar_informacion(self) -> str:
        """Devuelve la información descriptiva de la persona."""

    @abstractmethod
    def obtener_rol(self) -> str:
        """Devuelve el rol de la persona en el sistema."""
