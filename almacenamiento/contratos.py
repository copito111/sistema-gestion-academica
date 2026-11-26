from typing import Protocol, TypeVar


Clave = TypeVar("Clave", contravariant=True)
Resultado = TypeVar("Resultado", covariant=True)
Entidad = TypeVar("Entidad", contravariant=True)


class Lectura(Protocol[Clave, Resultado]):
    def buscar(self, clave: Clave) -> Resultado | None:
        ...

    def listar(self) -> tuple[Resultado, ...]:
        ...


class Escritura(Protocol[Clave, Entidad]):
    def guardar(self, clave: Clave, entidad: Entidad) -> None:
        ...


TipoClave = TypeVar("TipoClave")
TipoEntidad = TypeVar("TipoEntidad")


class Repositorio(Lectura[TipoClave, TipoEntidad], Escritura[TipoClave, TipoEntidad], Protocol):
    """Contrato para los usos que requieren tanto lectura como escritura."""