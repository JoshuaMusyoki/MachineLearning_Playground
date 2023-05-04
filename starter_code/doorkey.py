import pygame
import sys
import random
import numpy as np
pygame.init()
pygame.font.init()
# init_game begins the board with 50 pixel squares 
#Height and width separated by 2 pixels are n*m squares 
def init_game(boardSize):
    global reward
    screen = pygame.display.set_mode(((52*boardSize[0])+2,(52*boardSize[1])+102))    
    screen.fill((96,96,96))
    for i in range (boardSize[0]):
        for ii in range (boardSize[1]):
            pygame.draw.rect(screen, (224,224,224),
                             (2+i*52,2+ii*52,50,50),0)
    font=pygame.font.SysFont("timesnewroman", 24)
    text = font.render("Score:" + str(reward), True, (255, 255, 255))
    text1 = font.render("Press X to exit or R to restart", True, (255, 255, 255))
    
    screen.blit(text,
        (150 - text.get_width() // 2, ((boardSize[1]*51)+50) - text.get_height() // 2))
    screen.blit(text1,
        (150 - text1.get_width() // 2, ((boardSize[1]*51)+80) - text1.get_height() // 2))
    pygame.display.update()
    return screen

# Agent draws the agent in the posX by posY possition

class Agent(pygame.sprite.Sprite):
    def __init__(self):
        global boardSize
        super().__init__()  #super calls the AGENT constructor
        # Set transparent background
        self.image= pygame.Surface([50,50])
        self.image.fill((0,0,255))
        self.image.set_colorkey((0,0,255))
        self.haveKey=False
        self.returnCurrentPos=(0,0)
        # Drawing
        #pygame.draw.rect(self.image,(150,255,100),(20,20,20,20))
        #pygame.draw.rect(self.image,(100,255,150),(0,0,20,20))
        pygame.draw.ellipse(self.image,(255,255,255),(5,12,40,26))
        pygame.draw.ellipse(self.image,(0,0,0),(4,11,42,28),2)
        pygame.draw.circle(self.image,(0,128,255),(16,25),4)
        pygame.draw.circle(self.image,(255,0,127),(34,25),4)
        pygame.draw.circle(self.image,(0,0,0),(16,25),1)
        pygame.draw.circle(self.image,(0,0,0),(34,25),1)
        pygame.draw.line(self.image,(0,0,0),(22,30),(28,30),2)
        
        # get rect will get all the objects in the rectangle as one
        self.rect = self.image.get_rect()
    def pos(self,posx,posy):
        self.rect.x=(2+(posx*52))
        self.rect.y=(2+(posy*52))
        self.returnCurrentPos=(posx,posy)
        
    def move(self,Action):
        if Action=="UP" and self.returnCurrentPos[1]>0:
            self.pos(self.returnCurrentPos[0],(self.returnCurrentPos[1]-1))
        elif Action=="DOWN" and self.returnCurrentPos[1]<(boardSize[1]-1):
            self.pos(self.returnCurrentPos[0],(self.returnCurrentPos[1]+1))
        elif Action=="LEFT" and self.returnCurrentPos[0]>0:
            self.pos(self.returnCurrentPos[0]-1,(self.returnCurrentPos[1]))
        elif Action=="RIGHT" and self.returnCurrentPos[0]<(boardSize[0]-1):
            self.pos(self.returnCurrentPos[0]+1,(self.returnCurrentPos[1]))
        else:
            print("Corrupt movement!")

class nail(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  #super calls the AGENT constructor
        self.image= pygame.Surface([50,50])
        self.image.fill((0,0,252))
        self.image.set_colorkey((0,0,252))
        self.reward=-50
        
        pygame.draw.lines(self.image,(0,0,0),True,((10,10),(40,10),(37,15),
                                      (28,15),(28,35),(25,40),(22,35),(22,15),
                                      (20,15),(13,15)),3)

        self.rect = self.image.get_rect()
    def pos(self,posx,posy):
        self.rect.x=(2+(posx*52))
        self.rect.y=(2+(posy*52))
        self.returnCurrentPos=(posx,posy)

class key(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  #super calls the AGENT constructor
        self.image= pygame.Surface([50,50])
        self.image.fill((0,0,252))
        self.image.set_colorkey((0,0,252))
        self.reward=1000
        
        
        pygame.draw.circle(self.image,(230,230,0),(25,13),10)
        pygame.draw.circle(self.image,(0,0,0),(25,13),10,2)
        pygame.draw.circle(self.image,(0,0,255),(25,13),5)
        pygame.draw.circle(self.image,(0,0,0),(25,12),5,1)
        pygame.draw.rect(self.image,(230,230,0),(22,21,6,22),0)
        pygame.draw.rect(self.image,(0,0,0),(22,21,6,22),2)
        pygame.draw.line(self.image,(0,0,0),(36,38),(28,38),4)
        pygame.draw.line(self.image,(0,0,0),(36,31),(28,31),4)
        self.rect = self.image.get_rect()
    def pos(self,posx,posy):
        self.rect.x=(2+(posx*52))
        self.rect.y=(2+(posy*52))
        self.returnCurrentPos=(posx,posy)
        
class door(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  #super calls the AGENT constructor
        self.image= pygame.Surface([50,50])
        self.image.fill((0,0,255))
        self.image.set_colorkey((0,0,255))
        self.reward=5000
        
#        pygame.draw.circle(self.image,(230,230,0),(25,13),10)
#        pygame.draw.circle(self.image,(0,0,0),(25,13),10,2)
#        pygame.draw.circle(self.image,(0,0,255),(25,13),5)

        pygame.draw.rect(self.image,(255,0,0),(13,8,24,34),0)
        pygame.draw.rect(self.image,(0,0,0),(13,8,24,34),2)
        pygame.draw.rect(self.image,(0,0,0),(18,12,14,10),1)
        pygame.draw.rect(self.image,(0,0,0),(18,28,14,10),1)
        pygame.draw.circle(self.image,(0,0,0),(32,25),2)
#        pygame.draw.rect(self.image,(0,0,0),(13,8,24,34),1)
        self.rect = self.image.get_rect()
    def pos(self,posx,posy):
        self.rect.x=(2+(posx*52))
        self.rect.y=(2+(posy*52))
        self.returnCurrentPos=(posx,posy)
def updateReward():
    global reward
    global playing

#    global KepPos
    global boardSize
    #moving reward
    reward+=-10
    refresh()
    #Nail position? 
    for i in range(len(NailsPos)):
        if not((agent.returnCurrentPos-NailsPos[i]).any()):
            reward+=-100
            refresh()
    if not((agent.returnCurrentPos-np.asarray(KEY.returnCurrentPos)).any()):
        reward+=1000
        agent.haveKey=True
        KEY.pos(boardSize[0]-1,boardSize[1])
        refresh()
        
    if (not((agent.returnCurrentPos-DoorPos).any()) and agent.haveKey):
        reward+=5000
        playing =False
        finishGame()
        
    return reward

def populateBoard():
    
    global boardSize
    global all_sprites_list
    all_sprites_list = pygame.sprite.Group()
    agent = Agent()
    agent.pos(random.randint(0,boardSize[0]-1),random.randint(0,boardSize[1]-1))
    all_sprites_list.add(agent)
    numbOnails=int(0.15*(boardSize[0]*boardSize[1]))
    keyPos=np.zeros(2)
    keyPos[0]=random.randint(0,boardSize[0]-1)
    keyPos[1]=random.randint(0,boardSize[1]-1)
    Key=key()
    Key.pos(keyPos[0],keyPos[1])
    all_sprites_list.add(Key)
    doorPos=np.zeros(2)
    doorPos[0]=random.randint(0,boardSize[0]-1)
    doorPos[1]=random.randint(0,boardSize[1]-1)
    Door=door()
    Door.pos(doorPos[0],doorPos[1])
    all_sprites_list.add(Door) 
    nailPos=np.zeros([numbOnails,2])
    for i in range(numbOnails):
        nailPos[i,0]=random.randint(0,boardSize[0]-1)
        nailPos[i,1]=random.randint(0,boardSize[1]-1)
        GenericNail=nail()
        GenericNail.pos(nailPos[i,0],nailPos[i,1])
        all_sprites_list.add(GenericNail) 
    return nailPos,doorPos,keyPos,Key,agent
def finishGame():
#    global all_sprites_list
#    print(all_sprites_list)
#    global agent
#    del agent
    global boardSize
    if playing==True:
        boardSize[0]=random.randint(9,30)
        boardSize[1]=random.randint(9,15)
        init_game(boardSize)
        refresh()
        global reward,NailsPos,DoorPos,KeyPos,KEY,agent
        
        reward=0
        NailsPos,DoorPos,KeyPos,KEY,agent=populateBoard()  
    
    else:
        screen.fill((96,96,255))
        font=pygame.font.SysFont("timesnewroman", 34)
        text = font.render("Score:" + str(reward), True, (255, 255, 255))
        text1 = font.render("Press X to exit or R to restart", True, (255, 255, 255))
        
        screen.blit(text,
            (((boardSize[0]*51)/2) - text.get_width() // 2, (((boardSize[1]*51)/2)-50) - text.get_height() // 2))
        screen.blit(text1,
            (((boardSize[0]*51)/2) - text1.get_width() // 2, ((boardSize[1]*51)/2) - text1.get_height() // 2))
        pygame.display.update()
    
    
    
    return True
reward=0
#key1=key()
#key1.pos(1,1) 
#Door1=door()
#Door1.pos(5,5)       

boardSize=[20,15]
  
screen=init_game(boardSize)
#all_sprites_list.add(Nail1)   
#all_sprites_list.add(key1)  
#all_sprites_list.add(Door1)   

NailsPos,DoorPos,KeyPos,KEY,agent=populateBoard()
def refresh():
    init_game(boardSize)
    all_sprites_list.update()
    all_sprites_list.draw(screen)
    pygame.display.flip()
#Enables the X cross for exit the window
refresh()
running = True
playing =True
counter=0
clock=pygame.time.Clock()
font=pygame.font.SysFont("timesnewroman", 32)
while running:
    
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT or keys[pygame.K_x]:
            running = False
            pygame.display.quit()
            pygame.quit()
            pygame.font.quit()
            sys.exit()
        if playing==True:
            if keys[pygame.K_LEFT]:
                agent.move("LEFT")
#                refresh()
                updateReward()
                
            if keys[pygame.K_RIGHT]:
                agent.move("RIGHT")
#                refresh()
                updateReward()
                
            if keys[pygame.K_UP]:
                agent.move("UP")
#                refresh()
                updateReward()
                
            if keys[pygame.K_DOWN]:
                agent.move("DOWN")
#                refresh()
                updateReward()
                
        if keys[pygame.K_r]:
            playing =True
            finishGame()
            refresh()

    clock.tick(30)