from Room import *
from Player import *

class BossTile(Tile):
    # Boss states: 0 - idle, 1 - charge, 2 - attack, 3 - dead
    bossState = 0
