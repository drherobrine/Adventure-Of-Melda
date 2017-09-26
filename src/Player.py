class Player:
    def getAttack(self):
        return self.attack
    def getDefense(self):
        return self.defense
    def getHP(self):
        return self.HP
    def getPosX(self):
        return self.posX
    def getPosY(self):
        return self.posY
    def __init__(self, attack, defense, HP, posX, posY):
        self.attack = attack
        self.defense = defense
        self.HP = HP
        self.posX = posX
        self.posY = posY
