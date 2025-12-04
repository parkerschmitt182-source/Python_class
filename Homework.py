import pygame, sys
from pygame.locals import *
pygame.init()
screenW = 1000
screenH = 1000
screen = pygame.display.set_mode((screenW, screenH))
pygame.display.set_caption('myGame')
playerX = screenW/2
playerY = screenH/2
playerW = 50
playerH = 50
colorBlack = (0,0,0)
colorRed = (255,0,0)

Running = True
while Running==True:
	screen.fill(colorBlack)
	key = pygame.key.get_pressed()
	if key[pygame.K_LEFT]:
		playerX -= 0.5
	if key[pygame.K_RIGHT]:
		playerX += 0.5
	if key[pygame.K_UP]:
		playerY -= 0.5
	if key[pygame.K_DOWN]:
		playerY += 0.5
	if playerX<0:
		playerX=0
	if playerY<0:
		playerY = 0
	if playerX >screenW-playerW:
		playerX=screenW-playerW
	if playerY > screenH-playerH:
		playerY=screenH-playerH
	playerRect = pygame.Rect((playerX,playerY,playerW,playerH))
	pygame.draw.rect(screen,colorRed,playerRect)
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == QUIT:
			Running = False
	if key[pygame.K_ESCAPE]:
		Running = False
pygame.quit()
sys.exit()
		
		
