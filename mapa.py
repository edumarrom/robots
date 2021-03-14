from random import randint
from warnings import resetwarnings


class Mapa:
    """Soy el mapa!"""
    def __init__(self, latitud, longitud):
        self.__latitud = latitud
        self.__longitud = longitud

    def __repr__(self):
        return f'[{self.__latitud}, {self.__longitud}]'

    def latitud(self):
        return self.__latitud

    def longitud(self):
        return self.__longitud

    def mover(self, orientacion, distancia):
        """
        si voy al norte, sumo a la longitud, al sur es restar
        si voy al este, sumo a la latitud, al oeste es restar
        """
        if orientacion in ('N', 'E'):
            if orientacion == 'N':
                self.__longitud += distancia
            else: self.__latitud  += distancia
        elif orientacion in ('S', 'O'):
            if orientacion == 'S':
                self.__longitud -= distancia
            else: self.__latitud  -= distancia

    @staticmethod
    def posicion_aleatoria():
        return randint(-100, 100), randint(-100, 100)
