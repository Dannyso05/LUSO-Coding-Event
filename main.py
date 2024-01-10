import pygame
import random
import sys

pygame.init()
myfont = pygame.font.SysFont("consolas", 30)

dice1= random.randint(1,6)

screen = pygame.display.set_mode((400, 400))
largerButton= pygame.Rect(145, 300, 50, 50)
smallerButton=pygame.Rect(205, 300, 50, 50)
bool=False
one = pygame.image.load("dice-six-faces-one.png")
two = pygame.image.load("dice-six-faces-two.png")
three = pygame.image.load("dice-six-faces-three.png")
four = pygame.image.load("dice-six-faces-four.png")
five = pygame.image.load("dice-six-faces-five.png")
six = pygame.image.load("dice-six-faces-six.png")

one = pygame.transform.scale(one, (200, 200))
two = pygame.transform.scale(two, (200, 200))
three = pygame.transform.scale(three, (200, 200))
four = pygame.transform.scale(four, (200, 200))
five= pygame.transform.scale(five, (200, 200))
six = pygame.transform.scale(six, (200, 200))
oldNumber=0;
points=0;
def draw():
  #  screen.blit(soccerBall, (ball.x, ball.y))
    pygame.draw.rect(screen, (173,216,230), (0, 0, 400, 400))
    pygame.draw.rect(screen, (255,0,0), (145, 300, 50, 50))
    pygame.draw.rect(screen, (255,0,0), (205, 300, 50, 50))

    number = myfont.render(str(dice1),True, (59, 65, 66))
    larger = myfont.render(">",True, (59, 65, 66))
    smaller = myfont.render("<",True, (59, 65, 66))
    point = myfont.render("Points: "+str(points),True, (59, 65, 66))
    screen.blit(number, (185, 15))
    screen.blit(larger, (160, 310))
    screen.blit(smaller, (220, 310))
    screen.blit(point, (230, 360))
    if (dice1==1):
      screen.blit(one, (100, 75))
    if (dice1==2):
      screen.blit(two, (100, 75))
    if (dice1==3):
      screen.blit(three, (100, 75))
    if (dice1==4):
      screen.blit(four, (100, 75))
    if (dice1==5):
      screen.blit(five, (100, 75))
    if (dice1==6):
      screen.blit(six, (100, 75))

while True:
  draw()
  pygame.display.update()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit() 
      sys.exit()
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
      pygame.quit()
      sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN:           
          if smallerButton.collidepoint(pygame.mouse.get_pos()):
             oldNumber=dice1
             dice1= random.randint(1,6)
             if (dice1<oldNumber):
               points=points+1
          elif largerButton.collidepoint(pygame.mouse.get_pos()):
             oldNumber=dice1
             dice1= random.randint(1,6)
             if (dice1>oldNumber):
               points=points+1