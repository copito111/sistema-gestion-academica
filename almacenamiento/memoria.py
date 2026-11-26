from typing import Generic, TypeVar


Clave = TypeVar("Clave")
Entidad = TypeVar("Entidad")


class RepositorioEnMemoria(Generic[Clave, Entidad]):
    def __init__(self):
        self.__datos: dict[Clave, Entidad] = {}

    def buscar(self, clave: Clave) -> Entidad | None:
        return self.__datos.get(clave)

    def listar(self) -> tuple[Entidad, ...]:
        return tuple(self.__datos.values())

    def guardar(self, clave: Clave, entidad: Entidad) -> None:
        self.__datos[clave] = entidad
