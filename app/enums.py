from enum import Enum

def list_enum_to_json(ls:list[Enum]):
    res = '['
    for item in ls:
        res += ('"' + item._name_ + '", ')
    return res[:-2] + ']'

def list_json_to_enum(ls:list[str], cls):
    res = []
    for item in ls:
        res.append(cls[item])
    return res

class Starclass(Enum):
    O           = 0
    B           = 1
    A           = 2
    F           = 3
    G           = 4
    K           = 5
    M           = 6
    Be          = 7
    TTS         = 8
    C           = 9
    S           = 10
    W           = 11
    Black_Hole  = 12
    Neutron     = 13
    D           = 14
    L           = 15
    T           = 16
    Y           = 17
    Any         = 18
    Ae          = 19
    N           = 20
    

class PlanetType(Enum):
    Rock        = 0
    HMC         = 1
    Ice         = 2
    RockIce     = 3

class AtmossphericComposition(Enum):
    NH3     = 0
    CO2     = 1
    Ar      = 2
    CH4     = 3
    O       = 4
    Ni      = 5
    Ne      = 6
    SO2     = 7
    H2O     = 8
    He      = 9
    Any     = 10


class VolcanismType(Enum):
    none                    = 0
    Any                     = 1
    Low                     = 2
    WaterMagma              = 3
    SulphurDioxideMagma     = 4
    AmmoniaMagma            = 5
    MethaneMagma            = 6
    NitrogenMagma           = 7
    SilicateMagma           = 8
    MetalicMagma            = 9
    WaterGeyser             = 10
    CarbonGeyser            = 11
    AmmoniaGeyser           = 12
    MethanGeyser            = 13
    NitrogenGeyser          = 14
    HeliumGeyser            = 15
    SilicateGeyser          = 16
    RockyMagma              = 17


class BioType(Enum):
    Bacterium   =  0
    Fonticulua  = 1
    Aleoida     = 2
    Tussock     = 3
    Cactoida    = 4
    Clypeus     = 5
    Concha      = 6
    Electicae   = 7
    Frutexa     = 8
    Fumerola    = 9
    Fungoida    = 10
    Osseus      = 11
    Recepta     = 12
    Tubus       = 13
    Stratum     = 14