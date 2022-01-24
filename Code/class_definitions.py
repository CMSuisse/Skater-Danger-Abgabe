from gamegrid import *
import GameController as GC

            
class GroundTile(Actor):
    def __init__(self,spawnPos,isFlashing,flashPeriod):
        if isFlashing:
            Actor.__init__(self,"Artwork/Tile2.png")
            self.flashPeriod = flashPeriod
            self.isHidden = False
        else:
            Actor.__init__(self,"Artwork/Tile1.png")
        self.isFlashing = isFlashing
        self.spawnPos = spawnPos
            
    def act(self):
        if self.isFlashing: #Looks if the tile is even able to flash
            if self.nbCycles % self.flashPeriod == 0: #Determines if the tile should hide or come out of hiding
                if self.isHidden == False:
                    GC.flashTile(self,True,self.spawnPos)
                    self.isHidden = True
                else:
                    GC.flashTile(self,False,self.spawnPos)
                    self.isHidden = False
                    
class Coin(Actor):
    def __init__(self):
        Actor.__init__(self,("Artwork/Coin1.png","Artwork/Coin2.png","Artwork/Coin3.png","Artwork/Coin4.png","Artwork/Coin5.png","Artwork/Coin6.png","Artwork/Coin7.png","Artwork/Coin8.png","Artwork/Coin9.png","Artwork/Coin10.png",))
        self.AnimationStep = 0
        
    def act(self):
        if self.AnimationStep == 9: #Resets the animation
            self.AnimationStep = 0
        if self.nbCycles % 5 == 0: #Only shows the next step in the animation after 5 frames
            self.AnimationStep += 1
            self.show(self.AnimationStep)
        
class PressurePlate(Actor):
    def __init__(self,TilesToSpawn,TilesToDespawn,Player,isWinning):
        if isWinning:
            Actor.__init__(self,"Artwork/PressurePlateGolden.png")
        else:
            Actor.__init__(self,"Artwork/PressurePlate.png")
        self.TimesTriggered = 0
        self.TilesToSpawn = TilesToSpawn
        self.TilesToDespawn = TilesToDespawn
        self.isWinningPressurePlate = isWinning
        self.Player = Player #The terminology is a bit weird, but the code wouldn't know
        
    def act(self):
        if self.TimesTriggered == 1:
            GC.spawnTiles(self.TilesToSpawn,self.Player) #what to send here, since Player is only a global variable in the main.py file
            GC.despawnTiles(self.TilesToDespawn)
        
class Background(Actor):
    def __init__(self):
        Actor.__init__(self,"Artwork/CityBg.png")

class Credits(Actor):
    def __init__(self):
        Actor.__init__(self,("Artwork/Credits/Credits1.png","Artwork/Credits/Credits2.png","Artwork/Credits/Credits3.png","Artwork/Credits/Credits4.png","Artwork/Credits/Credits5.png","Artwork/Credits/Credits6.png","Artwork/Credits/Credits7.png"))
        self.step = 0
        
    def act(self):
        if self.nbCycles % 250 == 0 and not self.step == 6 and not self.nbCycles == 0:
            self.step += 1
        self.show(self.step)
        
#------------------Collision Listeners----------------------
class PlayerCL(GGActorCollisionListener):
    def collide(self,actor1,actor2):
        actor1.isGrounded = True
        return 1
    
class CoinPlayerCL(GGActorCollisionListener):
    def collide(self,actor1,actor2):
        removeActor(actor1)
        actor2.CoinsCollected += 1
        setTitle("Points: " + str(actor2.CoinsCollected))
        return 1
    
class PressurePlatePlayerCL(GGActorCollisionListener):
    def collide(self,actor1,actor2):
        actor1.TimesTriggered += 1
        if actor1.isWinningPressurePlate: #If the player has touched the golden pressure plate, load the next level
            actor2.hasWon = True
        return 1