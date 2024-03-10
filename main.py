import pygame
import time
from pygame.locals import *

xmax=300
ymax=300
run=True                                    #loop variable
list=[[0,0,0],[0,0,0],[0,0,0]]              #list to store values of cells 
input=1
winner=5
click=False
again=Rect(xmax//2-80,ymax//2+50,165,40)
count=0

pygame.init()
screen=pygame.display.set_mode((xmax,ymax)) #setting up display
pygame.display.set_caption('TIC TAC TOE')   #caption provider

def linedrawer():                           #function to draw cell dividers
    for x in range(1,3):
        pygame.draw.line(screen,(0,0,0),(0,100*x),(xmax,100*x),5)
        pygame.draw.line(screen,(0,0,0),(100*x,0),(100*x,ymax),5)

def marker():                               #function to draw 0 or X in cells
    xl=0
    for x  in list:
        yl=0
        for y in x:
            if y==-1:
                pygame.draw.line(screen,(255,0,0),(xl* 100 + 15,yl*100+15),(xl * 100 +85,yl*100 +85),4) 
                pygame.draw.line(screen,(255,0,0),(xl*100 +15,yl * 100+85),(xl *100 +85 , yl*100+15),4)
            if y==1:
                pygame.draw.circle(screen,(0,0,255),(xl*100+50,yl*100+50),30,5)
            yl+=1
        xl+=1    

def winn():                                 #function to check winning condition and winner
    global winner
    y=0
    for x in list:
        if sum(x)==3:                       #function to check rows 
            winner=1
        if sum(x)==-3:
            winner=-1
        if list[0][y]+list[1][y]+list[2][y]==3: #function to check fields
            winner = 1
        if list[0][y]+list[1][y]+list[2][y]==-3:
            winner = -1
        y+=1
    if list[0][0]+list[1][1]+list[2][2] ==3 or list[0][2]+list[1][1]+list[2][0]==3:
        winner=1
    if list[0][0]+list[1][1]+list[2][2] ==-3 or list[0][2]+list[1][1]+list[2][0]==-3:
        winner=-1

def diswin(winner):                         #function to announce winner and ask to play again
    font=pygame.font.SysFont(None,40)
    if winner==1:
        text='Player 1 wins!'
        color=(0,0,255)
    if winner==-1:
        text='Player 2 wins!'
        color=(255,0,0)   
    image=font.render(text,True,color)
    pygame.draw.rect(screen,(255,255,255),(xmax//2-100,ymax//2-60,210,50))
    screen.blit(image,(xmax//2-90,ymax//2-50))
    text='Play Again'
    again=Rect(xmax//2-80,ymax//2+50,165,40)
    image=font.render(text,True,color)
    pygame.draw.rect(screen,(255,255,255),again)
    screen.blit(image,(xmax//2-70,ymax//2+57))


while run:                                  #main game loop
    screen.fill((102, 255, 255))
    linedrawer()
    for events in pygame.event.get():
        if events.type ==pygame.QUIT:
            run=False
        if winner == 5:
            if events.type==pygame.MOUSEBUTTONDOWN and click==False:
                click=True
            if events.type==pygame.MOUSEBUTTONUP and click==True :
                click=False
                pos=pygame.mouse.get_pos()
                xpos=pos[0]//100
                ypos=pos[1]//100
                if list[xpos][ypos]==0:
                    list[xpos][ypos]=input         
                    input*=-1
                    winn()
                    count+=1
    marker()         
    if winner!=5:
        diswin(winner)
        if events.type==pygame.MOUSEBUTTONDOWN and click==False:
                click=True
        if events.type==pygame.MOUSEBUTTONUP and click==True :
                click=False
                pos=pygame.mouse.get_pos()
                if again.collidepoint(pos):         #reseting main variables
                    list=[[0,0,0],[0,0,0],[0,0,0]]   
                    input=1
                    winner=5  
                    count=0
    
    if count==9 and winner==5:                                    #reseting main variables on draw condition
        font=pygame.font.SysFont(None,40)
        text='Draw!'
        image=font.render(text,True,(102, 255, 255))
        pygame.draw.rect(screen,(255,255,255),(xmax//2-50,ymax//2-60,100,45))
        screen.blit(image,(xmax//2-40,ymax//2-50))
        pygame.display.update()
        time.sleep(2)
        list=[[0,0,0],[0,0,0],[0,0,0]]  
        input=1
        winner=5  
        count=0
    pygame.display.update()
    

pygame.quit()
