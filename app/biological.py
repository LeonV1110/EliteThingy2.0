from enums import Starclass, PlanetType, AtmossphericComposition, VolcanismType, BioType, list_enum_to_json
from body import Body

class Biological:

    mainType: BioType
    subType: str
    value: int

    # Predictors
    starclasses: list[Starclass]
    planetTypes: list[PlanetType]
    atmossphericCompositions: list[AtmossphericComposition]
    volcanismTypes: list[VolcanismType]
    minAtmosphericPressure: float
    maxAtmosphericPressure: float
    minGravity: float
    maxGravity: float
    minTemperature: float
    maxTemperature: float
    likelyhood: int #likely hood of subtype asuming maintype


    def __init__(self, mainType: BioType, subType: str, value: int, starclasses: list[Starclass], planetTypes: list[PlanetType], 
                 atmossphericCompositions: list[AtmossphericComposition], volcanismTypes: list[VolcanismType], 
                 minAtmosphericPressure: float, maxAtmosphericPressure: float, 
                 minGravity: float, maxGravity: float, minTemperature: float, maxTemperature: float, likelyhood: int):
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
        self.likelyhood = likelyhood


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
        
    def to_json(self):
        starclasses = list_enum_to_json(self.starclasses)
        planetTypes = list_enum_to_json(self.planetTypes)
        atmosComps = list_enum_to_json(self.atmossphericCompositions)
        volcanism = list_enum_to_json(self.volcanismTypes)

        return f'{{"MainType":  "{self.mainType._name_}", "SubType": "{self.subType}", "Value": {self.value}, "StarClasses": {starclasses}, "PlanetTypes": {planetTypes}, "AtmosComps": {atmosComps}, "VolcamismTypes": {volcanism}, "minAtmosPressure": {self.minAtmosphericPressure}, "maxAtmosPressure": {self.maxAtmosphericPressure}, "minGravity": {self.minGravity}, "maxGravity": {self.maxGravity}, "minTemp": {self.minTemperature}, "maxTemp": {self.maxTemperature}, "likelyhood": {self.likelyhood}}}'

class jsonBiological(Biological):
    def __init__(self, jsonDict: dict):
        self.mainType = BioType[jsonDict["MainType"]]
        self.subType = jsonDict["SubType"]
        self.value = jsonDict["Value"]
        
        self.starclasses = [Starclass[name] for name in jsonDict["StarClasses"]]
        self.planetTypes = [PlanetType[name] for name in jsonDict["PlanetTypes"]]
        self.atmossphericCompositions = [AtmossphericComposition[name] for name in jsonDict["AtmosComps"]]
        self.volcanismTypes = [VolcanismType[name] for name in jsonDict["VolcanismTypes"]]

        self.minAtmosphericPressure = jsonDict["minAtmosPressure"]
        self.maxAtmosphericPressure = jsonDict["maxAtmosPressure"]
        self.minGravity = jsonDict["minGravity"]
        self.maxGravity = jsonDict["maxGravity"]
        self.minTemperature = jsonDict["minTemp"]
        self.maxTemperature = jsonDict["maxTemp"]
        self.likelyhood = jsonDict["likelyhood"]