from almacenamiento.memoria import RepositorioEnMemoria
from modelos.aprendiz import Aprendiz
from modelos.curso import MODALIDADES
from modelos.inscripcion import ESTADOS_INSCRIPCION
from modelos.profesor import Profesor
from servicios.gestion_academica import GestionAcademica
from servicios.informes import resumen_academico


def leer(mensaje):
    return input(f"{mensaje}: ").strip()


def leer_edad():
    try:
        return int(leer("Edad"))
    except ValueError as error:
        raise ValueError("La edad debe ser un número entero positivo.") from error


def mostrar_lista(filas):
    filas = tuple(filas)
    if not filas:
        print("No hay registros para mostrar.")
    for fila in filas:
        print(fila)


def mostrar_entidades(entidades):
    mostrar_lista(entidad.mostrar_informacion() for entidad in entidades)


def ejecutar_menu(titulo, opciones, texto_salida="Volver"):
    while True:
        print(f"\n{titulo}")
        for numero, (etiqueta, _) in opciones.items():
            print(f"{numero}. {etiqueta}")
        print(f"0. {texto_salida}")
        opcion = leer("Opción")

        if opcion == "0":
            return
        if opcion not in opciones:
            print("Opción inválida.")
            continue

        _, accion = opciones[opcion]
        try:
            accion()
        except ValueError as error:
            print(f"Error: {error}")


def registrar_profesor(gestion):
    nombre = leer("Nombre")
    documento = leer("Documento")
    edad = leer_edad()

    profesion = leer("Profesión")
    codigo = leer("Código de profesor")
    especialidad = leer("Especialidad")

    profesor = Profesor(nombre, documento, edad, profesion, codigo, especialidad)
    gestion.registrar_profesor(profesor)
    print("Profesor registrado.")


def buscar_profesor(gestion):
    documento = leer("Documento")
    profesor = gestion.buscar_profesor(documento)
    print(profesor.mostrar_informacion())


def menu_profesores(gestion):
    ejecutar_menu("Profesores", {
        "1": ("Registrar profesor", lambda: registrar_profesor(gestion)),
        "2": ("Listar profesores", lambda: mostrar_entidades(gestion.listar_profesores())),
        "3": ("Buscar por documento", lambda: buscar_profesor(gestion)),
    }, texto_salida="Volver al menú principal")


def registrar_aprendiz(gestion):
    nombre = leer("Nombre")
    documento = leer("Documento")
    edad = leer_edad()
    contacto = leer("Contacto (correo o teléfono)")

    aprendiz = Aprendiz(nombre, documento, edad, contacto)
    gestion.registrar_aprendiz(aprendiz)
    print("Aprendiz registrado.")


def buscar_aprendiz(gestion):
    documento = leer("Documento")
    aprendiz = gestion.buscar_aprendiz(documento)
    print(aprendiz.mostrar_informacion())


def menu_aprendices(gestion):
    ejecutar_menu("Aprendices", {
        "1": ("Registrar aprendiz", lambda: registrar_aprendiz(gestion)),
        "2": ("Listar aprendices", lambda: mostrar_entidades(gestion.listar_aprendices())),
        "3": ("Buscar por documento", lambda: buscar_aprendiz(gestion)),
    }, texto_salida="Volver al menú principal")


def registrar_curso(gestion):
    codigo = leer("Código del curso")
    nombre = leer("Nombre")
    descripcion = leer("Descripción")
    try:
        horas = int(leer("Duración en horas"))
    except ValueError as error:
        raise ValueError("La duración debe ser un número entero de horas mayor que cero.") from error

    for clave, etiqueta in MODALIDADES.items():
        print(f"{clave}. {etiqueta}")
    modalidad = leer("Modalidad")
    documento_profesor = leer("Documento del profesor responsable")

    gestion.registrar_curso(codigo, nombre, descripcion, horas, modalidad, documento_profesor)
    print("Curso registrado.")


def buscar_curso(gestion):
    codigo = leer("Código del curso")
    curso = gestion.buscar_curso(codigo)
    print(curso.mostrar_informacion())


def consultar_cursos_del_profesor(gestion):
    documento = leer("Documento del profesor")
    mostrar_entidades(gestion.cursos_del_profesor(documento))


def menu_cursos(gestion):
    ejecutar_menu("Cursos", {
        "1": ("Registrar curso y asignar profesor", lambda: registrar_curso(gestion)),
        "2": ("Listar cursos", lambda: mostrar_entidades(gestion.listar_cursos())),
        "3": ("Buscar por código", lambda: buscar_curso(gestion)),
        "4": ("Consultar por profesor", lambda: consultar_cursos_del_profesor(gestion)),
    }, texto_salida="Volver al menú principal")


