from gamegrid import *

g = 1 #Gravitational constant g (irl: 9.8 m/s**2)

class Player(Actor):
    def __init__(self):
        Actor.__init__(self,("Artwork/PlayerRight.png","Artwork/PlayerLeft.png","Artwork/PlayerJumpRight.png","Artwork/PlayerJumpLeft.png"))
        self.speed = [0,0] #Initializing the speed values for player at 0,0 for the x and y speed
        self.inputs = [False,False,False] #Left,Right,Jump
        self.isDead = False
        self.isGrounded = False
        self.hasWon = False
        self.CoinsCollected = 0
        
    def act(self):
        if self.isGrounded == True:
            self.speed[1] = 0
        #----------------<Movement>-------------------
            if self.inputs[2]: #Is player jumping?
                self.speed[1] -= 8
            
        if self.inputs[0] and abs(self.speed[0]) <= 1: #Is player strafing left?
            self.speed[0] -= 1
        if self.inputs[1] and abs(self.speed[0]) <= 1: #Is player strafing right?
            self.speed[0] += 1
        if not self.inputs[0] and not self.inputs[1]:
            self.speed[0] = 0
            
            
        if self.speed[1] != 0:
            if abs(self.speed[0]) != self.speed[0]:
                self.show(3)
            else:
                self.show(2)
        else:
            if abs(self.speed[0]) != self.speed[0]:
                self.show(1)
            elif self.speed[0] != 0:
                self.show(0)
                
        self.setLocation(Location(self.getX()+self.speed[0],self.getY()+self.speed[1]))
        
        #--------------</Movement>--------------------------
        
        #--------------<Post-Frame>-------------------------

        if self.speed[1] <= 5 and not self.isGrounded: #Doin' the gravity
            self.speed[1] += g        
            
        if self.getY() > 650: #Checks, is the player dead or not?
            self.isDead = True
            removeActor(self)
        
        self.isGrounded = False
        
        #-------------</Post-Frame>-------------------------