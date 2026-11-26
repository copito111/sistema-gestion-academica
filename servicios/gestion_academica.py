from almacenamiento.contratos import Repositorio
from modelos.profesor import Profesor


class GestionAcademica:
    def __init__(self, profesores: Repositorio[str, Profesor]):
        self.__profesores = profesores

    def registrar_profesor(self, profesor: Profesor) -> None:
        if self.__profesores.buscar(profesor.documento) is not None:
            raise ValueError("Ya existe un profesor con ese documento.")

        for registrado in self.listar_profesores():
            if registrado.codigo == profesor.codigo:
                raise ValueError("Ya existe un profesor con ese código.")

        self.__profesores.guardar(profesor.documento, profesor)

    def listar_profesores(self) -> tuple[Profesor, ...]:
        return self.__profesores.listar()

    def buscar_profesor(self, documento: str) -> Profesor:
        profesor = self.__profesores.buscar(documento.strip())
        if profesor is None:
            raise ValueError("Profesor no encontrado.")
        return profesor