def registrar_inscripcion(gestion):
    documento = leer("Documento del aprendiz")
    codigo = leer("Código del curso")
    gestion.inscribir(documento, codigo)
    print("Inscripción registrada.")


def cambiar_estado(gestion):
    documento = leer("Documento del aprendiz")
    codigo = leer("Código del curso")
    estado = leer(f"Estado ({' o '.join(ESTADOS_INSCRIPCION)})").lower()
    gestion.cambiar_estado_inscripcion(documento, codigo, estado)
    print("Estado actualizado.")


def mostrar_inscripciones(inscripciones):
    mostrar_lista(
        f"{inscripcion.aprendiz.nombre} ({inscripcion.aprendiz.documento}) | "
        f"{inscripcion.curso.nombre} ({inscripcion.curso.codigo}) | "
        f"{inscripcion.fecha.isoformat()} | {inscripcion.estado}"
        for inscripcion in inscripciones
    )


def menu_inscripciones(gestion):
    ejecutar_menu("Inscripciones", {
        "1": ("Registrar inscripción", lambda: registrar_inscripcion(gestion)),
        "2": ("Cambiar estado", lambda: cambiar_estado(gestion)),
        "3": ("Cursos de un aprendiz", lambda: mostrar_inscripciones(
            gestion.inscripciones_del_aprendiz(leer("Documento del aprendiz"))
        )),
        "4": ("Aprendices inscritos en un curso", lambda: mostrar_inscripciones(
            gestion.inscripciones_del_curso(leer("Código del curso"))
        )),
    }, texto_salida="Volver al menú principal")


def registrar_nota(gestion, documento_profesor):
    codigo = leer("Código del curso")
    documento = leer("Documento del aprendiz")
    valor = leer("Nota (0.0 a 5.0)")
    gestion.registrar_nota(documento_profesor, documento, codigo, valor)
    print("Nota registrada.")


def modificar_nota(gestion, documento_profesor):
    codigo = leer("Código del curso")
    documento = leer("Documento del aprendiz")
    try:
        posicion = int(leer("Número de la nota"))
    except ValueError as error:
        raise ValueError("El número de la nota debe ser entero.") from error
    valor = leer("Nueva nota (0.0 a 5.0)")
    gestion.modificar_nota(documento_profesor, documento, codigo, posicion, valor)
    print("Nota actualizada.")


def consultar_notas(gestion, documento_profesor):
    codigo = leer("Código del curso")
    documento = leer("Documento del aprendiz")
    notas = gestion.consultar_notas(documento_profesor, documento, codigo)
    mostrar_lista(f"Nota {posicion}: {nota}" for posicion, nota in enumerate(notas, start=1))


def mostrar_informe(inscripciones):
    mostrar_lista(resumen_academico(inscripcion) for inscripcion in inscripciones)


def menu_profesor(gestion):
    profesor = gestion.buscar_profesor(leer("Documento del profesor"))
    documento = profesor.documento
    ejecutar_menu(f"Panel del profesor {profesor.nombre}", {
        "1": ("Registrar nota", lambda: registrar_nota(gestion, documento)),
        "2": ("Modificar nota", lambda: modificar_nota(gestion, documento)),
        "3": ("Consultar notas de una inscripción", lambda: consultar_notas(gestion, documento)),
        "4": ("Ver mis cursos", lambda: mostrar_entidades(gestion.cursos_del_profesor(documento))),
        "5": ("Ver inscritos de un curso", lambda: mostrar_inscripciones(
            gestion.inscripciones_para_profesor(documento, leer("Código del curso"))
        )),
        "6": ("Ver promedios e informe por curso", lambda: mostrar_informe(
            gestion.inscripciones_para_profesor(documento, leer("Código del curso"))
        )),
        "7": ("Ver promedios e informe por aprendiz", lambda: mostrar_informe(
            gestion.inscripciones_de_aprendiz_para_profesor(documento, leer("Documento del aprendiz"))
        )),
    })


def main():
    gestion = GestionAcademica(
        profesores=RepositorioEnMemoria(),
        aprendices=RepositorioEnMemoria(),
        cursos=RepositorioEnMemoria(),
        inscripciones=RepositorioEnMemoria(),
    )
    opciones = {
        "1": ("Profesores", lambda: menu_profesores(gestion)),
        "2": ("Aprendices", lambda: menu_aprendices(gestion)),
        "3": ("Cursos", lambda: menu_cursos(gestion)),
        "4": ("Inscripciones", lambda: menu_inscripciones(gestion)),
        "5": ("Panel del profesor", lambda: menu_profesor(gestion)),
    }

    try:
        ejecutar_menu("Sistema de gestión académica", opciones, texto_salida="Salir")
    except (EOFError, KeyboardInterrupt):
        print()
    print("Hasta luego.")


if __name__ == "__main__":
    main()
