import random
import time
from ./src/Tile import *
from ./src/Player import *
from ./src/Enemy import *
playerHP = 10
playerAtk = 1
playerDef = 1
playerX = 0
playerY = 0

def load():
    loadfile = open("save", "r"):#GO
    loadLines = loadfile.readlines().
    playerAtk = loadLines[0]
    playerDef = loadLines[1]
    playerHP = loadLines[2]
    playerX = loadLines[3]
    playerY = loadLines[4]
    loadLines.close()
def save():
    savefile = open("save", "w")
    savefile.truncate()
    savefile.write(playerAtk + "\n")
    savefile.write(playerDef + "\n")
    savefile.write(playerHP + "\n")
    savefile.write(playerX + "\n")
    savefile.write(playerY + "\n")
    savefile.close()

load()
PlayerInst = Player(playerAtk, playerDef, playerHP, playerX, playerY)

print("You are Kink. You are on a quest to rescue Princess Melda from a Mutant Ninja Turtle.")
time.sleep(2)
print("You have just washed up on the shore of the island with Melda's tower.")
time.sleep(1)
print("Now go on, save her!")

tiles = [[0 for x in range(5)] for x in range(5)]
tiles[0][0] = Tile(True, "Where you washed up", "You feel an invisible wall to the north and west. There is water to the south. Unfortunately, you are too dumb to wade.", False, [])
tiles[0][1] = Tile(False, "nope", "just no", False, [])
tiles[0][2] = Tile(False, "rly?", "ure 2 dum 2 wade", False, [])
tiles[0][3] = Tile(False, "u", "cant walk on water", False, [])
tiles[0][4] = Tile(False, "Dude.", "Just. PLAY FRKN NORMALLY!", False, [])
tiles[1][0] = Tile(True, "Beach north", "There still is an energy wall to the north. You see more beach to the south and grasslands to the east.", False, [])
tiles[1][1] = Tile(True, "Beach lower north", "The ocean is to the west. Grasslands to the east and sand to the north and south.", True, [])
tiles[1][2] = Tile(True, "Beach center", "You are in the middle of the beach. Grasslands to the east. Beach to the north and south. Ocean to the west.")
tiles[1][3] = Tile(True, "Beach upper south", "There is the ocean to the west. Grasslands to the east. You see a mountain in the distance. Beach to the north and south.")
tiles[1][4] = Tile(True, "Beach south", "Ocean to the west, beach to the north, grasslands to the east. There is an energy wall to the south.")
tiles[2][0] = Tile(True, "Grasslands", "There is an entrance to a particularly scary-looking tower to the east.")
tiles[2][1] = Tile(True, "Grasslands", "Nothing special.")
tiles[2][2] = Tile(True, "Grasslands", "Nothing special.")
tiles[2][3] = Tile(True, "Grasslands", "Mountain to the east.")
tiles[2][4] = Tile(True, "Grasslands", "Energy wall to the south")
tiles[3][0] = Tile(True, "Tower entrance", "The tower is to the east. You feel a chill down your spine.")
tiles[3][1] = Tile(True, "Grasslands", "Tower entrance to the north, tower wall to the east.")
tiles[3][2] = Tile(True, "Grasslands", "Mountain to the south.")
tiles[3][3] = Tile(False, "noclip", "noclip off")
tiles[3][4] = Tile(True, "Grasslands", "Energy wall to the south")
tiles[4][0] = BossTile(True, "Boss Fight", "You are ready.")
tiles[4][1] = Tile(False, "noclip", "noclip off")
tiles[4][2] = Tile(True, "Grasslands", "Nothing special.")
tiles[4][3] = Tile(True, "Grasslands", "Mountain to the west, energy wall to the east.")
tiles[4][4] = Tile(True, "Grasslands", "Energy wall to the west and south.")

while not dead:
