from almacenamiento.memoria import RepositorioEnMemoria
from modelos.profesor import Profesor
from servicios.gestion_academica import GestionAcademica


SECCIONES_PENDIENTES = {
    "2": "Aprendices",
    "3": "Cursos",
    "4": "Inscripciones",
    "5": "Calificaciones e informes",
}


def leer(mensaje):
    return input(f"{mensaje}: ").strip()


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
    try:
        edad = int(leer("Edad"))
    except ValueError as error:
        raise ValueError("La edad debe ser un número entero positivo.") from error

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


def main():
    repositorio = RepositorioEnMemoria()
    gestion = GestionAcademica(profesores=repositorio)
    opciones = {"1": ("Profesores", lambda: menu_profesores(gestion))}
    for numero, nombre in SECCIONES_PENDIENTES.items():
        opciones[numero] = (nombre, lambda etapa=nombre: print(f"{etapa}: pendiente de implementar."))

    try:
        ejecutar_menu("Sistema de gestión académica", opciones, texto_salida="Salir")
    except (EOFError, KeyboardInterrupt):
        print()
    print("Hasta luego.")


if __name__ == "__main__":
    main()
