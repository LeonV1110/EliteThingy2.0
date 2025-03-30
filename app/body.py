from enums import Starclass, PlanetType, AtmossphericComposition, VolcanismType, BioType

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
    volcamismType: VolcanismType
    atmosphericPressure: float
    gravity: float
    minTemperature: float
    maxTemperature: float
    

    def __init__(self, name: str, id: int, systemName: str, systemId: int, biologicalCount: int,
                 parentStar: Starclass, planetType: PlanetType, atmossphericComposition: AtmossphericComposition,
                 volcamismType: VolcanismType, atmosphericPressure: float, gravity: float, 
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



    def to_json(self):
        return f'{{"id":{self.id}, "Name":"{self.name}", "SystemId": {self.systemId}, "SystemName":"{self.systemName}", "BioCount": {self.biologicalCount}, "ParentStar": "{self.parentStar._name_}", "PlanetType": "{self.planetType._name_}", "AtmosComp": "{self.atmossphericComposition._name_}", "Volcanism": "{self.volcamismType._name_}", "Pressure": {round(self.atmosphericPressure, 2)}, "Gravity": {round(self.gravity, 2)}, "minTemp": {self.minTemperature}, "maxTemp": {self.maxTemperature}}}'


class jsonBody(Body):
    def __init__(self, jsonDict: dict):
        self.name = jsonDict["Name"]
        self.id = jsonDict["id"]
        self.systemName = jsonDict["SystemName"]
        self.systemId = jsonDict["SystemId"]
        self.biologicalCount = jsonDict["BioCount"]
        self.parentStar = Starclass[jsonDict["ParentStar"]]
        self.planetType = PlanetType[jsonDict["PlanetType"]]
        self.atmossphericComposition = AtmossphericComposition[jsonDict["AtmosComp"]]
        self.volcamismType = VolcanismType[jsonDict["Volcanism"]]
        self.atmosphericPressure = jsonDict["Pressure"]
        self.gravity = jsonDict["Gravity"]
        self.minTemperature = jsonDict["minTemp"]
        self.maxTemperature = jsonDict["maxTemp"]

class emptyBody(Body):
    def __init__(self):
        self.name = ''
        self.id = 0
        self.systemName = ''
        self.systemId = 0
        self.biologicalCount = BioType.Aleoida
        self.parentStar = Starclass.A
        self.planetType = PlanetType.Rock
        self.atmossphericComposition = AtmossphericComposition.Any
        self.volcamismType = VolcanismType.Any
        self.atmosphericPressure = AtmossphericComposition.Any
        self.gravity = 0
        self.minTemperature = 0
        self.maxTemperature = 1