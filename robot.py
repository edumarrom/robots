from mapa import Mapa
from random import choice as aleatorio
from brujula import Brujula
# Clase Robot - edumarrom

IZQUIERDA = ('L', 'I', 'LEFT', 'IZQUIERDA', 'IZQ')
DERECHA = ('R', 'D', 'RIGHT', 'DERECHA', 'DER')

class Robot:
    __ultimo = 0
    def __init__(self, alias, gen):
        Robot.__ultimo += 1
        self.__numero = Robot.__ultimo  # act1
        self.__alias = alias
        self.set_generacion(gen.upper())
        self.brujula = Brujula()
        lat, lon = Mapa.posicion_aleatoria()
        self.__posicion = Mapa(lat, lon)
        self.__orientacion = self.brujula.punto_aleatorio()
        self.__distancia = 0

    """
    def __repr__(self):
        return f"Robot('{self.__alias}', '{self.__generacion}')"
    """

    def __str__(self):
        return f'{self.saludar()} | {self.orientacion()} | {self.distancia()} m. recorridos | {self.posicion()}'

    @staticmethod
    def comprobar_generacion(gen):
        return gen in ('A', 'B', 'M')

    def alias(self):
        return self.__alias

    def set_generacion(self, gen):
        if self.comprobar_generacion(gen):
            self.__generacion = gen
        else: raise ValueError(f"'{gen}' no es una generación válida.")

    def orientacion(self):
        return self.__orientacion

    def set_orientacion(self, ori):
        self.__orientacion = ori

    def posicion(self):
        return self.__posicion

    def distancia(self):
        return self.__distancia


    def girar(self, direccion):
        if direccion.upper() in IZQUIERDA:
            destino = self.brujula.izquierda(self.orientacion())
            self.set_orientacion(destino)
        elif direccion.upper() in DERECHA:
            destino = self.brujula.derecha(self.orientacion())
            self.set_orientacion(destino)
        else: raise ValueError(f"'{direccion}' no es una dirección válida.")

    def avanzar(self, distancia):
        direccion = self.orientacion()
        self.__posicion.mover(direccion, distancia)
        self.__distancia += distancia

    def saludar(self):
        return f'{self.__generacion}{self.__numero} ({self.__alias})'

paco = Robot('Paco', 'm')
paco.orientacion()
paco.girar('izquierda')
paco.orientacion()
manolo = Robot('Manolo', 'z')
paco.avanzar(300)
paco.girar('der')
paco.avanzar(750)
paco.girar('r')
print(paco)
