from coordenada import Coordenada
from random import choice as aleatorio
from brujula import Brujula

# Sinónimos que el usuario podrá utilizar para girar.
IZQUIERDA = ('L', 'I', 'LEFT', 'IZQUIERDA', 'IZQ')
DERECHA = ('R', 'D', 'RIGHT', 'DERECHA', 'DER')
DETRAS = ('B', 'A', 'TR', 'DETRAS', 'ATRAS', 'BACK', 'ESPALDA', \
    'TURN AROUND', 'MEDIA VUELTA')

class Robot:
    """
    Clase Robot
    ---
    La clase Robot representa a un robot, el cual tiene la habilidad \
        de moverse a traves de un plano bidimensional.

    El robot está compuesto por:
        - numero: int -> número de identificación.
        - alias: str -> Alias del robot.
        - generacion: str -> Generación a la que pertenece.
        - orientacion: Mapa
        - posicion

    """
    __ultimo = 0
    def __init__(self, alias, gen):
        Robot.__ultimo += 1
        self.__numero = Robot.__ultimo  # act1
        self.__alias = alias
        self.set_generacion(gen.upper())
        self.brujula = Brujula()
        self.__orientacion = self.brujula.punto_aleatorio()
        lat, lon = Coordenada.posicion_aleatoria()
        self.__posicion = Coordenada(lat, lon)
        self.__distancia = 0

    """
    def __repr__(self):
        return f"Robot('{self.__alias}', '{self.__generacion}')"
    """

    def __str__(self):
        """Devuelve un literal que describe el estado del robot."""
        return f'{self.saludar()} | {self.orientacion()} | '\
            f'{self.distancia()} m. recorridos | '\
            f'X: {self.posicion().latitud()}, Y: {self.posicion().longitud()}'

    @staticmethod
    def comprobar_generacion(gen):
        """
        Devuelve True si la generacion recibida es válida, \
            False en caso contrario.
        """
        return gen in ('A', 'B', 'M')

    def alias(self):
        """Devuelve el alias de un robot."""
        return self.__alias

    def orientacion(self):
        """Devuelve el punto cardinal al que el robot está mirando."""
        return self.__orientacion

    def posicion(self):
        """Devuelve la posición en la que se encuentra el robot."""
        return self.__posicion

    def distancia(self):
        """Devuelve en metros la distancia recorrida por el robot."""
        return self.__distancia

    def set_orientacion(self, ori):
        """Asigna un nuevo punto cardinal al robot."""
        self.__orientacion = ori

    def set_generacion(self, gen):
        """Asigna una nueva generación al robot."""
        if self.comprobar_generacion(gen):
            self.__generacion = gen
        else: raise ValueError(f"'{gen}' no es una generación válida.")

    def girar(self, direccion):
        """
        El robot gira sobre sí mísmo, haciendo que mire a la \
            izquierda derecha o atrás.
        """
        if direccion.upper() in IZQUIERDA:
            destino = self.brujula.izquierda(self.orientacion())
            self.set_orientacion(destino)
        elif direccion.upper() in DERECHA:
            destino = self.brujula.derecha(self.orientacion())
            self.set_orientacion(destino)
        elif direccion.upper() in DETRAS:
            destino = self.brujula.detras(self.orientacion())
            self.set_orientacion(destino)
        else: raise ValueError(f"'{direccion}' no es una dirección válida.")

    def avanzar(self, distancia = 1):
        """Hace avanzar al robot una distancia dada."""
        direccion = self.orientacion()
        self.__posicion.mover(direccion, distancia)
        self.__distancia += distancia

    def saludar(self):
        """El robot saluda, indicando su nombre completo \
            (código del robot + (alias).
        """
        return f'{self.__generacion}{self.__numero} ({self.__alias})'


if __name__ == "__main__":
    paco = Robot('Paco', 'm')
    paco.saludar()
    paco.orientacion()
    paco.girar('izquierda')
    paco.orientacion()
    # manolo = Robot('Manolo', 'z') Devuelve una excepción ValueError.
    paco.avanzar(300)
    paco.girar('der')
    paco.avanzar()
    paco.girar('detras')
    print(paco)
