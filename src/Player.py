class Player:
    def getAttack(self):
        return self.attack
    def getDefense(self):
        return self.defense
    def getHP(self):
        return self.HP
    def __init__(self, attack, defense, HP):
        self.attack = attack
        self.defense = defense
        self.HP = HP
