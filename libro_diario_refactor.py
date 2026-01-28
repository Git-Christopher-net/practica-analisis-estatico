"""
Módulo de gestión contable para Negocios Digitales.
Proporciona la clase LibroDiario para el registro de transacciones.
"""


class LibroDiario:
    """
    Clase que representa un libro contable para registrar ingresos y egresos.
    """

    def __init__(self):
        """Inicializa una lista vacía de transacciones."""
        self.transacciones = []

    def registrar_transaccion(self, fecha: str, descripcion: str,
                              monto: float, tipo: str):
        """
        Registra una nueva transacción financiera con validación de datos.
        """
        tipos_validos = ["ingreso", "egreso"]

        if tipo not in tipos_validos:
            raise ValueError(f"Tipo inválido. Debe ser: {tipos_validos}")

        if monto <= 0:
            raise ValueError("El monto debe ser un número positivo.")

        self.transacciones.append({
            "fecha": fecha,
            "descripcion": descripcion,
            "monto": monto,
            "tipo": tipo
        })

    def obtener_resumen_financiero(self) -> dict:
        """
        Calcula el total de ingresos y egresos.
        Retorna un diccionario con los resultados.
        """
        totales = {"ingresos": 0.0, "egresos": 0.0}

        for transaccion in self.transacciones:
            if transaccion["tipo"] == "ingreso":
                totales["ingresos"] += transaccion["monto"]
            else:
                totales["egresos"] += transaccion["monto"]

        return totales
    