from enums import Starclass, PlanetType, AtmossphericComposition, VolcamismType, BioType

class Body:

    name: str
    id: int
    systemName: str
    systemId: int
    biologicalCount: int

    # Predictors

    parentStar: Starclass
    planetType: PlanetType
    atmossphericComposition: AtmossphericComposition
    volcamismType: VolcamismType
    atmosphericPressure: float
    gravity: float
    minTemperature: float
    maxTemperature: float
    

    def __init__(self, name: str, id: int, systemName: str, systemId: int, biologicalCount: int,
                 parentStar: Starclass, planetType: PlanetType, atmossphericComposition: AtmossphericComposition,
                 volcamismType: VolcamismType, atmosphericPressure: float, gravity: float, 
                 minTemperature: float, maxTemperature: float):
        self.name = name
        self.id = id
        self.systemName = systemName
        self.systemId = systemId
        self.biologicalCount = biologicalCount
        self.parentStar = parentStar
        self.planetType = planetType
        self.atmossphericComposition = atmossphericComposition
        self.volcamismType = volcamismType
        self.atmosphericPressure = atmosphericPressure
        self.gravity = gravity
        self.minTemperature = minTemperature
        self.maxTemperature = maxTemperature