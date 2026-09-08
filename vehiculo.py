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
        # Inicializa el atributo _en_taller con el mismo valor (encapsulamiento según diagrama)
        self._en_taller = en_taller

    # Definición del método ingresar (no recibe parámetros adicionales ni retorna ningún valor)
    def ingresar(self):
        # Cambia el estado del atributo _en_taller a True indicando que el vehículo está en el taller
        self._en_taller = True
        # Mantiene sincronizado el atributo en_taller con valor True
        self.en_taller = True

    # Definición del método entregar (no recibe parámetros adicionales ni retorna ningún valor)
    def entregar(self):
        # Cambia el estado del atributo _en_taller a False indicando que el vehículo fue retirado del taller
        self._en_taller = False
        # Mantiene sincronizado el atributo en_taller con valor False
        self.en_taller = False

