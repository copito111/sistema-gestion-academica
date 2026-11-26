"""Punto de entrada para el sistema académico de consola."""

SECCIONES = {
    "1": "Profesores",
    "2": "Aprendices",
    "3": "Cursos",
    "4": "Inscripciones",
    "5": "Calificaciones e informes",
}


def main():
    while True:
        print("\nSistema de gestión académica")
        for numero, nombre in SECCIONES.items():
            print(f"{numero}. {nombre}")
        print("0. Salir")

        opcion = input("Elige una opción: ").strip()
        if opcion == "0":
            print("Hasta luego.")
            return

        nombre = SECCIONES.get(opcion)
        if nombre is None:
            print("Opción inválida.")
        else:
            print(f"{nombre}: pendiente de implementar.")


if __name__ == "__main__":
    main()
