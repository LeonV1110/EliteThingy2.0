from enum import Enum

class Starclass(Enum):
    O = 0
    B = 1
    A = 2
    F = 3
    G = 4
    K = 5
    M = 6
    Ae_Be = 7
    TTS = 8
    C = 9
    S = 10
    W = 11
    Black_Hole = 12
    Neutron = 13
    D = 14
    L = 15
    T = 16
    Y = 17

class PlanetType(Enum):
    Rocky = 0
    #TODO

class AtmossphericComposition(Enum):
    none = 0
    #TODO


class VolcamismType(Enum):
    none = 0
    #TODO

class BioType(Enum):
    Bacterium: 0