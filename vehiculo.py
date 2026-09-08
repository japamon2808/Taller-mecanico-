# Definición de la clase Vehiculo (siguiendo la convención PEP 8 de nombres de clase con mayúscula inicial)
class Vehiculo:

    # Método constructor que se ejecuta automáticamente al crear un nuevo objeto Vehiculo
    def __init__(self, patente: str, annio: int, en_taller: bool = True):
        # 'self' hace referencia a la instancia que se está creando
        # Asigna la patente recibida al atributo propio del objeto
        self.patente = patente
        # Asigna el año recibido al atributo propio del objeto
        self.annio = annio
        # Asigna el estado de permanencia en taller (por defecto True al ingresar)
        self.en_taller = en_taller
