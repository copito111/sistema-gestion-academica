from decimal import Decimal, InvalidOperation


class Calificacion:
    def __init__(self, valor):
        self.cambiar_valor(valor)

    @property
    def valor(self) -> Decimal:
        return self.__valor

    def cambiar_valor(self, valor):
        try:
            numero = Decimal(str(valor).strip().replace(",", "."))
        except InvalidOperation as error:
            raise ValueError("Escribe una nota numérica, como 3.5.") from error
        if not numero.is_finite() or not Decimal("0") <= numero <= Decimal("5"):
            raise ValueError("La nota debe estar entre 0.0 y 5.0.")
        self.__valor = numero

