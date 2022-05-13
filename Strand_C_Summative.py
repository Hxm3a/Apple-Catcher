#import libraries
import pygame
import random as r
import time as t

#define colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
SKY = (204, 255, 255)

pygame.init()

#set up for screen
size = (800,400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Catch without a dad")

sButton = pygame.image.load("start.png")
rButton = pygame.image.load("restart.png")
eButton = pygame.image.load("exit.png")

#i used a video for reference to create Button class so credit goes to Coding with Russ, https://www.youtube.com/watch?v=G8MYGDf_9ho 
class button():
    def __init__ (self, x, y, image):
        self.clicked = False
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
    def draw(self):
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()
        
        #check if mouse is over buttons and if the buttons are clicked
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #draw the button onto the screen
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action
#create button instances
startButton = button(300,200, sButton)
exitButton = button(405,200, eButton)
restartButton = button(300,200, rButton)

class apples(object):
  def __init__(self):
    self.x = ""
    self.y = 50


def displayLives(lives):
  if lives == 3:
    screen.blit(fullheart.image,(665,0))
    screen.blit(fullheart.image,(710,0))
    screen.blit(fullheart.image,(755,0))
  elif lives == 2:
    screen.blit(fullheart.image,(665,0))
    screen.blit(fullheart.image,(710,0))
    screen.blit(bheart.image,(755,0))
  elif lives == 1:
    screen.blit(fullheart.image,(665,0))
    screen.blit(bheart.image,(710,0))
    screen.blit(bheart.image,(755,0))
  elif lives == 0:
    screen.blit(bheart.image,(665,0))
    screen.blit(bheart.image,(710,0))
    screen.blit(bheart.image,(755,0))

fullheart = pygame.sprite.Sprite()
fullheart.image = pygame.image.load("fullheart.png")

bheart = pygame.sprite.Sprite()
bheart.image = pygame.image.load("brokenheart.png")

floor = pygame.sprite.Sprite()
floor.image = pygame.image.load("floor (1).png")
floor.rect = floor.image.get_rect()
floor.rect.topleft = (0,300)

font = pygame.font.Font(None, 30)
tfont = pygame.font.Font(None, 70)

a1 = apples()
a1 = pygame.sprite.Sprite()
a1.image = pygame.image.load("apple1.png")
a1.rect = a1.image.get_rect()
a1.x = r.randint(20, 780)
a1.y = -50
print(a1.x)
movey = 0.1
velocityy = 0.1

b = pygame.sprite.Sprite()
b.image = pygame.image.load("basket (2).png")
b.rect = b.image.get_rect()
bx = 200
movex = 0

score = 0
stext = font.render(str(score), True, BLACK, SKY)
Stext = font.render("Score:", True, BLACK, SKY)
title = tfont.render("WELCOME TO APPLE CATCHER!", True, BLACK, SKY)
instructions = font.render("use the arrow keys to control the basket and catch apples!", True, BLACK, SKY)
lives = 3
gameStart = False
restart = False
highscore = 0
hightext = font.render("High Score:", True, BLACK, SKY)
hText = font.render(str(highscore), True, BLACK, SKY)


while True:
    screen.fill (SKY)
    screen.blit(title, (15,0))
    screen.blit(instructions, (100,100))
    event = pygame.event.poll()
    if startButton.draw():
        gameStart = True
        t.sleep(1)
        break
    if exitButton.draw():
        break
    pygame.display.flip()

while (gameStart):
  
  #fill screen to white
  screen.fill(SKY)
  #print(b.rect)
  #set the hitboxes of the sprites
  b.rect.topleft = (bx,200)
  a1.rect.topleft = (a1.x,a1.y)

  #blit the basket sprite
  screen.blit(b.image, (bx,200))
  #make the basket move
  bx = movex + bx

  #put floor, basket and apple onto the screen
  screen.blit(floor.image, (0,300))
  screen.blit(stext, (65,0))
  screen.blit(Stext, (0,0))
  screen.blit(hightext, (0,20))
  screen.blit(hText, (115,20))
  screen.blit(a1.image, (a1.x, a1.y))
  screen.blit(b.image, (bx,200))
  
  #get the apple to move
  a1.y = movey + a1.y
    
  displayLives(lives)

  if lives == -1:
        screen.fill(SKY)
        movey = 0
        if restartButton.draw():
            restart = True
            a1.y = -70
            bx = 200
        if exitButton.draw():
            gameStart = False
  if restart:
      movey = 0.1
      velocityy = 0.1
      t.sleep(2)
      a1.y = -70
      lives = 3
      if score > highscore:
          highscore = score
          hText = font.render(str(highscore), True, BLACK, SKY)
      score = 0
      stext = font.render(str(score), True, BLACK, SKY)
      restart = False


  #update the display
  pygame.display.flip()
  
  if score >= 9 and score <20:
      velocityy = 0.25
  elif score >= 20:
      velocityy = 0.5
 
  #check for events
  event = pygame.event.poll()
  
  if event.type == pygame.QUIT:
    break
  if event.type == pygame.KEYDOWN:
    if (event.key == (pygame.K_RIGHT)):
      movex = 1
    if event.key == (pygame.K_LEFT):
      movex = -1
  if event.type == pygame.KEYUP:
    movex = 0
  
  elif (pygame.sprite.collide_rect(a1, b)):
    a1.x = r.randint(20,750)
    movey = 0
    a1.y = -70
    movey = velocityy
    score += 1 
    print(score)
    stext = font.render(str(score), True, BLACK, SKY)
  if (pygame.sprite.collide_rect(a1, floor)):
    a1.x = r.randint(20,750)
    a1.y = -70
    lives -= 1
        
  pygame.display.flip()