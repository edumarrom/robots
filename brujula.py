from random import choice as aleatorio
# Clase brújula
class Brujula:

    def __init__(self, puntos=None):
        if puntos is not None:
            self.__puntos = puntos
        else:
            self.__puntos = ('N', 'E', 'S', 'O')

    def punto_aleatorio(self):
        return aleatorio(self.__puntos)

    def es_punto_cardinal(self, punto):
        return  punto in self.__puntos

    def __comprobar_punto_cardinal(self, punto):
        if not self.es_punto_cardinal(punto):
            raise ValueError(f"'{punto}' no es un punto cardinal válido.")

    def izquierda(self, punto):
        self.__comprobar_punto_cardinal(punto)
        pos = self.__puntos.index(punto) - 1
        return self.__puntos[pos % len(self.__puntos)]

    def derecha(self, punto):
        self.__comprobar_punto_cardinal(punto)
        pos = self.__puntos.index(punto) + 1
        return self.__puntos[pos % len(self.__puntos)]
