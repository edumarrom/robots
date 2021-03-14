from random import choice as punto_aleatorio
class Brujula:
    """
    Clase Brújula
    ---
    La clase brújula representa los puntos cardinales en los que un \
        robot puede orientarse.

    Por defecto, estos puntos son 'Norte', 'Este', 'Sur' y 'Oeste'.
    """
    def __init__(self, puntos=None):
        """Constructor de la clase Brujuls."""
        if puntos is not None:
            self.__puntos = puntos
        else:
            self.__puntos = ('N', 'E', 'S', 'O')

    def punto_aleatorio(self):
        """Devuelve un punto cardinal aleatorio."""
        return punto_aleatorio(self.__puntos)

    def es_punto_cardinal(self, punto):
        """
        Devuelve True si el punto recibido existe en los puntos de la \
            brujula, False en caso contrario.
        """
        return  punto in self.__puntos

    def __comprobar_punto_cardinal(self, punto):
        """
        Comprueba si el punto cardinal recibido es válido. \
        De no serlo, devuelve una excepción ValueError.
        """
        if not self.es_punto_cardinal(punto):
            raise ValueError(f"'{punto}' no es un punto cardinal válido.")

    def izquierda(self, punto):
        """
        Devuelve el punto cardinal a la izquierda del punto recibido.
        """
        self.__comprobar_punto_cardinal(punto)
        pos = self.__puntos.index(punto) - 1
        return self.__puntos[pos % len(self.__puntos)]

    def derecha(self, punto):
        """
        Devuelve el punto cardinal a la derecha del punto recibido.
        """
        self.__comprobar_punto_cardinal(punto)
        pos = self.__puntos.index(punto) + 1
        return self.__puntos[pos % len(self.__puntos)]

    def detras(self, punto):
        """
        Devuelve el punto cardinal a espaldas del punto recibido.
        """
        self.__comprobar_punto_cardinal(punto)
        pos = self.__puntos.index(punto) + 2
        return self.__puntos[pos % len(self.__puntos)]
