from decimal import Decimal

from modelos.inscripcion import Inscripcion


MINIMO_NOTAS = 3
NOTA_APROBACION = Decimal("3.0")


def calcular_promedio(notas: tuple[Decimal, ...]) -> Decimal | None:
    if len(notas) < MINIMO_NOTAS:
        return None
    return sum(notas) / len(notas)


def resumen_academico(inscripcion: Inscripcion) -> str:
    notas = inscripcion.notas
    promedio = calcular_promedio(notas)
    texto_notas = ", ".join(f"{posicion}) {valor}" for posicion, valor in enumerate(notas, 1))
    encabezado = (
        f"{inscripcion.aprendiz.nombre} ({inscripcion.aprendiz.documento}) | "
        f"{inscripcion.curso.nombre} ({inscripcion.curso.codigo}) | "
        f"Inscripción {inscripcion.estado} | Notas {texto_notas or 'sin notas'}"
    )
    if promedio is None:
        return f"{encabezado} | Pendiente"
    resultado = "Aprobado" if promedio >= NOTA_APROBACION else "Reprobado"
    return f"{encabezado} | Promedio {promedio:.2f} | {resultado}"
