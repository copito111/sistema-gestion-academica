from almacenamiento.contratos import Repositorio
from modelos.aprendiz import Aprendiz
from modelos.profesor import Profesor


class GestionAcademica:
    def __init__(
        self,
        profesores: Repositorio[str, Profesor],
        aprendices: Repositorio[str, Aprendiz],
    ):
        self.__profesores = profesores
        self.__aprendices = aprendices

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

    def registrar_aprendiz(self, aprendiz: Aprendiz) -> None:
        if self.__aprendices.buscar(aprendiz.documento) is not None:
            raise ValueError("Ya existe un aprendiz con ese documento.")
        self.__aprendices.guardar(aprendiz.documento, aprendiz)

    def listar_aprendices(self) -> tuple[Aprendiz, ...]:
        return self.__aprendices.listar()

    def buscar_aprendiz(self, documento: str) -> Aprendiz:
        aprendiz = self.__aprendices.buscar(documento.strip())
        if aprendiz is None:
            raise ValueError("Aprendiz no encontrado.")
        return aprendiz