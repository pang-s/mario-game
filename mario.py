#Mario game created by Pang
import re
import pygame._view
import pygame
import random
import sys
from pygame.locals import*
   
# Define some colors 
black    = (   0,   0,   0) 
white    = ( 255, 255, 255) 
red      = ( 255,   0,   0)
green      = ( 0,   255,   0)
blue      = ( 0,   0,   255)
yellow      = ( 255,   255,   0)
TEXTCOLOR = white

#Terminate program
def terminate():
    pygame.quit()
    sys.exit()

#Waits for player to press key to continue
def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # pressing escape quits
                    terminate()
                return
            
#Draw text function           
def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

#Coin sprite
class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite. __init__(self)

        # Set height, width 
        self.image = pygame.image.load("images/coin.png")
   
        # Make top-left corner the passed-in location. 
        self.rect = self.image.get_rect() 
        self.rect.x = x
        self.rect.y = y

#Plant sprite     
class Plant(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite. __init__(self)

        # Set height, width 
        self.image = pygame.image.load("images/plant.png")
   
        # Make top-left corner the passed-in location. 
        self.rect = self.image.get_rect() 
        self.rect.x = x
        self.rect.y = y
        
# Platform sprite
class Platform (pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, color):
        pygame.sprite.Sprite.__init__(self)
 
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
# Player sprite
class Player(pygame.sprite.Sprite): 
   
    # -- Attributes 
    # Set speed vector of player
    change_x=0
    change_y=0
 
    # Triggered if the player wants to jump.
    jump_ready = False
 
    # Count of frames since the player hit 'jump' and we
    # collided against something. Used to prevent jumping
    # when we haven't hit anything.
    frame_since_collision = 0
    frame_since_jump = 0
     
    # -- Methods 
    # Constructor function 
    def __init__(self,x,y): 
        # Call the parent's constructor 
        pygame.sprite.Sprite.__init__(self) 
           
        # Set height, width 
        self.image = pygame.image.load("images/mario.png")
   
        # Make top-left corner the passed-in location. 
        self.rect = self.image.get_rect() 
        self.rect.x = x
        self.rect.y = y
       
    # Change the speed of the player 
    def changespeed_x(self,x):
        self.change_x = x
 
    def changespeed_y(self,y):
        self.change_y = y
           
    # Find a new position for the player 
    def update(self,blocks): 
 
        # Save the old x position, update, and see if player collided.
        old_x = self.rect.x
        new_x = old_x + self.change_x
        self.rect.x = new_x
 
        collide = pygame.sprite.spritecollide (self, blocks, False)
        if collide:
            # Player collided, go back to the old pre-collision location
            self.rect.x = old_x
 
        # Save the old y position, update, and see if we collided.
        old_y = self.rect.y 
        new_y = old_y + self.change_y 
        self.rect.y = new_y
         
        block_hit_list = pygame.sprite.spritecollide(self, blocks, False) 
 
        for block in block_hit_list:
            # Player collided. Set the old pre-collision location.
            self.rect.y = old_y
            self.rect.x = old_x
 
            # Stop player vertical movement
            self.change_y = 0
 
            # Start counting frames since player hit something
            self.frame_since_collision = 0
 
        # If the player recently asked to jump, and have recently
        # had ground under his feet, go ahead and change the velocity
        # to send player upwards
        if self.frame_since_collision < 6 and self.frame_since_jump < 6:
            self.frame_since_jump = 100
            self.change_y -= 8
 
        # Increment frame counters
        self.frame_since_collision+=1
        self.frame_since_jump+=1
 
    # Calculate effect of gravity.
    def calc_grav(self):
        self.change_y += .35
 
        # See if we are on the ground.
        if self.rect.y >= 485 and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = 485
            self.frame_since_collision = 0
 
    # Called when user hits 'jump' button
    def jump(self,blocks):
        self.jump_ready = True
        self.frame_since_jump = 0
         
pygame.init() 
    
# Set the height and width of the screen
SCREENWIDTH = 900
SCREENHEIGHT = 600
size=[SCREENWIDTH,SCREENHEIGHT] 
screen=pygame.display.set_mode(size) 
   
pygame.display.set_caption("Mario") 
 
# Create platforms
def create_level1():

    block_list = pygame.sprite.Group()
    #list of platform
    blocks = [ [900,90,0,560,green],
              [100,20,200,465,white],
              [100,20,400,410,white],
              [100,20,600,350,white],
              [100,20,800,290,white]
            ]
     
    # Loop through the list. Create the platform, add it to the list
    for item in blocks:
        block=Platform(item[0],item[1],item[2],item[3],item[4])
 
        block_list.add(block)

    
    #list of coins
    coins = [ [200,410],
              [400,355],
              [600,295],
              [800,235],
              [800,500]
            ]
     
    # Loop through the list. Create coins, add it to the list
    for item in coins:
        coin=Coin(item[0],item[1])
 
        level1coin_list.add(coin)

    #list of plants
    plants = [ [0,460],
            ]
     
    # Loop through the list. Create plants, add it to the list
    for item in plants:
        plant=Plant(item[0],item[1])
 
        level1plant_list.add(plant)
        

    return block_list

def create_level2():

    block_list = pygame.sprite.Group()
    #list of platforms
    blocks = [ [900,90,0,560,green],
              [100,20,200,465,white],
              [100,20,400,400,white],
              [100,20,150,340,white],
              [100,20,500,290,white],
              [100,20,800,290,white]
            ]
     
    # Loop through the list. Create the platform, add it to the list
    for item in blocks:
        block=Platform(item[0],item[1],item[2],item[3],item[4])
 
        block_list.add(block)

    
    #list of coins
    coins = [ [200,410],
              [400,345],
              [150,285],
              [500,235],
              [670,100]
            ]
     
    # Loop through the list. Create coins, add it to the list
    for item in coins:
        coin=Coin(item[0],item[1])
 
        level2coin_list.add(coin)

    #list of plants
    plants = [ [350,460],
              [670,460]
            ]
     
    # Loop through the list. Create plants, add it to the list
    for item in plants:
        plant=Plant(item[0],item[1])
 
        level2plant_list.add(plant)
        
    return block_list

def create_level3():

    block_list = pygame.sprite.Group()
    #list of platforms
    blocks = [ [900,90,0,560,green],
              [50,20,200,465,white],
              [50,20,600,315,white],
              [100,20,300,250,white],
              [50,20,400,390,white],
              [100,20,100,170,white],
              [100,20,800,290,white]
            ]
     
    # Loop through the list. Create platform, add it to the list
    for item in blocks:
        block=Platform(item[0],item[1],item[2],item[3],item[4])
 
        block_list.add(block)

    #list of coins
    coins = [ [200,410],
              [600,260],
              [300,195],
              [400,335],
              [100,115]
            ]
     
    # Loop through the list. Create coins, add it to the list
    for item in coins:
        coin=Coin(item[0],item[1])
 
        level3coin_list.add(coin)

#list of plants
    plants = [ [350,460],
               [450,460],
              [550,460]
            ]
     
    # Loop through the list. Create plants, add it to the list
    for item in plants:
        plant=Plant(item[0],item[1])
 
        level3plant_list.add(plant)
        
    return block_list


def create_level4():

    block_list = pygame.sprite.Group()
    #list of platforms
    blocks = [ [900,90,0,560,green],
              [100,20,100,465,white],
              [50,20,400,380,white],
              [50,20,100,320,white],
              [50,20,400,260,white],
              [100,20,700,370,white],
              [100,20,800,290,white]
            ]
     
    # Loop through the list. Create platforms, add it to the list
    for item in blocks:
        block=Platform(item[0],item[1],item[2],item[3],item[4])
 
        block_list.add(block)

    #list of coins
    coins = [ [100,410],
              [400,325],
              [100,265],
              [400,205],
              [700,315]
            ]
     
    # Loop through the list. Create the coins, add it to the list
    for item in coins:
        coin=Coin(item[0],item[1])
 
        level4coin_list.add(coin)


#list of plants
    plants = [ [250,460],
               [450,460],
               [550,460],
              [650,460]
            ]
     
    # Loop through the list. Create the plants, add it to the list
    for item in plants:
        plant=Plant(item[0],item[1])
 
        level4plant_list.add(plant)
        
    return block_list

def create_level5():

    block_list = pygame.sprite.Group()
    #list of platforms
    blocks = [ [900,90,0,560,green],
              [50,20,0,465,white],
              [50,20,200,400,white],
              [50,20,0,340,white],
              [50,20,200,280,white],
              [50,20,500,290,white],
              [100,20,800,290,white]
            ]
     
    # Loop through the list. Create the platform, add it to the list
    for item in blocks:
        block=Platform(item[0],item[1],item[2],item[3],item[4])
 
        block_list.add(block)

    #list of coins
    coins = [ [0,410],
              [200,345],
              [0,285],
              [200,225],
              [500,235]
            ]
     
    # Loop through the list. Create the coins, add it to the list
    for item in coins:
        coin=Coin(item[0],item[1])
 
        level5coin_list.add(coin)

    #list of plants
    plants = [ [200,460],
               [400,460],
               [600,460],
               [800,460],
            ]
     
    # Loop through the list. Create the platforms, add it to the list
    for item in plants:
        plant=Plant(item[0],item[1])
 
        level5plant_list.add(plant)
        
    return block_list

# Main program

playerRight = pygame.image.load("images/mario.png")
playerLeft = pygame.transform.flip(playerRight, True, False)
 
# The font we use to draw text on the screen (size 27)
font = pygame.font.SysFont('OCR A EXTENDED', 27)
   
# Used to manage how fast the screen updates 
clock=pygame.time.Clock()

# show the "Start" screen
drawText('Mario', font, screen, (SCREENWIDTH/2), (SCREENHEIGHT / 2) - 50)
drawText('Press a key to start.', font, screen, (SCREENWIDTH / 2), (SCREENHEIGHT / 2) + 50)
pygame.display.update()
waitForPlayerToPressKey()
   
# -------- Main Program Loop ----------- 
while True:
    #set up
    player = Player(20, 15)
    player.rect.x = 100
    player.rect.y = 550

    all_sprites_list = pygame.sprite.Group()
    
    level1coin_list = pygame.sprite.Group()
    level2coin_list = pygame.sprite.Group()
    level3coin_list = pygame.sprite.Group()
    level4coin_list = pygame.sprite.Group()
    level5coin_list = pygame.sprite.Group()

    level1plant_list = pygame.sprite.Group()
    level2plant_list = pygame.sprite.Group()
    level3plant_list = pygame.sprite.Group()
    level4plant_list = pygame.sprite.Group()
    level5plant_list = pygame.sprite.Group()

    all_sprites_list.add(player)
    
    current_room = 1
    coin_list = level1coin_list
    plant_list = level1plant_list
    block_list = create_level1()

    score = 0
    lives = 3
    
    while True: #the game loop runs while the game part is playing
        
        for event in pygame.event.get(): # User did something 
            if event.type == QUIT: # If user clicked close 
                terminate()
     
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed_x(-6)
                    player.image = playerLeft
                if event.key == pygame.K_RIGHT:
                    player.changespeed_x(6)
                    player.image = playerRight
                if event.key == pygame.K_SPACE:
                    player.jump(block_list)
                if event.key == pygame.K_DOWN:
                    player.changespeed_y(6)
                     
            if event.type == pygame.KEYUP: 
                if event.key == pygame.K_LEFT: 
                    player.changespeed_x(-0)
                if event.key == pygame.K_RIGHT: 
                    player.changespeed_x(0)

        # Stop player around the screen if they go too far left/right
        if player.rect.x >= SCREENWIDTH - 70:
            player.rect.x = SCREENWIDTH - 70
     
        if player.rect.x <= 0:
            player.rect.x = 0

        #Coin collision
        coins_hit_list = pygame.sprite.spritecollide(player, coin_list, True)  
             
        # Check the list of coin collisions and change score
        for coin in coins_hit_list:
            score +=4

        #Plant collision
        plants_hit_list = pygame.sprite.spritecollide(player, plant_list, True)  
             
        # Check the list of plant collisions and lose lives
        for plant in plants_hit_list:
            lives -=1

        if lives < 0:
            break

        #Changing levels through doors    
        player.update(block_list)
        if 900 > player.rect.x > 820 and 300 > player.rect.y > 190:
            if current_room == 1:
                block_list = create_level2()
                coin_list = level2coin_list
                plant_list = level2plant_list
                current_room = 2
                player.rect.x = 100
                player.rect.y = 550
            
            elif current_room == 2:
                block_list = create_level3()
                coin_list = level3coin_list
                plant_list = level3plant_list
                current_room = 3
                player.rect.x = 100
                player.rect.y = 550

            elif current_room == 3:
                block_list = create_level4()
                coin_list = level4coin_list
                plant_list = level4plant_list
                current_room = 4
                player.rect.x = 100
                player.rect.y = 550

            elif current_room == 4:
                block_list = create_level5()
                coin_list = level5coin_list
                plant_list = level5plant_list
                current_room = 5
                player.rect.x = 100
                player.rect.y = 550
                
            elif current_room == 5:
                break

        #Calculate gravity
        player.calc_grav()
         
        # Set the screen background 
        screen.fill(black)
       
        # ALL CODE TO DRAW BELOW THIS COMMENT
        pygame.draw.rect(screen, blue, [830, 200, 50, 100],4)
        all_sprites_list.draw(screen)
        block_list.draw(screen)
        coin_list.draw(screen)
        plant_list.draw(screen)
        drawText("Level: " + str(current_room), font, screen, 90, 30)
        drawText("Score: " + str(score), font, screen, 800, 30)
        drawText("Lives: " + str(lives), font, screen, 800, 80)
        # ALL CODE TO DRAW ABOVE THIS COMMENT 
           
        # Limit to 20 frames per second 
        clock.tick(40) 
       
        # update the screen with what we've drawn. 
        pygame.display.flip() 

    #stop the game and show game over screen

    screen.fill(black)
    drawText("Score: " + str(score), font, screen, 800, 30)
    drawText('Press a key to play again.', font, screen, (SCREENWIDTH / 2), (SCREENHEIGHT / 2))
    pygame.display.update()
    waitForPlayerToPressKey()
