from gamegrid import *
import GameController as GC

GC.doIntroduction()

thisGG = makeGameGrid(600,600,1,None,None,False) #Doing setup. BORING!
setSimulationPeriod(20)
show()

GC.startGame() #This is where the fun part begins