from abc import ABC, abstractmethod


class Persona(ABC):
    def __init__(self, nombre: str, documento: str, edad: int):
        if not nombre.strip() or not documento.strip():
            raise ValueError("El nombre y el documento son obligatorios.")
        if type(edad) is not int or edad <= 0:
            raise ValueError("La edad debe ser un número entero positivo.")
        self.__nombre = nombre.strip()
        self.__documento = documento.strip()
        self.__edad = edad

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def documento(self) -> str:
        return self.__documento

    @property
    def edad(self) -> int:
        return self.__edad

    @abstractmethod
    def obtener_rol(self) -> str:
        """Devuelve el rol de la persona."""

    @abstractmethod
    def mostrar_informacion(self) -> str:
        """Devuelve una descripción de la persona."""