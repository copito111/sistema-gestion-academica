from decimal import Decimal

from almacenamiento.contratos import Repositorio
from modelos.aprendiz import Aprendiz
from modelos.curso import Curso
from modelos.inscripcion import Inscripcion
from modelos.profesor import Profesor


class GestionAcademica:
    def __init__(
        self,
        profesores: Repositorio[str, Profesor],
        aprendices: Repositorio[str, Aprendiz],
        cursos: Repositorio[str, Curso],
        inscripciones: Repositorio[tuple[str, str], Inscripcion],
    ):
        self.__profesores = profesores
        self.__aprendices = aprendices
        self.__cursos = cursos
        self.__inscripciones = inscripciones

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

    def registrar_curso(self, codigo, nombre, descripcion, horas, modalidad, documento_profesor) -> None:
        profesor = self.buscar_profesor(documento_profesor)
        curso = Curso(codigo, nombre, descripcion, horas, modalidad, profesor)
        if self.__cursos.buscar(curso.codigo) is not None:
            raise ValueError("Ya existe un curso con ese código.")
        self.__cursos.guardar(curso.codigo, curso)

    def listar_cursos(self) -> tuple[Curso, ...]:
        return self.__cursos.listar()

    def buscar_curso(self, codigo: str) -> Curso:
        curso = self.__cursos.buscar(codigo.strip())
        if curso is None:
            raise ValueError("Curso no encontrado.")
        return curso

    def cursos_del_profesor(self, documento_profesor: str) -> tuple[Curso, ...]:
        profesor = self.buscar_profesor(documento_profesor)
        return tuple(
            curso for curso in self.listar_cursos()
            if curso.profesor.documento == profesor.documento
        )

    def inscribir(self, documento_aprendiz: str, codigo_curso: str) -> None:
        aprendiz = self.buscar_aprendiz(documento_aprendiz)
        curso = self.buscar_curso(codigo_curso)
        clave = (aprendiz.documento, curso.codigo)
        if self.__inscripciones.buscar(clave) is not None:
            raise ValueError("Este aprendiz ya tiene una inscripción en el curso.")
        self.__inscripciones.guardar(clave, Inscripcion(aprendiz, curso))

    def buscar_inscripcion(self, documento_aprendiz: str, codigo_curso: str) -> Inscripcion:
        clave = (documento_aprendiz.strip(), codigo_curso.strip())
        inscripcion = self.__inscripciones.buscar(clave)
        if inscripcion is None:
            raise ValueError("Inscripción no encontrada.")
        return inscripcion

    def cambiar_estado_inscripcion(
        self, documento_aprendiz: str, codigo_curso: str, estado: str,
    ) -> None:
        inscripcion = self.buscar_inscripcion(documento_aprendiz, codigo_curso)
        inscripcion.cambiar_estado(estado)

    def inscripciones_del_aprendiz(self, documento: str) -> tuple[Inscripcion, ...]:
        aprendiz = self.buscar_aprendiz(documento)
        return tuple(
            inscripcion for inscripcion in self.__inscripciones.listar()
            if inscripcion.aprendiz.documento == aprendiz.documento
        )

    def inscripciones_del_curso(self, codigo: str) -> tuple[Inscripcion, ...]:
        curso = self.buscar_curso(codigo)
        return tuple(
            inscripcion for inscripcion in self.__inscripciones.listar()
            if inscripcion.curso.codigo == curso.codigo
        )

    def registrar_nota(self, documento_profesor, documento_aprendiz, codigo_curso, valor) -> None:
        inscripcion = self.__inscripcion_editable(documento_profesor, documento_aprendiz, codigo_curso)
        inscripcion.registrar_nota(valor)

    def modificar_nota(self, documento_profesor, documento_aprendiz, codigo_curso, posicion, valor) -> None:
        inscripcion = self.__inscripcion_editable(documento_profesor, documento_aprendiz, codigo_curso)
        inscripcion.modificar_nota(posicion, valor)

    def consultar_notas(self, documento_profesor, documento_aprendiz, codigo_curso) -> tuple[Decimal, ...]:
        self.__verificar_profesor_del_curso(documento_profesor, codigo_curso)
        return self.buscar_inscripcion(documento_aprendiz, codigo_curso).notas

    def inscripciones_para_profesor(
        self, documento_profesor: str, codigo_curso: str,
    ) -> tuple[Inscripcion, ...]:
        self.__verificar_profesor_del_curso(documento_profesor, codigo_curso)
        return self.inscripciones_del_curso(codigo_curso)

    def inscripciones_de_aprendiz_para_profesor(
        self, documento_profesor: str, documento_aprendiz: str,
    ) -> tuple[Inscripcion, ...]:
        profesor = self.buscar_profesor(documento_profesor)
        return tuple(
            inscripcion for inscripcion in self.inscripciones_del_aprendiz(documento_aprendiz)
            if inscripcion.curso.profesor.documento == profesor.documento
        )

    def __verificar_profesor_del_curso(self, documento_profesor: str, codigo_curso: str) -> None:
        curso = self.buscar_curso(codigo_curso)
        if curso.profesor.documento != documento_profesor.strip():
            raise ValueError("El curso no está asignado a ese profesor.")

    def __inscripcion_editable(self, documento_profesor, documento_aprendiz, codigo_curso) -> Inscripcion:
        self.__verificar_profesor_del_curso(documento_profesor, codigo_curso)
        inscripcion = self.buscar_inscripcion(documento_aprendiz, codigo_curso)
        if inscripcion.estado != "activa":
            raise ValueError("Solo se pueden cambiar notas de inscripciones activas.")
        return inscripcion
