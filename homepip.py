import pygame, sys
from pygame.locals import *
pygame.init()
screenW=1000
screenH=1000
screen = pygame.display.set_mode((screenW, screenH))
pygame.display.set_caption("St Nick's Escape")
colorBlack = (0,0,0)
colorRed = (255,0,0)
colorBlue = (0,0,255)
colorGreen = (0,255,0)
ColorCyan = (0,255,255)
currentColor = colorBlack
detected = False
player = pygame.Rect((10,10,50,50))
eRect = pygame.Rect((200,200,50,50))
tRect = pygame.Rect((200,175,300,50))
e2Rect = pygame.Rect((350,350,50,50))
t2Rect = pygame.Rect((20,340,300,50))
winRect = pygame.Rect((500,500,50,10))
def UpDownLeftRight():

    if key[pygame.K_LEFT]:
        player.x-=1
        
    if key[pygame.K_RIGHT]:
        player.x+=1
    if key[pygame.K_UP]:
        player.y-=1
    if key[pygame.K_DOWN]:
        player.y+=1
def boundaries():
 
    if player.x<0:
        player.x=0
    if player.y<0:
        player.y=0
    if player.x>screenW-player.width:
        player.x=screenW-player.width
    if player.y>screenH-player.height:
        player.y= screenH-player.height
running = True
while running ==True:
    screen.fill(colorBlack)
    key = pygame.key.get_pressed()
    UpDownLeftRight()
    boundaries()
    currentColor = colorGreen
    if player.colliderect(tRect):
        currentColor = colorRed
        print('ouch')
        caught = 1
    if player.colliderect(t2Rect):
        currentColor = colorRed
        print('that must have hurt')
        caught = 1
    if player.colliderect(winRect):
        currentColor = ColorCyan
        
            
        print("YOU WIN!!!!!")
        running = False
        
    origin = eRect.center
    point1 = (eRect.x+300,eRect.y-20)
    point2 = (eRect.x+300,eRect.y+20)
    origin2 = e2Rect.center
    point12 = (e2Rect.x-300,e2Rect.y+20)
    point22 = (e2Rect.x-300,e2Rect.y-20)


    pRect = pygame.Rect((player.x,player.y,player.width,player.height))
    pygame.draw.line(screen,ColorCyan, origin,point1,1)
    pygame.draw.line(screen,ColorCyan, point1,point2,1)
    pygame.draw.line(screen,ColorCyan, point2,origin,1)
    pygame.draw.line(screen,ColorCyan, origin2,point12,1)
    pygame.draw.line(screen,ColorCyan, point12,point22,1)
    pygame.draw.line(screen,ColorCyan, point22,origin2,1)
    pygame.draw.rect(screen,colorBlue, eRect)
    pygame.draw.rect(screen,colorBlue, e2Rect)
    pygame.draw.rect(screen,colorGreen, winRect)
    pygame.draw.rect(screen,currentColor, pRect)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    if key[pygame.K_ESCAPE]:
        running= False
        print("stop")
pygame.quit()