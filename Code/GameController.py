from gamegrid import *
import class_definitions as cd
import levels
from time import sleep
import Player as player
import java.util.ConcurrentModificationException as CME #Yes, you are able to import java definitions because jython is a java application
LevelProgress = 0
TotalCoins = 0

def doIntroduction():
    print "Welcome to skater danger."
    sleep(2)
    print "You can move your character with the A, D and Space keys."
    sleep(2)
    print "Your goal is to reach the golden pressure plate."
    sleep(2)
    print "Also try to collect as many coins as possible."
    sleep(2)
    print "But be careful. Not every ground tile is perfectly steady..."
    sleep(2)
    print "If you want to restart a level, then there will always be a way into the void for you..."
    sleep(2)

def getInputs(Player):
    if isKeyPressed(65): #A-Key
        Player.inputs[0] = True
    else:
        Player.inputs[0] = False
    if isKeyPressed(68):#D-Key
        Player.inputs[1] = True
    else:
        Player.inputs[1] = False
    if isKeyPressed(32): #Space-Bar
        Player.inputs[2] = True
    else:
        Player.inputs[2] = False

#----------------------<Tiles>------------------------
        
def spawnTiles(tiles,Player):#Goes through the list and spawns the tiles with their respective parameters
    for tile in tiles:
        newTile = cd.GroundTile(tile[0],tile[1],tile[2])
        addActor(newTile,tile[0])
        Player.addCollisionActor(newTile)
        
def despawnTiles(tiles): #Goes through the list and removes the tiles in the list
    for tile in tiles:
        removeActorsAt(tile[0])

def flashTile(tile,hideTile,spawnPos): #Gets called by tiles with the flashing parameter every time a flashing cycle has passed
    if hideTile:
        tile.setLocation(Location(-100,-100))
    else:
        tile.setLocation(spawnPos)
        
#---------------------</Tiles>---------------------------
def startGame():
    determinLevel(LevelProgress)

def determinLevel(LevelProgress):
    if LevelProgress == 0: #if - tower of doom
        levelLoader(levels.level_0)
    if LevelProgress == 1:
        levelLoader(levels.level_1)
    if LevelProgress == 2:
        levelLoader(levels.level_2)
    if LevelProgress == 3:
        levelLoader(levels.level_3)
    if LevelProgress == 4:
        win()

def levelLoader(level):
    global LevelProgress,TotalCoins
    removeAllActors()
    setTitle("Skater Danger")
    addActor(cd.Background(),Location(300,300))
    
    doPause()
    Player = player.Player()
    Player.addActorCollisionListener(cd.PlayerCL()) #Builds the level
    addActor(Player,level[0])
    spawnTiles(level[1],Player)
    spawnCoins(level[2],Player)
    spawnPressurePlates(level[3],Player)   
    doRun()
    
    while not isDisposed():#Main loop
        try:
            getInputs(Player)
        except CME: #I'm oddly proud of this try-except clause...
            pass
            
        if Player.isDead: #Restart the level if the player has died
            levelLoader(level)
        if Player.hasWon: #Advance to the next level when the player has won
            LevelProgress += 1
            TotalCoins += Player.CoinsCollected
            determinLevel(LevelProgress)
            
def win():
    removeAllActors()
    sleep(2)
    setTitle("You collected " + str(TotalCoins) + " out of 8 Coins")
    addActor(cd.Credits(),Location(300,300))

def spawnCoins(coins,Player):
    for coin in coins:
        newCoin = cd.Coin()
        addActor(newCoin,coin) #coin is just: Location(x,y)
        newCoin.addActorCollisionListener(cd.CoinPlayerCL())
        newCoin.addCollisionActor(Player) #Register the Player as the collison partner
        
def spawnPressurePlates(PressurePlates,Player):
    for PressurePlate in PressurePlates:
        newPressurePlate = cd.PressurePlate(PressurePlate[1],PressurePlate[2],Player,PressurePlate[3])#Pressure Plate needs the parameters: TilesToSpawn, TilesToDespawn and Player to register it as a collision partner with the tiles the Pressure Plate spawns
        newPressurePlate.addActorCollisionListener(cd.PressurePlatePlayerCL())
        newPressurePlate.addCollisionActor(Player)
        addActor(newPressurePlate,PressurePlate[0])