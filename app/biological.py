from enums import Starclass, PlanetType, AtmossphericComposition, VolcamismType, BioType
from body import Body

class Biological:

    mainType: BioType
    subType: str
    value: int

    # Predictors
    starclasses: list[Starclass]
    planetTypes: list[PlanetType]
    atmossphericCompositions: list[AtmossphericComposition]
    volcanismTypes: list[VolcamismType]
    minAtmosphericPressure: float
    maxAtmosphericPressure: float
    minGravity: float
    maxGravity: float
    minTemperature: float
    maxTemperature: float
    likelyhood: int #likely hood


    def __init__(self, mainType: BioType, subType: str, value: int, starclasses: list[Starclass], planetTypes: list[PlanetType], 
                 atmossphericCompositions: list[AtmossphericComposition], volcanismTypes: list[VolcamismType], 
                 minAtmosphericPressure: float, maxAtmosphericPressure: float, 
                 minGravity: float, maxGravity: float, minTemperature: float, maxTemperature: float):
        self.mainType = mainType
        self.subType = subType
        self.value = value
        
        self.starclasses = starclasses
        self.planetTypes = planetTypes
        self.atmossphericCompositions = atmossphericCompositions
        self.volcanismTypes = volcanismTypes
        self.minAtmosphericPressure = minAtmosphericPressure
        self.maxAtmosphericPressure = maxAtmosphericPressure
        self.minGravity = minGravity
        self.maxGravity = maxGravity
        self.minTemperature = minTemperature
        self.maxTemperature = maxTemperature


    def presence_possible(self, body: Body):
        if (not body.parentStar in self.starclasses and 
            not body.planetType in self.planetTypes and
            not body.atmossphericComposition in self.atmossphericCompositions and
            not body.volcamismType in self.volcanismTypes and 
            not body.atmosphericPressure >= self.minAtmosphericPressure and 
            not body.atmosphericPressure <= self.maxAtmosphericPressure and 
            not body.gravity >= self.minGravity and 
            not body.gravity <= self.maxGravity and
            not body.minTemperature >= self.minTemperature and 
            not body.maxTemperature <= self.maxTemperature):
            # TODO reorder in importance of variable
            return False
        else: 
            return True