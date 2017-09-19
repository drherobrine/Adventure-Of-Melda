class Tile:

    def isAccessible(self):
        return self.accessible
    def getName(self):
        return self.name
    def getText(self):
        return self.text
    def getEncounterPossibility(self):
        return self.encounterPossibility
    def getEncounterableEnemies(self):
        return self.encounterableEnemies
    def __init__(self, accessible, name, text, encounterPossibility, encounterableEnemies):
        self.accessible = accessible
        self.name = name
        self.text = text
        self.encounterPossibility = encounterPossibility
        self.encounterableEnemies = []
