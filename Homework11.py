import pygame, sys
from pygame.locals import *
import time
pygame.init()
pygame.mixer.init()
font = pygame.font.SysFont(None, 50)
found = pygame.mixer.Sound('over-there.mp3')
win = pygame.mixer.Sound("you-win-sfx-442128.mp3")

pygame.mixer.music.load('90s-game-music-no-copyright-352850 (1).mp3')
pygame.mixer.music.play(-1)
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
follow = pygame.Rect((100,100,50,50))
eRect = pygame.Rect((200,200,50,50))
tRect = pygame.Rect((200,175,300,50))
e2Rect = pygame.Rect((350,350,50,50))
t2Rect = pygame.Rect((20,340,300,50))
winRect = pygame.Rect((500,500,50,100))
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
num = 1
num2 = 1
while running ==True:
    eRect.x = eRect.x +num
    tRect.x = tRect.x +num
    e2Rect.x = e2Rect.x +num2
    t2Rect.x = t2Rect.x +num2
    if eRect.x > (400):
        num = -3
        num2 = -1
    if eRect.x < (100):
        num = 3
        num2 = 1

    screen.fill(colorBlack)


    key = pygame.key.get_pressed()
    UpDownLeftRight()

    follow.x = player.x - follow.x
    follow.y = player.y - follow.y
    boundaries()
    currentColor = colorGreen
    if player.colliderect(tRect):
        currentColor = colorRed
        print('ouch')
        if play ==1:
            play = 0
            found.play()
        caught = 1


    if player.colliderect(t2Rect):
        currentColor = colorRed
        print('that must have hurt')
        if play==1:
            found.play()
            play = 0
        caught = 1



    if player.colliderect(winRect):
        currentColor = ColorCyan
        win.play()
        time.sleep(2)
        print("YOU WIN!!!!!")
        running = False
    play = 1
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
    pygame.draw.rect(screen,colorRed, winRect)
    #pygame.draw.rect(screen,colorRed, follow)

    pygame.draw.rect(screen,currentColor, pRect)

    text = font.render("You are St Nick. You have to avoid the guards", True, (colorGreen))
    screen.blit(text, (50, 50))
    text = font.render("chimney", True, (colorRed))
    screen.blit(text, (400, 600))
    text = font.render("and get down the chimney.", True, (colorGreen))
    screen.blit(text, (50, 100))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    if key[pygame.K_ESCAPE]:
        running= False
        print("stop")
pygame.quit()
