class Enemy:
    def getEnemyHP(self):
        return self.enemyHP
    def getEnemyName(self):
        return self.enemyName
    def getEnemyAttack(self):
        return self.enemyAttack
    def getEnemyDefense(self):
        return self.enemyDefense
    def __init__(self, enemyHP, enemyName, enemyAttack, enemyDefense):
        self.enemyHP = enemyHP
        self.enemyName = enemyName
        self.enemyAttack = enemyAttack
        self.enemyDefense = enemyDefense
