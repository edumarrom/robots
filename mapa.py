from random import randint
from warnings import resetwarnings


class Coordenada:
    """
    Clase Coordenada
    ---
    La clase coordenada representa la posición de un robot en un plano bidimensional.
    Esta posición se representa con la latitud (eje x) y la longitud (eje y).
    """
    def __init__(self, latitud, longitud):
        """Constructor de la clase Coordenada."""
        self.__latitud = latitud
        self.__longitud = longitud

    def __repr__(self):
        return f'[{self.__latitud}, {self.__longitud}]'

    @staticmethod
    def posicion_aleatoria():
        """Devuelve una posición aleatoria."""
        return randint(-100, 100), randint(-100, 100)

    def latitud(self):
        """Devuelve la latitud de una coordenada."""
        return self.__latitud

    def longitud(self):
        """Devuelve la longitud de una coordenada."""
        return self.__longitud

    def mover(self, orientacion, distancia):
        """
        Modifica la coordenada, teniendo en cuenta un punto cardinal.
        """
        if orientacion in ('N', 'E'):
            if orientacion == 'N':
                self.__longitud += distancia
            else: self.__latitud  += distancia
        elif orientacion in ('S', 'O'):
            if orientacion == 'S':
                self.__longitud -= distancia
            else: self.__latitud  -= distancia
