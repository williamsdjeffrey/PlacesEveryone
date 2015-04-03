#!/usr/bin/python
import random, os
import time 
import sys
import pygame
from pygame.locals import *
from sys import exit
if not pygame.mixer: print "No sound system detected."
pygame.mixer.init(44100)
StartSound = pygame.mixer.Sound(os.path.join("sounds","shuffle.wav"))
ClickSound = pygame.mixer.Sound(os.path.join("sounds","click.wav"))
cardflipsound = pygame.mixer.Sound(os.path.join("sounds","cardflip.wav"))
cheersound = pygame.mixer.Sound(os.path.join("sounds","cheer.wav"))
youlose = pygame.mixer.Sound(os.path.join("sounds","gameover.wav"))
#Sound2 = pygame.mixer.music.load(os.path.join("sounds","shuffle.wav"))
background_image_filename = 'Image/blue.jpg'
iP_1c = 'Image/01c.gif'
iP_1d = 'Image/01d.gif'
iP_1h = 'Image/01h.gif'
iP_1s = 'Image/01s.gif'
iP_2c = 'Image/02c.gif'
iP_2d = 'Image/02d.gif'
iP_2h = 'Image/02h.gif'
iP_2s = 'Image/02s.gif'
iP_3c = 'Image/03c.gif'
iP_3d = 'Image/03d.gif'
iP_3h = 'Image/03h.gif'
iP_3s = 'Image/03s.gif'
iP_4c = 'Image/04c.gif'
iP_4d = 'Image/04d.gif'
iP_4h = 'Image/04h.gif'
iP_4s = 'Image/04s.gif'
iP_5c = 'Image/05c.gif'
iP_5d = 'Image/05d.gif'
iP_5h = 'Image/05h.gif'
iP_5s = 'Image/05s.gif'
iP_6c = 'Image/06c.gif'
iP_6d = 'Image/06d.gif'
iP_6h = 'Image/06h.gif'
iP_6s = 'Image/06s.gif'
iP_7c = 'Image/07c.gif'
iP_7d = 'Image/07d.gif'
iP_7h = 'Image/07h.gif'
iP_7s = 'Image/07s.gif'
iP_8c = 'Image/08c.gif'
iP_8d = 'Image/08d.gif'
iP_8h = 'Image/08h.gif'
iP_8s = 'Image/08s.gif'
iP_9c = 'Image/09c.gif'
iP_9d = 'Image/09d.gif'
iP_9h = 'Image/09h.gif'
iP_9s = 'Image/09s.gif'
iP_10c = 'Image/10c.gif'
iP_10d = 'Image/10d.gif'
iP_10h = 'Image/10h.gif'
iP_10s = 'Image/10s.gif'
iP_11c = 'Image/11c.gif'
iP_11d = 'Image/11d.gif'
iP_11h = 'Image/11h.gif'
iP_11s = 'Image/11s.gif'
iP_12c = 'Image/12c.gif'
iP_12d = 'Image/12d.gif'
iP_12h = 'Image/12h.gif'
iP_12s = 'Image/12s.gif'
iP_13c = 'Image/13c.gif'
iP_13d = 'Image/13d.gif'
iP_13h = 'Image/13h.gif'
iP_13s = 'Image/13s.gif'
iBack_Card = 'Image/back101.gif'
SCREEN_SIZE = (1600, 900) 
pygame.init()

source = pygame.mixer.Channel(0)
pygame.mixer.music.load(1)
pygame.display.set_icon(pygame.image.load("Image/simpybigtwo_default.png"))
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)#SCREEN_SIZE, FULLSCREEN, 32)
pygame.display.set_caption("Welcome to \"Places Everyone\" - The Newest Card Game on the Market")

background = pygame.image.load(background_image_filename).convert()
P_1c = pygame.image.load(iP_1c).convert()
P_1d = pygame.image.load(iP_1d).convert()
P_1h = pygame.image.load(iP_1h).convert()
P_1s = pygame.image.load(iP_1s).convert()
P_2c = pygame.image.load(iP_2c).convert()
P_2d = pygame.image.load(iP_2d).convert()
P_2h = pygame.image.load(iP_2h).convert()
P_2s = pygame.image.load(iP_2s).convert()
P_3c = pygame.image.load(iP_3c).convert()
P_3d = pygame.image.load(iP_3d).convert()
P_3h = pygame.image.load(iP_3h).convert()
P_3s = pygame.image.load(iP_3s).convert()
P_4c = pygame.image.load(iP_4c).convert()
P_4d = pygame.image.load(iP_4d).convert()
P_4h = pygame.image.load(iP_4h).convert()
P_4s = pygame.image.load(iP_4s).convert()
P_5c = pygame.image.load(iP_5c).convert()
P_5d = pygame.image.load(iP_5d).convert()
P_5h = pygame.image.load(iP_5h).convert()
P_5s = pygame.image.load(iP_5s).convert()
P_6c = pygame.image.load(iP_6c).convert()
P_6d = pygame.image.load(iP_6d).convert()
P_6h = pygame.image.load(iP_6h).convert()
P_6s = pygame.image.load(iP_6s).convert()
P_7c = pygame.image.load(iP_7c).convert()
P_7d = pygame.image.load(iP_7d).convert()
P_7h = pygame.image.load(iP_7h).convert()
P_7s = pygame.image.load(iP_7s).convert()
P_8c = pygame.image.load(iP_8c).convert()
P_8d = pygame.image.load(iP_8d).convert()
P_8h = pygame.image.load(iP_8h).convert()
P_8s = pygame.image.load(iP_8s).convert()
P_9c = pygame.image.load(iP_9c).convert()
P_9d = pygame.image.load(iP_9d).convert()
P_9h = pygame.image.load(iP_9h).convert()
P_9s = pygame.image.load(iP_9s).convert()
P_10c = pygame.image.load(iP_10c).convert()
P_10d = pygame.image.load(iP_10d).convert()
P_10h = pygame.image.load(iP_10h).convert()
P_10s = pygame.image.load(iP_10s).convert()
P_11c = pygame.image.load(iP_11c).convert()
P_11d = pygame.image.load(iP_11d).convert()
P_11h = pygame.image.load(iP_11h).convert()
P_11s = pygame.image.load(iP_11s).convert() 
P_12c = pygame.image.load(iP_12c).convert()
P_12d = pygame.image.load(iP_12d).convert()
P_12h = pygame.image.load(iP_12h).convert()
P_12s = pygame.image.load(iP_12s).convert() 
P_13c = pygame.image.load(iP_13c).convert()
P_13d = pygame.image.load(iP_13d).convert()
P_13h = pygame.image.load(iP_13h).convert()
P_13s = pygame.image.load(iP_13s).convert() 
Back_Card = pygame.image.load(iBack_Card).convert()
Back_Card90 = pygame.transform.rotate(Back_Card , 90)
Back_Cardn90 = pygame.transform.rotate(Back_Card , -90)

screen_width, screen_height = SCREEN_SIZE
laserfire=pygame.mixer.Sound("Sound\saucerexplode.WAV")
laserfire.set_volume(0.4)
soundcounter=0
laserfire.play()
def display_all():
    global player_card_x
    global player_card_rect
    global p3_card_x
    global p3_card_rect
    global display_card_x
    global DeckCounter
    global player_card_list
    fill_background()
    display_num_of_cards(player_card_list, num_of_card)
    display_p2_num_of_cards(p2_card_list, p2_num_of_card)
    display_p3_num_of_cards(p3_card_list, p3_num_of_card)
    display_p4_num_of_cards(p4_card_list, p4_num_of_card)
    screen.blit(Back_Card, (player_card_rect[0][0]-300, player_card_rect[0][1]-200))
    screen.blit(write("Deck"),(200,275))
    if DeckCounter>=0:
    	screen.blit(writenum(DeckCounter),(125,425))
    else:
    	screen.blit(write("0"),(125,425))
    screen.blit(write("cards remaining"),(150,425))
    screen.blit(write("Player 1"),(800,650))
    screen.blit(write("Player 2"),(400,60))
    screen.blit(write("Player 3"),(800,10))
    screen.blit(write("Player 4"),(1200,60))
    
def display_num_of_cards(list, num):
    for x in range(0, 5):
        screen.blit(Back_Card, (player_card_rect[x][0]+60*x+100, player_card_rect[x][1]))
    return
    
def display_p2_num_of_cards(list, num):#really player 4
    global chosenplace4
    global chosencard4
    global index4
    card = random.randint(0, 4)
    index4=card
    place = random.randint(1, 4)
    for x in range(0, 5):
	if turn_id==4:
		chosencard4=p2_card_list[card]
		chosenplace4=place
		if card==0:
			screen.blit(pygame.transform.rotate(num_to_cards(p2_card_list[0]),90),(p2_card_rect[x][0]-100,100+100*x))
			if x!=0:
				screen.blit(Back_Card90,(p2_card_rect[x][0]-100,100+100*x))
		if card==1:
			screen.blit(pygame.transform.rotate(num_to_cards(p2_card_list[1]),90),(p2_card_rect[x][0]-100,100+100*x))
			if x!=1:
				screen.blit(Back_Card90,(p2_card_rect[x][0]-100,100+100*x))
		if card==2:
			screen.blit(pygame.transform.rotate(num_to_cards(p2_card_list[2]),90),(p2_card_rect[x][0]-100,100+100*x))
			if x!=2:
				screen.blit(Back_Card90,(p2_card_rect[x][0]-100,100+100*x))
		if card==3:
			screen.blit(pygame.transform.rotate(num_to_cards(p2_card_list[3]),90),(p2_card_rect[x][0]-100,100+100*x))
			if x!=3:
				screen.blit(Back_Card90,(p2_card_rect[x][0]-100,100+100*x))
		if card==4:
			screen.blit(pygame.transform.rotate(num_to_cards(p2_card_list[4]),90),(p2_card_rect[x][0]-100,100+100*x))
			if x!=4:
				screen.blit(Back_Card90,(p2_card_rect[x][0]-100,100+100*x))		
	else:
		screen.blit(Back_Card90,(p2_card_rect[x][0]-100,100+100*x))
    return

def display_p3_num_of_cards(list, num):
    global chosenplace3
    global chosencard3
    global index3
    card = random.randint(0, 4)
    index3=card
    place = random.randint(1, 4)
    for x in range(0, 5):
	if turn_id==3:
		chosencard3=p3_card_list[card]
		chosenplace3=place
		if card==0:
			screen.blit(num_to_cards(p3_card_list[0]),(p3_card_rect[x][0]+60*x+100, p3_card_rect[x][1]))
			if x!=0:
				screen.blit(Back_Card, (p3_card_rect[x][0]+60*x+100, p3_card_rect[x][1]))
		if card==1:
			screen.blit(num_to_cards(p3_card_list[1]),(p3_card_rect[x][0]+60*x+100, p3_card_rect[x][1]))
			if x!=1:
				screen.blit(Back_Card, (p3_card_rect[x][0]+60*x+100, p3_card_rect[x][1]))
		if card==2:
			screen.blit(num_to_cards(p3_card_list[2]),(p3_card_rect[x][0]+60*x+100, p3_card_rect[x][1]))


			if x!=2:
				screen.blit(Back_Card, (p3_card_rect[x][0]+60*x+100, p3_card_rect[x][1]))
		if card==3:
			screen.blit(num_to_cards(p3_card_list[3]),(p3_card_rect[x][0]+60*x+100, p3_card_rect[x][1]))
			if x!=3:
				screen.blit(Back_Card, (p3_card_rect[x][0]+60*x+100, p3_card_rect[x][1]))
		if card==4:
			screen.blit(num_to_cards(p3_card_list[4]),(p3_card_rect[x][0]+60*x+100, p3_card_rect[x][1]))
			if x!=4:
				screen.blit(Back_Card, (p3_card_rect[x][0]+60*x+100, p3_card_rect[x][1]))
	else:
        	screen.blit(Back_Card, (p3_card_rect[x][0]+60*x+100, p3_card_rect[x][1]))
    return

def display_p4_num_of_cards(list, num):
    global chosenplace2
    global chosencard2
    global index2
    card = random.randint(0, 4)
    index2=card
    place = random.randint(1, 4)
    for x in range(0, 5):
	if turn_id==2:
		chosencard2=p4_card_list[card]
		chosenplace2=place
		if card==0:
			screen.blit(pygame.transform.rotate(num_to_cards(p4_card_list[0]),90),(p4_card_rect[x][0]+250, 100+100*x))
			if x!=0:
				screen.blit(Back_Cardn90, (p4_card_rect[x][0]+250, 100+100*x))
		if card==1:
			screen.blit(pygame.transform.rotate(num_to_cards(p4_card_list[1]),90),(p4_card_rect[x][0]+250, 100+100*x))
			if x!=1:
				screen.blit(Back_Cardn90, (p4_card_rect[x][0]+250, 100+100*x))
		if card==2:
			screen.blit(pygame.transform.rotate(num_to_cards(p4_card_list[2]),90),(p4_card_rect[x][0]+250, 100+100*x))
			if x!=2:
				screen.blit(Back_Cardn90, (p4_card_rect[x][0]+250, 100+100*x))
		if card==3:
			screen.blit(pygame.transform.rotate(num_to_cards(p4_card_list[3]),90),(p4_card_rect[x][0]+250, 100+100*x))
			if x!=3:
				screen.blit(Back_Cardn90, (p4_card_rect[x][0]+250, 100+100*x))
		if card==4:
			screen.blit(pygame.transform.rotate(num_to_cards(p4_card_list[4]),90),(p4_card_rect[x][0]+250, 100+100*x))
			if x!=4:
				screen.blit(Back_Cardn90, (p4_card_rect[x][0]+250, 100+100*x))
	else:
        	screen.blit(Back_Cardn90, (p4_card_rect[x][0]+250, 100+100*x))
    return

def ini_random_cards(p_card_list):
    global all_card_list
    for x in range(0, 5):
        start = random.randint(0, 51)
        i = start
        while i != -1 :
            if 0 == all_card_list[start]:
                if i != 0:
                    start += 1
                    start %= 52
                    i -= 1
                else:
                    break
            else:
                start += 1
                start %= 52
        all_card_list[start] = 1
        p_card_list[x] = start
    return p_card_list

def ini_random_cards2(p_card_list):
    global all_card_list
    for x in range(0, 32):
        start = random.randint(0, 51)
        i = start
        while i != -1 :
            if 0 == all_card_list[start]:
                if i != 0:
                    start += 1
                    start %= 52
                    i -= 1
                else:
                    break
            else:
                start += 1
                start %= 52
        all_card_list[start] = 1
        p_card_list[x] = start
    return p_card_list
        
def num_to_cards(num):
    if 0==num:
        return P_2s
    if 1==num:
        return P_2c
    if 2==num:
        return P_2h
    if 3==num:
        return P_2d
    if 4==num:
        return P_3s
    if 5==num:
        return P_3c 
    if 6==num:
        return P_3h
    if 7==num:
        return P_3d
    if 8==num:
        return P_4s
    if 9==num:
        return P_4c
    if 10==num:
        return P_4h
    if 11==num:
        return P_4d
    if 12==num:
        return P_5s
    if 13==num:
        return P_5c
    if 14==num:
        return P_5h
    if 15==num:
        return P_5d
    if 16==num:
        return P_6s
    if 17==num:
        return P_6c
    if 18==num:
        return P_6h
    if 19==num:
        return P_6d
    if 20==num:
        return P_7s
    if 21==num:
        return P_7c
    if 22==num:
        return P_7h
    if 23==num:
        return P_7d
    if 24==num:
        return P_8s
    if 25==num:
        return P_8c
    if 26==num:
        return P_8h
    if 27==num:
        return P_8d
    if 28==num:
        return P_9s
    if 29==num:
        return P_9c
    if 30==num:
        return P_9h
    if 31==num:
        return P_9d
    if 32==num:
        return P_10s
    if 33==num:
        return P_10c
    if 34==num:
        return P_10h
    if 35==num:
        return P_10d
    if 36==num:
        return P_11s
    if 37==num:
        return P_11c
    if 38==num:
        return P_11h
    if 39==num:
        return P_11d
    if 40==num:
        return P_12s
    if 41==num:
        return P_12c
    if 42==num:
        return P_12h
    if 43==num:
        return P_12d
    if 44==num:
        return P_13s
    if 45==num:
        return P_13c
    if 46==num:
        return P_13h
    if 47==num:
        return P_13d
    if 48==num:
        return P_1s
    if 49==num:
        return P_1c
    if 50==num:
        return P_1h
    if 51==num:
        return P_1d

def write(msg="pygame is cool", color= (255,255,255)):    
    #myfont = pygame.font.SysFont("None", 32) #To avoid py2exe error
    myfont = pygame.font.Font(None,30)
    mytext = myfont.render(msg, True, color)
    mytext = mytext.convert_alpha()
    return mytext 


def writenum(int=0, color= (255,255,255)):    
    #myfont = pygame.font.SysFont("None", 32) #To avoid py2exe error
    myfont = pygame.font.Font(None,30)
    mytext = myfont.render(str(int), True, color)
    mytext = mytext.convert_alpha()
    return mytext 
def writenum2(int=0, color= (255,0,0)):    
    #myfont = pygame.font.SysFont("None", 32) #To avoid py2exe error
    myfont = pygame.font.Font(None,30)
    mytext = myfont.render(str(int), True, color)
    mytext = mytext.convert_alpha()
    return mytext 

def write2(msg="pygame is cool", color= (255,0,0)):    
    #myfont = pygame.font.SysFont("None", 32) #To avoid py2exe error
    myfont = pygame.font.Font(None,30)
    mytext = myfont.render(msg, True, color)
    mytext = mytext.convert_alpha()
    return mytext  
def write3(msg="pygame is cool", color= (255,255,255)):    
    #myfont = pygame.font.SysFont("None", 32) #To avoid py2exe error
    myfont = pygame.font.Font(None,60)
    mytext = myfont.render(msg, True, color)
    mytext = mytext.convert_alpha()
    return mytext  
def write4(msg="pygame is cool", color= (255,255,255)):    
    #myfont = pygame.font.SysFont("None", 32) #To avoid py2exe error
    myfont = pygame.font.Font(None,40)
    mytext = myfont.render(msg, True, color)
    mytext = mytext.convert_alpha()
    return mytext   
def write5(msg="pygame is cool", color= (255,0,0)):    
    #myfont = pygame.font.SysFont("None", 32) #To avoid py2exe error
    myfont = pygame.font.Font(None,60)
    mytext = myfont.render(msg, True, color)
    mytext = mytext.convert_alpha()
    return mytext      

def fill_background():
    for y in range(0, screen_height, background.get_height()):
        for x in range(0, screen_width, background.get_width()):
            screen.blit(background, (x, y))
def DisplayScores(num):
	global Player1score
	global Player2score
	global Player3score
	global Player4score
	screen.blit(background, (0,0))
	screen.blit(write3("Lets See Who's Winning"),(600,100))
	if len(sys.argv) > 1:
		screen.blit(writenum2(sys.argv[1]),(300,200))
	else:
		screen.blit(write2('Player 1'),(300,200))
	screen.blit(write2("________"),(300,201))
	screen.blit(writenum(Player1score),(300,226))
	screen.blit(write2("Player 2"),(600,200))
	screen.blit(write2("________"),(600,201))
	screen.blit(writenum(Player2score),(600,226))
	screen.blit(write2("Player 3"),(900,200))
	screen.blit(write2("________"),(900,201))
	screen.blit(writenum(Player3score),(900,226))
	screen.blit(write2("Player 4"),(1200,200))
	screen.blit(write2("________"),(1200,201))
	screen.blit(writenum(Player4score),(1200,226))
	screen.blit(write5("Left Click Mouse to return to game"),(550,400))
	screen.blit(write5("Hit Space to review instructions"),(600,500))
	screen.blit(write5("Hit n to start a new game"),(650,600))
	
	pygame.display.update()
	BACK=True;
	while BACK==True:
		for event in pygame.event.get():
			if event.type== QUIT:
				exit()
			if event.type==MOUSEBUTTONDOWN:
				BACK=False
			if event.type==KEYDOWN:
				if event.key==K_n:
					newgame()
					BACK=False
				if event.key==K_SPACE:
					instructions(num)
					BACK=False
				else:
					BACK=False
	backtogame(num)
def DisplayEndGameScores():
	global Player1score
	global Player2score
	global Player3score
	global Player4score
	global winner
	tracker=0
	screen.blit(background, (0,0))
	screen.blit(write3("Lets See Who Won"),(600,100))
	if len(sys.argv) > 1:
		screen.blit(writenum2(sys.argv[1]),(300,200))
	else:
		screen.blit(write2('Player 1'),(300,200))	
	screen.blit(write2("________"),(300,201))
	screen.blit(writenum(Player1score),(300,226))
	screen.blit(write2("Player 2"),(600,200))
	screen.blit(write2("________"),(600,201))
	screen.blit(writenum(Player2score),(600,226))
	screen.blit(write2("Player 3"),(900,200))
	screen.blit(write2("________"),(900,201))
	screen.blit(writenum(Player3score),(900,226))
	screen.blit(write2("Player 4"),(1200,200))
	screen.blit(write2("________"),(1200,201))
	screen.blit(writenum(Player4score),(1200,226))
	screen.blit(write5("Press any key to start a new game"),(650,600))
	while tracker==0:
		if Player1score>Player2score and Player1score>Player3score and Player1score>Player4score:
			winner=1
			tracker=1
		if Player2score>Player1score and Player2score>Player3score and Player2score>Player4score:
			winner=2
			tracker=1
		if Player3score>Player1score and Player3score>Player1score and Player3score>Player4score:
			winner=3
			tracker=1
		if Player4score>Player1score and Player4score>Player2score and Player4score>Player3score:
			winner=4
			tracker=1
		if tracker==0:
			winner=extraround()
			tracker=1
	if winner==1:
		screen.blit(write2("Winner"),(300,251))
	if winner==2:
		screen.blit(write2("Winner"),(600,251))
	if winner==3:
		screen.blit(write2("Winner"),(900,251))
	if winner==4:
		screen.blit(write2("Winner"),(1200,251))
	pygame.display.update()
	BACK=True;
	while BACK==True:
		for event in pygame.event.get():
			if event.type== QUIT:
				exit()
			if event.type==MOUSEBUTTONDOWN:
				BACK=False
			if event.type==KEYDOWN:
				if event.key==K_n:
					BACK=False
				if event.key==K_SPACE:
					BACK=False
				else:
					BACK=False
	newgame()
def extraround():
	winner=1
	return winner
def backtogame(num):
	global index
	display_all()
	screen.blit(write2("Press Space to Review Instructions"),(10,10))
	screen.blit(write2("Press ESC to see who is winning"),(10,35))
	screen.blit(write2("Press n to start a new game"),(10,60))
	pygame.display.update()
	if num==1:
		if index>=0:
			ShowCard([0,-1], index)
			DisplayChoices(-1)
def newgame():
    	global GameBegan
	global Player1score
	global Player2score
	global Player3score
	global Player4score
	global winner
	Player1score=0
	Player2score=0
	Player3score=0
	Player4score=0
	winner=0
    	GameBegan=0
	screen.blit(background, (0,0))
	screen.blit(write3("Welcome to \"Places Everyone\""),(600,100))
	screen.blit(write4("Hit space for instructions"),(700,250))
	screen.blit(write3("OR"),(775,325))
	screen.blit(write("Choose Your Computer's Difficulty"),(700,400))
	screen.blit(write("Hit 1 for easy"),(700,425))
	screen.blit(write("Hit 2 for medium"),(700,450))
	screen.blit(write("Hit 3 for hard"),(700,475))
	screen.blit(write("Hit 4 for very hard"),(700,500))
	pygame.display.update()
	BACK=True;
	while BACK==True:
		for event in pygame.event.get():
			if event.type== QUIT:
				exit()
			if event.type==MOUSEBUTTONDOWN:
				GameBegan=1
				BACK=False
			if event.type==KEYDOWN:
				if event.key==K_SPACE:
					instructions(0)
					BACK=False
				else:
					GameBegan=1
					BACK=False
	initializeGame()
def difficultySelected(xcoordinate,ycoordinate):
	difficulty=0
	if 700<xcoordinate<867 and 425<ycoordinate<450:
		difficulty=1
	if 700<xcoordinate<867 and 450<ycoordinate<475:
		difficulty=2
	if 700<xcoordinate<867 and 475<ycoordinate<500:
		difficulty=3
	if 700<xcoordinate<880 and 500<ycoordinate<525:
		difficulty=4
	return difficulty
def initializeGame():
    global index
    index=-1
    global start_turn 
    global counter
    global card_clicked_list    
    global p2_card_clicked_list 
    global p3_card_clicked_list 
    global p4_card_clicked_list 
    global player_card_list 
    global player_card_rect 
    global p2_card_rect     
    global p3_card_rect     
    global p4_card_rect     
    global p2_card_list     
    global p3_card_list     
    global p4_card_list
    global CardsInDeck
    global DeckCounter
    DeckCounter=32     
    global all_card_list    
    
    global org_player_card_x 
    global player_card_x     
    global player_card_y     
    global org_p2_card_y 
    global p2_card_x     
    global p2_card_y     
    global org_p3_card_x 
    global p3_card_x     
    global p3_card_y     
    global org_p4_card_y 
    global p4_card_x     
    global p4_card_y     
    global org_display_card_x 
    global display_card_x     
    global display_card_y     
    
    global click_move_y 
    global put_card_alreay 
    global first_put       
    global turn_id 
    global clicked 
    global start3c 
    
    global num_of_card     
    global p2_num_of_card  
    global p3_num_of_card  
    global p4_num_of_card  
    
    
    global start_turn_id 
    global owner         
    global screen_width, screen_height

    counter=0
    loop_num=-1
    if loop_num > 0:
        loop_number = loop_num
    else:
        loop_number = 1
    global hi
    hi=1
    if hi==1:
	    card_clicked_list    = [0] * 5
	    p2_card_clicked_list = [0] * 5
	    p3_card_clicked_list = [0] * 5
	    p4_card_clicked_list = [0] * 5
	    player_card_list  = [0] * 5
	    player_card_rect  = [[0,0], [0,0], [0,0], [0,0], [0,0]]
	    p2_card_rect      = [[0,0], [0,0], [0,0], [0,0], [0,0]]
	    p3_card_rect      = [[0,0], [0,0], [0,0], [0,0], [0,0]]
	    p4_card_rect      = [[0,0], [0,0], [0,0], [0,0], [0,0]]
	    p2_card_list     = [0] * 5
	    p3_card_list     = [0] * 5
	    p4_card_list     = [0] * 5
	    CardsInDeck      = [0] * 32
	    all_card_list    = [0] * 52
            

            org_player_card_x = SCREEN_SIZE[0]/2-4*P_1c.get_width()
            player_card_x     = SCREEN_SIZE[0]/2-4*P_1c.get_width()
            player_card_y     = 500
            org_p2_card_y = 50 + P_1c.get_height()
            p2_card_x     = SCREEN_SIZE[0]-5*Back_Card90.get_width()/2-10
            p2_card_y     = 50 + P_1c.get_height()
            org_p3_card_x = SCREEN_SIZE[0]/2-4*Back_Card.get_width()
            p3_card_x     = SCREEN_SIZE[0]/2-4*Back_Card.get_width()
            p3_card_y     = 50
            org_p4_card_y = 50 + P_1c.get_height() 
            p4_card_x     = Back_Cardn90.get_width()
            p4_card_y     = 50 + P_1c.get_height()
            org_display_card_x = SCREEN_SIZE[0]/2 - P_1c.get_width()/2
            display_card_x     = SCREEN_SIZE[0]/2 - P_1c.get_width()/2

            display_card_y     = 280

            click_move_y =  30
            put_card_alreay = 0
            first_put       = 1
            turn_id = 1
            clicked = 0
            start3c = 1

            num_of_card     = 5
            p2_num_of_card  = 5
            p3_num_of_card  = 5
            p4_num_of_card  = 5

            
            random.seed()
            p4_card_list = ini_random_cards(p4_card_list)
            p3_card_list = ini_random_cards(p3_card_list)
            p2_card_list = ini_random_cards(p2_card_list)
            player_card_list = ini_random_cards(player_card_list)
	    CardsInDeck = ini_random_cards2(CardsInDeck)            	

            start_turn_id = turn_id
            owner         = start_turn_id

            screen.blit(background, (0,0))
             
            screen_width, screen_height = SCREEN_SIZE
             
            for i in range(0, 5): 
                player_card_rect[i][1] = player_card_y
                player_card_rect[i][0] = player_card_x+i*P_1c.get_width()/2
                p2_card_rect[i][1]     = p2_card_y+i*Back_Card90.get_height()/4
                p2_card_rect[i][0]     = p2_card_x
                p3_card_rect[i][1]     = p3_card_y
                p3_card_rect[i][0]     = p3_card_x+i*Back_Card.get_width()/2
                p4_card_rect[i][1]     = p4_card_y+i*Back_Cardn90.get_height()/4
                p4_card_rect[i][0]     = p4_card_x



            start_turn = 0
			
            display_all()
	    screen.blit(write2("Press Space to Review Instructions"),(10,10))
	    screen.blit(write2("Press ESC to see who is winning"),(10,35))
	    screen.blit(write2("Press n to start a new game"),(10,60))
            pygame.display.update()
            
            time.sleep(1)
	    begin=-1
def instructions(num):
	global GameBegan
	screen.blit(background, (0,0))
	screen.blit(write2("instructions"),(700,10))
	screen.blit(write2("__________"),(700,11))
	screen.blit(write2("Steps:"),(450,60))
	screen.blit(write2("1) Five cards are dealt to each player face down"),(450,85))
	screen.blit(write2("2) The player will select one of his cards to view"),(450,110))
	screen.blit(write2("3) The player selects the place he/she thinks that "),(450,135))
	screen.blit(write2("the card selected will rank against the other players selected cards"),(475,160))
	screen.blit(write2("4) The players show and compare cards and see what place their card ranks"),(450,185))
	screen.blit(write2("5) The players then calculate and record their scores based on the scoring table"),(450,210))
	screen.blit(write2("6) Cards used are set aside and players grab a replacement card from the deck"),(450,235))
	screen.blit(write2("7) Repeat steps 1-7 until deck runs out where one final round is played"),(450,260))
	screen.blit(write2("8) Game then ends and the player with the highest points wins."),(450,285))
	screen.blit(write2("Notes:"),(450,310))
	screen.blit(write2("1) Highest card gets first place and lowest card gets last place."),(450,335))
	screen.blit(write2("2) 2 is considered the lowest card and Ace is considered the highest card."),(450,360))
	screen.blit(write2("3) In the last round players do not need to have all five cards if deck runs out."),(450,385))
	screen.blit(write2("4) In the case of a tie, players with the same card choose another card out of "),(450,410))
	screen.blit(write2("their five and the new higher card gets the higher place"),(475,435))
	screen.blit(write2("5) In the last round if a player or players have no more cards to break a tie, the cards suit will determine"),(450,460))
	screen.blit(write2("the higher place. Suits rank in this order from highest to lowest, Spades, Clubs, Hearts, and Diamonds."),(475,485))
	screen.blit(write2("6) If a players five cards tie with another players five cards suits will also determine the higher place."),(450,510))
	screen.blit(write2("7) If there is a tie in points at the end of the game, another round is given with "),(450,535))
	screen.blit(write2("a reshuffled deck until someone pulls ahead in points"),(475,560))
	screen.blit(write2("Scoring:"),(450,585))
	screen.blit(write2("1 point for guessing the correct place"),(500,610))
	screen.blit(write2("0 points for guessing one place off of the correct place"),(500,635))
	screen.blit(write2("-1 points for guessing two or more places off"),(500,660))
	screen.blit(write2("Good luck!"),(450,710))
	if GameBegan==0:
		screen.blit(write2("Left click to go back to the main menu"),(450,750))
	if GameBegan==1:
		screen.blit(write2("Left click to go back to the game"),(450,750))
	pygame.display.update()
	BACK=True
	while BACK==True:
		for event in pygame.event.get():
			if event.type== QUIT:
				exit()
			if event.type==MOUSEBUTTONDOWN:
				if GameBegan==0:
					newgame()
				backtogame(num)
				BACK=False
			if event.type==KEYDOWN:
				if event.key==K_n:
					newgame()
					BACK=False
	return -1
def DisplayChoices(num):
    global clicked
    screen.blit(write("Guess Your Place"),(940,375))
    screen.blit(write("1st place"),(975,400))
    screen.blit(write("2nd place"), (975,425))
    screen.blit(write("3rd place"),(975,450))
    screen.blit(write("4th place"),(975,475))
    pygame.display.update()
    if num==0:
	    BACK=True
    	    while BACK==True:
		for event in pygame.event.get():
			if event.type==QUIT:
				exit()
	    		if event.type==KEYDOWN:
				if event.key==27:
					DisplayScores(1)
				if event.key==K_n:
					newgame()
				if event.key==K_SPACE:
					num=instructions(1)
			if event.type==MOUSEBUTTONDOWN:
				if 976<= pygame.mouse.get_pos()[0] <1064 and 402<=pygame.mouse.get_pos()[1]<499:					
					BACK=False
			    		ChoosePlace(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1] )
					clicked=True
    if num==1:
	    screen.blit(write("Guess Your Place"),(940,375))
	    screen.blit(background, (975, 400), pygame.Rect(975, 400, 100, 25))
	    screen.blit(write2("1st place"),(975,400))
	    screen.blit(write("2nd place"), (975,425))
	    screen.blit(write("3rd place"),(975,450))
	    screen.blit(write("4th place"),(975,475))
	    pygame.display.update()
    if num==2:
	    screen.blit(write("Guess Your Place"),(940,375))
	    screen.blit(write("1st place"),(975,400))
	    screen.blit(background, (975, 425), pygame.Rect(975, 425, 100, 25))
	    screen.blit(write2("2nd place"), (975,425))
	    screen.blit(write("3rd place"),(975,450))
	    screen.blit(write("4th place"),(975,475))
	    pygame.display.update()
    if num==3:
	    screen.blit(write("Guess Your Place"),(940,375))
	    screen.blit(write("1st place"),(975,400))
	    screen.blit(write("2nd place"), (975,425))
	    screen.blit(background, (975, 450), pygame.Rect(975, 450, 100, 25))
	    screen.blit(write2("3rd place"),(975,450))
	    screen.blit(write("4th place"),(975,475))
	    pygame.display.update()
    if num==4:
	    screen.blit(write("Guess Your Place"),(940,375))
	    screen.blit(write("1st place"),(975,400))
	    screen.blit(write("2nd place"), (975,425))
	    screen.blit(write("3rd place"),(975,450))
	    screen.blit(background, (975, 475), pygame.Rect(975, 475, 100, 25))
	    screen.blit(write2("4th place"),(975,475))
	    pygame.display.update()
def CardClicked( mouse_x, mouse_y): 
    global card_clicked_list
    global turn_id
    global index
    for i in range(num_of_card-1, -1, -1):
        if player_card_x + i * P_1c.get_width()/2+60*i+100 <= mouse_x < player_card_x + i * P_1c.get_width()/2 + P_1c.get_width()+60*i+100:
            if 0 == card_clicked_list[i]:
                #unclicked the click card
                if player_card_y <= mouse_y < player_card_y+P_1c.get_height():
		    ShowCard([0,-1], i)
		    index=i
		    DisplayChoices(0)
		    turn_id=2
                    card_clicked_list[i] = 0
                    break

def CardClicked2(numofties): 
	global player_card_rect
	global player_card_list
	global index
	global DeckCounter
	global playertieindex1
	global playertieindex2
	global playertieindex3
	global playertieindex4
	global suit
	if numofties==0:
		card_index=-1
		while card_index==-1:
			for event in pygame.event.get():
			    if event.type == QUIT:
				exit()		
			    if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
				    x=pygame.mouse.get_pos()[0]
				    y=pygame.mouse.get_pos()[1]
				    if 503<y<626:
					if 584<x<663 and index!=0:
						card_index=0
						playertieindex1=0
					if 684<x<763 and index!=1:
						card_index=1
						playertieindex1=1
					if 784<x<863 and index!=2:
						card_index=2
						playertieindex1=2
					if 884<x<963 and index!=3:
						card_index=3
						playertieindex1=3
					if 984<x<1063 and index!=4:
						card_index=4
						playertieindex1=4
		screen.blit(num_to_cards(player_card_list[card_index]), (player_card_rect[card_index][0]+60*card_index+100, player_card_rect[card_index][1]))
		pygame.display.update()
		result=(player_card_list[card_index])/4+2
		player_card_list[card_index]=CardsInDeck[DeckCounter-1]
		return result
	if numofties==1:
		card_index=-1
		while card_index==-1:
			for event in pygame.event.get():
			    if event.type == QUIT:
				exit()		
			    if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
				    x=pygame.mouse.get_pos()[0]
				    y=pygame.mouse.get_pos()[1]
				    if 503<y<626:
					if 584<x<663 and index!=0 and playertieindex1!=0:
						card_index=0
						playertieindex2=0
					if 684<x<763 and index!=1 and playertieindex1!=1:
						card_index=1
						playertieindex2=1
					if 784<x<863 and index!=2 and playertieindex1!=2:
						card_index=2
						playertieindex2=2
					if 884<x<963 and index!=3 and playertieindex1!=3:
						card_index=3
						playertieindex2=3
					if 984<x<1063 and index!=4 and playertieindex1!=4:
						card_index=4
						playertieindex2=4
		screen.blit(num_to_cards(player_card_list[card_index]), (player_card_rect[card_index][0]+60*card_index+100, player_card_rect[card_index][1]))
		pygame.display.update()
		result=(player_card_list[card_index])/4+2
		player_card_list[card_index]=CardsInDeck[DeckCounter-1]
		return result
	if numofties==2:
		card_index=-1
		while card_index==-1:
			for event in pygame.event.get():
			    if event.type == QUIT:
				exit()		
			    if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
				    x=pygame.mouse.get_pos()[0]
				    y=pygame.mouse.get_pos()[1]
				    if 503<y<626:
					if 584<x<663 and index!=0 and playertieindex1!=0 and playertieindex2!=0:
						card_index=0
						playertieindex3=0
					if 684<x<763 and index!=1 and playertieindex1!=1 and playertieindex2!=1:
						card_index=1
						playertieindex3=1
					if 784<x<863 and index!=2 and playertieindex1!=2 and playertieindex2!=2:
						card_index=2
						playertieindex3=2
					if 884<x<963 and index!=3 and playertieindex1!=3 and playertieindex2!=3:
						card_index=3
						playertieindex3=3
					if 984<x<1063 and index!=4 and playertieindex1!=4 and playertieindex2!=4:
						card_index=4
						playertieindex3=4
		screen.blit(num_to_cards(player_card_list[card_index]), (player_card_rect[card_index][0]+60*card_index+100, player_card_rect[card_index][1]))
		pygame.display.update()
		result=(player_card_list[card_index])/4+2
		player_card_list[card_index]=CardsInDeck[DeckCounter-1]
		return result
		return result
	if numofties==3:
		card_index=-1
		while card_index==-1:
			for event in pygame.event.get():
			    if event.type == QUIT:
				exit()		
			    if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
				    x=pygame.mouse.get_pos()[0]
				    y=pygame.mouse.get_pos()[1]
				    if 503<y<626:
					if 584<x<663 and index!=0 and playertieindex1!=0 and playertieindex2!=0 and playertieindex3!=0:
						card_index=0
						playertieindex4=0
					if 684<x<763 and index!=1 and playertieindex1!=1 and playertieindex2!=1 and playertieindex3!=1:
						card_index=1
						playertieindex4=1
					if 784<x<863 and index!=2 and playertieindex1!=2 and playertieindex2!=2 and playertieindex3!=2:
						card_index=2
						playertieindex4=2
					if 884<x<963 and index!=3 and playertieindex1!=3 and playertieindex2!=3 and playertieindex3!=3:
						card_index=3
						playertieindex4=3
					if 984<x<1063 and index!=4 and playertieindex1!=4 and playertieindex2!=4 and playertieindex3!=4:
						card_index=4
						playertieindex4=4
		screen.blit(num_to_cards(player_card_list[card_index]), (player_card_rect[card_index][0]+60*card_index+100, player_card_rect[card_index][1]))
		pygame.display.update()
		suit=player_card_list[card_index]
		result=(player_card_list[card_index])/4+2
		player_card_list[card_index]=CardsInDeck[DeckCounter-1]
		return result
def computertiecard(num,numberofties):
	global p2_card_list     
	global p3_card_list     
	global p4_card_list
	global p2_card_rect
	global p3_card_rect
	global p4_card_rect
	global index2
	global index3
	global index4
	global tieindex1
	global tieindex2
	global tieindex3
	global tieindex4
	global tieindex11
	global tieindex22
	global tieindex33
	global tieindex44
	global tieindex111
	global tieindex222
	global tieindex333
	global tieindex444
	global DeckCounter
	global suit2
	global suit3
	global suit4
	time.sleep(1)
	if numberofties==0:
		card = random.randint(0, 4)
		if num==0:
			while card==index2:
				card = random.randint(0, 4)
			tieindex1=card
			screen.blit(pygame.transform.rotate(num_to_cards(p4_card_list[card]),90),(p4_card_rect[card][0]+250, 100+100*card))
			pygame.display.update()
			result=	(p4_card_list[card]/4)+2		
			p4_card_list[card]=CardsInDeck[DeckCounter-1]
			return result
		if num==1:
			while card==index3:
				card = random.randint(0, 4)
			tieindex11=card
			screen.blit(num_to_cards(p3_card_list[card]),(p3_card_rect[card][0]+60*card+100, p3_card_rect[card][1]))
			pygame.display.update()
			result=(p3_card_list[card]/4)+2
			p3_card_list[card]=CardsInDeck[DeckCounter-1]
			return result
		if num==2:
			while card==index4:
				card = random.randint(0, 4)
			tieindex111=card
			screen.blit(pygame.transform.rotate(num_to_cards(p2_card_list[card]),90),(p2_card_rect[card][0]-100,100+100*card))
			pygame.display.update()
			result=(p2_card_list[card]/4)+2
			p2_card_list[card]=CardsInDeck[DeckCounter-1]
			return result

	if numberofties==1:
		card = random.randint(0, 4)
		if num==0:
			while card==index2 or card==tieindex1:
				card = random.randint(0, 4)
			tieindex2=card
			screen.blit(pygame.transform.rotate(num_to_cards(p4_card_list[card]),90),(p4_card_rect[card][0]+250, 100+100*card))
			pygame.display.update()
			result=	(p4_card_list[card]/4)+2		
			p4_card_list[card]=CardsInDeck[DeckCounter-1]
			return result
		if num==1:
			while card==index3 or card==tieindex11:
				card = random.randint(0, 4)
			tieindex22=card
			screen.blit(num_to_cards(p3_card_list[card]),(p3_card_rect[card][0]+60*card+100, p3_card_rect[card][1]))
			pygame.display.update()
			result=(p3_card_list[card]/4)+2
			p3_card_list[card]=CardsInDeck[DeckCounter-1]
			return result
		if num==2:
			while card==index4 or card==tieindex111:
				card = random.randint(0, 4)
			tieindex222=card
			screen.blit(pygame.transform.rotate(num_to_cards(p2_card_list[card]),90),(p2_card_rect[card][0]-100,100+100*card))
			pygame.display.update()
			result=(p2_card_list[card]/4)+2
			p2_card_list[card]=CardsInDeck[DeckCounter-1]
			return result
	if numberofties==2:
		card = random.randint(0, 4)
		if num==0:
			while card==index2 or card==tieindex1 or card==tieindex2:
				card = random.randint(0, 4)
			tieindex3=card
			screen.blit(pygame.transform.rotate(num_to_cards(p4_card_list[card]),90),(p4_card_rect[card][0]+250, 100+100*card))
			pygame.display.update()
			result=	(p4_card_list[card]/4)+2		
			p4_card_list[card]=CardsInDeck[DeckCounter-1]
			return result
		if num==1:
			while card==index3 or card==tieindex11 or card==tieindex22:
				card = random.randint(0, 4)
			tieindex33=card
			screen.blit(num_to_cards(p3_card_list[card]),(p3_card_rect[card][0]+60*card+100, p3_card_rect[card][1]))
			pygame.display.update()
			result=(p3_card_list[card]/4)+2
			p3_card_list[card]=CardsInDeck[DeckCounter-1]
			return result
		if num==2:
			while card==index4 or card==tieindex111 or card==tieindex222:
				card = random.randint(0, 4)
			tieindex333=card
			screen.blit(pygame.transform.rotate(num_to_cards(p2_card_list[card]),90),(p2_card_rect[card][0]-100,100+100*card))
			pygame.display.update()
			result=(p2_card_list[card]/4)+2
			p2_card_list[card]=CardsInDeck[DeckCounter-1]
			return result
	if numberofties==3:
		card = random.randint(0, 4)
		if num==0:
			while card==index2 or card==tieindex1 or card==tieindex2 or card==tieindex3:
				card = random.randint(0, 4)
			tieindex4=card
			screen.blit(pygame.transform.rotate(num_to_cards(p4_card_list[card]),90),(p4_card_rect[card][0]+250, 100+100*card))
			pygame.display.update()
			suit2=p4_card_list[card]
			result=	(p4_card_list[card]/4)+2		
			p4_card_list[card]=CardsInDeck[DeckCounter-1]
			return result
		if num==1:
			while card==index3 or card==tieindex11 or card==tieindex22 or card==tieindex33:
				card = random.randint(0, 4)
			tieindex44=card
			screen.blit(num_to_cards(p3_card_list[card]),(p3_card_rect[card][0]+60*card+100, p3_card_rect[card][1]))
			pygame.display.update()
			suit3=p3_card_list[card]
			result=(p3_card_list[card]/4)+2
			p3_card_list[card]=CardsInDeck[DeckCounter-1]
			return result
		if num==2:
			while card==index4 or card==tieindex111 or card==tieindex222 or card==tieindex333:
				card = random.randint(0, 4)
			tieindex444=card
			screen.blit(pygame.transform.rotate(num_to_cards(p2_card_list[card]),90),(p2_card_rect[card][0]-100,100+100*card))
			pygame.display.update()
			suit4=p2_card_list[card]
			result=(p2_card_list[card]/4)+2
			p2_card_list[card]=CardsInDeck[DeckCounter-1]
			return result
def ChoosePlace(mouse_x,mouse_y):
	global chosenplace
	chosenplace=0
	if 976 <= mouse_x <1064 and 402 <= mouse_y < 421:
		chosenplace=1
		DisplayChoices(1)
	if 976 <= mouse_x <1064 and 421 <= mouse_y < 449:
		chosenplace=2
		DisplayChoices(2)
	if 976 <= mouse_x <1064 and 449 <= mouse_y < 472:
		chosenplace=3
		DisplayChoices(3)
	if 976 <= mouse_x <1064 and 472 <= mouse_y < 499:
		chosenplace=4
		DisplayChoices(4)
def highercard(number):
	global DeckCounter
	global suit
	global suit2
	global suit3
	global suit4
	if number==0:
		#print "1 and 2"
		screen.blit(write("Flip another card"),(750,300))
		pygame.display.update()
		highercard1=CardClicked2(0)
		DeckCounter=DeckCounter-1
		highercard2=computertiecard(0,0)
		DeckCounter=DeckCounter-1
		if highercard1==highercard2:
			highercard1=CardClicked2(1)
			DeckCounter=DeckCounter-1
			highercard2=computertiecard(0,1)
			DeckCounter=DeckCounter-1
			if highercard1==highercard2:
				highercard1=CardClicked2(2)
				DeckCounter=DeckCounter-1
				highercard2=computertiecard(0,2)
				DeckCounter=DeckCounter-1
				if highercard1==highercard2:
					highercard1=CardClicked2(3)
					DeckCounter=DeckCounter-1
					highercard2=computertiecard(0,3)
					DeckCounter=DeckCounter-1
					if highercard1==highercard2:
						####SUITS DECIDE########
						highercard1=suit
						highercard2=suit2
		if highercard1>highercard2:
			newnumber=1
		else:
			newnumber=0
	if number==1:
		#print "1 and 3"
		screen.blit(write("Flip another card"),(750,300))
		pygame.display.update()
		highercard1=CardClicked2(0)
		DeckCounter=DeckCounter-1
		highercard2=computertiecard(1,0)
		DeckCounter=DeckCounter-1
		if highercard1==highercard2:
			highercard1=CardClicked2(1)
			DeckCounter=DeckCounter-1
			highercard2=computertiecard(1,1)
			DeckCounter=DeckCounter-1
			if highercard1==highercard2:
				highercard1=CardClicked2(2)
				DeckCounter=DeckCounter-1
				highercard2=computertiecard(1,2)
				DeckCounter=DeckCounter-1
				if highercard1==highercard2:
					highercard1=CardClicked2(3)
					DeckCounter=DeckCounter-1
					highercard2=computertiecard(1,3)
					DeckCounter=DeckCounter-1
					if highercard1==highercard2:
						####SUITS DECIDE########
						highercard1=suit
						highercard2=suit3
		if highercard1>highercard2:
			newnumber=1
		else:
			newnumber=0
	if number==2:
		#print "1 and 4"
		screen.blit(write("Flip another card"),(750,300))
		pygame.display.update()
		highercard1=CardClicked2(0)
		DeckCounter=DeckCounter-1
		highercard2=computertiecard(2,0)
		DeckCounter=DeckCounter-1
		if highercard1==highercard2:
			highercard1=CardClicked2(1)
			DeckCounter=DeckCounter-1
			highercard2=computertiecard(2,1)
			DeckCounter=DeckCounter-1
			if highercard1==highercard2:
				highercard1=CardClicked2(2)
				DeckCounter=DeckCounter-1
				highercard2=computertiecard(2,2)
				DeckCounter=DeckCounter-1
				if highercard1==highercard2:
					highercard1=CardClicked2(3)
					DeckCounter=DeckCounter-1
					highercard2=computertiecard(2,3)
					DeckCounter=DeckCounter-1
					if highercard1==highercard2:
						####SUITS DECIDE########
						highercard1=suit
						highercard2=suit4
		if highercard1>highercard2:
			newnumber=1
		else:
			newnumber=0
	if number==3:
		#print "2 and 3"
		highercard1=computertiecard(0,0)
		DeckCounter=DeckCounter-1
		highercard2=computertiecard(1,0)
		DeckCounter=DeckCounter-1
		if highercard1==highercard2:
			highercard1=computertiecard(0,1)
			DeckCounter=DeckCounter-1
			highercard2=computertiecard(1,1)
			DeckCounter=DeckCounter-1
			if highercard1==highercard2:
				highercard1=computertiecard(0,2)
				DeckCounter=DeckCounter-1
				highercard2=computertiecard(1,2)
				DeckCounter=DeckCounter-1
				if highercard1==highercard2:
					highercard1=computertiecard(0,3)
					DeckCounter=DeckCounter-1
					highercard2=computertiecard(1,3)
					DeckCounter=DeckCounter-1
					if highercard1==highercard2:
						####SUITS DECIDE########
						highercard1=suit2
						highercard2=suit3
		if highercard1>highercard2:
			newnumber=1
		else:
			newnumber=0
	if number==4:
		#print "2 and 4"
		highercard1=computertiecard(0,0)
		DeckCounter=DeckCounter-1
		highercard2=computertiecard(2,0)
		DeckCounter=DeckCounter-1
		if highercard1==highercard2:
			highercard1=computertiecard(0,1)
			DeckCounter=DeckCounter-1
			highercard2=computertiecard(2,1)
			DeckCounter=DeckCounter-1
			if highercard1==highercard2:
				highercard1=computertiecard(0,2)
				DeckCounter=DeckCounter-1
				highercard2=computertiecard(2,2)
				DeckCounter=DeckCounter-1
				if highercard1==highercard2:
					highercard1=computertiecard(0,3)
					DeckCounter=DeckCounter-1
					highercard2=computertiecard(2,3)
					DeckCounter=DeckCounter-1
					if highercard1==highercard2:
						####SUITS DECIDE########
						highercard1=suit2
						highercard2=suit4
		if highercard1>highercard2:
			newnumber=1
		else:
			newnumber=0
	if number==5:
		#print "3 and 4"
		highercard1=computertiecard(1,0)
		DeckCounter=DeckCounter-1
		highercard2=computertiecard(2,0)
		DeckCounter=DeckCounter-1
		if highercard1==highercard2:
			highercard1=computertiecard(1,1)
			DeckCounter=DeckCounter-1
			highercard2=computertiecard(2,1)
			DeckCounter=DeckCounter-1
			if highercard1==highercard2:
				highercard1=computertiecard(1,2)
				DeckCounter=DeckCounter-1
				highercard2=computertiecard(2,2)
				DeckCounter=DeckCounter-1
				if highercard1==highercard2:
					highercard1=computertiecard(1,3)
					DeckCounter=DeckCounter-1
					highercard2=computertiecard(2,3)
					DeckCounter=DeckCounter-1
					if highercard1==highercard2:
						####SUITS DECIDE########
						highercard1=suit3
						highercard2=suit4
		if highercard1>highercard2:
			newnumber=1
		else:
			newnumber=0
	if number==6:
		#print "1 and 2 and 3"
		screen.blit(write("Flip another card"),(750,300))
		pygame.display.update()
		highercard1=CardClicked2(0)
		DeckCounter=DeckCounter-1
		highercard2=computertiecard(0,0)
		DeckCounter=DeckCounter-1
		highercard3=computertiecard(1,0)
		DeckCounter=DeckCounter-1
	
		if highercard1>highercard2 and highercard1>highercard3:
			if highercard2>highercard3:
				newnumber=5
			else:
				newnumber=4
		if highercard2>highercard1 and highercard2>highercard3:
			if highercard1>highercard3:
				newnumber=3
			else:
				newnumber=1
		if highercard3>highercard1 and highercard3>highercard2:
			if highercard1>highercard2:
				newnumber=2
			else:
				newnumber=0
	if number==7:
		#print "2 and 3 and 4"
		highercard1=computertiecard(0,0)
		DeckCounter=DeckCounter-1
		highercard2=computertiecard(1,0)
		DeckCounter=DeckCounter-1
		highercard3=computertiecard(2,0)
		DeckCounter=DeckCounter-1
		if highercard1>highercard2 and highercard1>highercard3:
			if highercard2>highercard3:
				newnumber=5
			else:
				newnumber=4
		if highercard2>highercard1 and highercard2>highercard3:
			if highercard1>highercard3:
				newnumber=3
			else:
				newnumber=1
		if highercard3>highercard1 and highercard3>highercard2:
			if highercard1>highercard2:
				newnumber=2
			else:
				newnumber=0
	if number==8:
		#print "1 and 2 and 4"
		newnumber=0
		screen.blit(write("Flip another card"),(750,300))
		pygame.display.update()
		highercard1=CardClicked2(0)
		DeckCounter=DeckCounter-1
		highercard2=computertiecard(0,0)
		DeckCounter=DeckCounter-1
		highercard3=computertiecard(2,0)
		DeckCounter=DeckCounter-1
		if highercard1>highercard2 and highercard1>highercard3:
			if highercard2>highercard3:
				newnumber=5
			else:
				newnumber=4
		if highercard2>highercard1 and highercard2>highercard3:
			if highercard1>highercard3:
				newnumber=3
			else:
				newnumber=1
		if highercard3>highercard1 and highercard3>highercard2:
			if highercard1>highercard2:
				newnumber=2
			else:
				newnumber=0
	if number==9:
		#print "1 and 3 and 4"
		screen.blit(write("Flip another card"),(750,300))
		pygame.display.update()
		highercard1=CardClicked2(0)
		DeckCounter=DeckCounter-1
		highercard2=computertiecard(1,0)
		DeckCounter=DeckCounter-1
		highercard3=computertiecard(2,0)
		DeckCounter=DeckCounter-1
		if highercard1>highercard2 and highercard1>highercard3:
			if highercard2>highercard3:
				newnumber=5
			else:
				newnumber=4
		if highercard2>highercard1 and highercard2>highercard3:
			if highercard1>highercard3:
				newnumber=3
			else:
				newnumber=1
		if highercard3>highercard1 and highercard4>highercard2:
			if highercard1>highercard2:
				newnumber=2
			else:
				newnumber=0
	if number==10:
		#print "1 and 2 and 3 and 4"
		screen.blit(write("Flip another card"),(750,300))
		pygame.display.update()
		highercard1=CardClicked2(0)
		DeckCounter=DeckCounter-1
		highercard2=computertiecard(0,0)
		DeckCounter=DeckCounter-1
		highercard3=computertiecard(1,0)
		DeckCounter=DeckCounter-1
		highercard4=computertiecard(2,0)
		DeckCounter=DeckCounter-1
		if highercard1==highercard2 and highercard1==highercard3 and highercard1!=highercard4:
		#####1,2,3######
			if highercard4>highercard1:
				highercard4=5
			else:
				highercard4=0
			highercard1=CardClicked2(1)
			DeckCounter=DeckCounter-1
			highercard2=computertiecard(0,1)
			DeckCounter=DeckCounter-1
			highercard3=computertiecard(1,1)
			DeckCounter=DeckCounter-1
			if highercard1==highercard2 and highercard1!=highercard3:
				if highercard3>highercard1:
					highercard3=4
				else:
					highercard3=1
				highercard1=CardClicked2(2)
				DeckCounter=DeckCounter-1
				highercard2=computertiecard(0,2)
				DeckCounter=DeckCounter-1
				if highercard1==highercard2:
					highercard1=CardClicked2(3)
					DeckCounter=DeckCounter-1
					highercard2=computertiecard(0,3)
					DeckCounter=DeckCounter-1
					if highercard1==highercard2:
						####SUITS DECIDE########
						highercard1=suit
						highercard2=suit2
						if highercard1>highercard2:
							highercard1=3
							highercard2=2
						else:
							highercard1=2
							highercard2=3
			if highercard1==highercard3 and highercard1!=highercard2:
				if highercard2>highercard1:
					highercard2=4
				else:
					highercard2=1
				highercard1=CardClicked2(2)
				DeckCounter=DeckCounter-1
				highercard3=computertiecard(1,2)
				DeckCounter=DeckCounter-1
				if highercard1==highercard3:
					highercard1=CardClicked2(3)
					DeckCounter=DeckCounter-1
					highercard3=computertiecard(1,3)
					DeckCounter=DeckCounter-1
					if highercard1==highercard3:
						####SUITS DECIDE########
						highercard1=suit
#################################################Part 1##########################################################################
						highercard3=suit3
						if highercard1>highercard3:
							highercard1=3
							highercard3=2
						else:
							highercard1=2
							highercard3=3
			if highercard2==highercard3 and highercard2!=highercard1:
				if highercard1>highercard2:
					highercard1=4
				else:
					highercard1=1
				highercard2=computertiecard(0,2)
				DeckCounter=DeckCounter-1
				highercard3=computertiecard(1,2)
				DeckCounter=DeckCounter-1
				if highercard2==highercard3:
					highercard2=computertiecard(0,3)
					DeckCounter=DeckCounter-1
					highercard3=computertiecard(1,3)
					DeckCounter=DeckCounter-1
					if highercard2==highercard3:
						####SUITS DECIDE########
						highercard2=suit2
						highercard3=suit3
						if highercard2>highercard3:
							highercard2=3
							highercard3=2
						else:
							highercard2=2
							highercard3=3

			if highercard1==highercard2 and highercard1==highercard3:
				highercard1=CardClicked2(2)
				highercard2=computertiecard(0,2)
				highercard3=computertiecard(1,2)
				if highercard1==highercard2 and highercard1!=highercard3:
					if highercard3>highercard1:
						highercard3=4
					else:
						highercard3=1
					highercard1=CardClicked2(3)
					DeckCounter=DeckCounter-1
					highercard2=computertiecard(0,3)
					DeckCounter=DeckCounter-1
					if highercard1==highercard2:
						####SUITS DECIDE########
						highercard1=suit
						highercard2=suit2
						if highercard1>highercard2:
							highercard1=3
							highercard2=2
						else:
							highercard1=2
							highercard2=3
				if highercard1==highercard3 and highercard1!=highercard2:
					if highercard2>highercard1:
						highercard2=4
					else:
						highercard2=1
					highercard1=CardClicked2(3)
					DeckCounter=DeckCounter-1
					highercard3=computertiecard(1,3)
					DeckCounter=DeckCounter-1
					if highercard1==highercard3:
						####SUITS DECIDE########
						highercard1=suit
						highercard3=suit3
						if highercard1>highercard3:
							highercard1=3
							highercard3=2
						else:
							highercard1=2
							highercard3=3
				if highercard2==highercard3 and highercard2!=highercard1:
					if highercard1>highercard2:
						highercard1=4
					else:
						highercard1=1
					highercard2=computertiecard(0,3)
					DeckCounter=DeckCounter-1
####################################################Part 2####################################################
					highercard3=computertiecard(1,3)
					DeckCounter=DeckCounter-1
					if highercard2==highercard3:
						####SUITS DECIDE########
						highercard2=suit2
						highercard3=suit3
						if highercard2>highercard3:
							highercard2=3
							highercard3=2
						else:
							highercard2=2
							highercard3=3
				if highercard1==highercard2 and highercard1==highercard3:
					highercard1=CardClicked2(3)
					highercard2=computertiecard(0,3)
					highercard3=computertiecard(1,3)
					if highercard1==highercard2 and highercard1!=highercard3:
						if highercard3>highercard1:
							highercard3=4
						else:
							highercard3=1
						####SUITS DECIDE########
						highercard1=suit
						highercard2=suit2
						if highercard1>highercard2:
							highercard1=3
							highercard2=2
						else:
							highercard1=2
							highercard2=3
					if highercard1==highercard3 and highercard1!=highercard2:
						if highercard2>highercard1:
							highercard2=4
						else:
							highercard2=1
						####SUITS DECIDE########
						highercard1=suit
						highercard3=suit3
						if highercard1>highercard3:
							highercard1=3
							highercard3=2
						else:
							highercard1=2
							highercard3=3
					if highercard2==highercard3 and highercard2!=highercard1:
						if highercard1>highercard2:
							highercard1=4
						else:
							highercard1=1
						####SUITS DECIDE########
						highercard2=suit2
						highercard3=suit3
						if highercard2>highercard3:
							highercard2=3
							highercard3=2
						else:
							highercard2=2
							highercard3=3
					if highercard1==highercard2 and highercard1==highercard3:
						####SUITS DECIDE########
						highercard1=suit
						highercard2=suit2
						highercard3=suit3
						if highercard1>highercard2 and highercard1>highercard3:
							if highercard2>highercard3:
								highercard1=4
								highercard2=3
								highercard3=2
							if highercard3>highercard2:
								highercard1=4
								highercard2=2
								highercard3=3
						if highercard2>highercard1 and highercard2>highercard3:
							if highercard1>highercard3:
								highercard1=3
								highercard2=4
								highercard3=2
							if highercard3>highercard1:
								highercard1=2
								highercard2=4
								highercard3=3
						if highercard3>highercard1 and highercard3>highercard2:
############################################Part 3##################################################
							if highercard1>highercard2:
								highercard1=3
								highercard2=2
								highercard3=4
							if highercard2>highercard1:
								highercard1=2
								highercard2=3
								highercard3=4

		if highercard1==highercard2 and highercard1==highercard4 and highercard1!=highercard3:
		#####1,2,4######
			if highercard3>highercard1:
				highercard3=5
			else:
				highercard3=0
			highercard1=CardClicked2(1)
			DeckCounter=DeckCounter-1
			highercard2=computertiecard(0,1)
			DeckCounter=DeckCounter-1
			highercard4=computertiecard(2,1)
			DeckCounter=DeckCounter-1
			if highercard1==highercard2 and highercard1!=highercard4:
				if highercard4>highercard1:
					highercard4=4
				else:
					highercard4=1
				highercard1=CardClicked2(2)
				DeckCounter=DeckCounter-1
				highercard2=computertiecard(0,2)
				DeckCounter=DeckCounter-1
				if highercard1==highercard2:
					highercard1=CardClicked2(3)
					DeckCounter=DeckCounter-1
					highercard2=computertiecard(0,3)
					DeckCounter=DeckCounter-1
					if highercard1==highercard2:
						####SUITS DECIDE########
						highercard1=suit
						highercard2=suit2
						if highercard1>highercard2:
							highercard1=3
							highercard2=2
						else:
							highercard1=2
							highercard2=3
			if highercard1==highercard4 and highercard1!=highercard2:
				if highercard2>highercard1:
					highercard2=4
				else:
					highercard2=1
				highercard1=CardClicked2(2)
				DeckCounter=DeckCounter-1
				highercard4=computertiecard(2,2)
				DeckCounter=DeckCounter-1
				if highercard1==highercard4:
					highercard1=CardClicked2(3)
					DeckCounter=DeckCounter-1
					highercard4=computertiecard(2,3)
					DeckCounter=DeckCounter-1
					if highercard1==highercard4:
						####SUITS DECIDE########
						highercard1=suit
						highercard4=suit4
						if highercard1>highercard4:
							highercard1=3
							highercard4=2
						else:
							highercard1=2
							highercard4=3
			if highercard2==highercard4 and highercard2!=highercard1:
				if highercard1>highercard2:
					highercard1=4
				else:
					highercard1=1
				highercard2=computertiecard(0,2)
				DeckCounter=DeckCounter-1
				highercard4=computertiecard(2,2)
				DeckCounter=DeckCounter-1
				if highercard2==highercard4:
					highercard2=computertiecard(0,3)
#####################################################Part 4#########################################
					DeckCounter=DeckCounter-1
					highercard4=computertiecard(2,3)
					DeckCounter=DeckCounter-1
					if highercard2==highercard4:
						####SUITS DECIDE########
						highercard2=suit2
						highercard4=suit4
						if highercard2>highercard4:
							highercard2=3
							highercard4=2
						else:
							highercard2=2
							highercard4=3

			if highercard1==highercard2 and highercard1==highercard4:
				highercard1=CardClicked2(2)
				highercard2=computertiecard(0,2)
				highercard4=computertiecard(2,2)
				if highercard1==highercard2 and highercard1!=highercard4:
					if highercard4>highercard1:
						highercard4=4
					else:
						highercard4=1
					highercard1=CardClicked2(3)
					DeckCounter=DeckCounter-1
					highercard2=computertiecard(0,3)
					DeckCounter=DeckCounter-1
					if highercard1==highercard2:
						####SUITS DECIDE########
						highercard1=suit
						highercard2=suit2
						if highercard1>highercard2:
							highercard1=3
							highercard2=2
						else:
							highercard1=2
							highercard2=3
				if highercard1==highercard4 and highercard1!=highercard2:
					if highercard2>highercard1:
						highercard2=4
					else:
						highercard2=1
					highercard1=CardClicked2(3)
					DeckCounter=DeckCounter-1
					highercard4=computertiecard(2,3)
					DeckCounter=DeckCounter-1
					if highercard1==highercard4:
						####SUITS DECIDE########
						highercard1=suit
						highercard4=suit4
						if highercard1>highercard4:
							highercard1=3
							highercard4=2
						else:
							highercard1=2
							highercard4=3
				if highercard2==highercard4 and highercard2!=highercard1:
					if highercard1>highercard2:
						highercard1=4
					else:
						highercard1=1
					highercard2=computertiecard(0,3)
					DeckCounter=DeckCounter-1
					highercard4=computertiecard(2,3)
					DeckCounter=DeckCounter-1
					if highercard2==highercard4:
						####SUITS DECIDE########
						highercard2=suit2
						highercard4=suit4
						if highercard2>highercard4:
							highercard2=3
							highercard4=2
						else:
							highercard2=2
							highercard4=3
				if highercard1==highercard2 and highercard1==highercard4:
					highercard1=CardClicked2(3)
					highercard2=computertiecard(0,3)
					highercard4=computertiecard(2,3)
					if highercard1==highercard2 and highercard1!=highercard4:
####################################################Part 6####################################################
						if highercard4>highercard1:
							highercard4=4
						else:
							highercard4=1
						####SUITS DECIDE########
						highercard1=suit
						highercard2=suit2
						if highercard1>highercard2:
							highercard1=3
							highercard2=2
						else:
							highercard1=2
							highercard2=3
					if highercard1==highercard4 and highercard1!=highercard2:
						if highercard2>highercard1:
							highercard2=4
						else:
							highercard2=1
						####SUITS DECIDE########
						highercard1=suit
						highercard4=suit4
						if highercard1>highercard4:
							highercard1=3
							highercard4=2
						else:
							highercard1=2
							highercard4=3
					if highercard2==highercard4 and highercard2!=highercard1:
						if highercard1>highercard2:
							highercard1=4
						else:
							highercard1=1
						####SUITS DECIDE########
						highercard2=suit2
						highercard4=suit4
						if highercard2>highercard4:
							highercard2=3
							highercard4=2
						else:
							highercard2=2
							highercard4=3
					if highercard1==highercard2 and highercard1==highercard4:
						####SUITS DECIDE########
						highercard1=suit
						highercard2=suit2
						highercard4=suit4
						if highercard1>highercard2 and highercard1>highercard4:
							if highercard2>highercard4:
								highercard1=4
								highercard2=3
								highercard4=2
							if highercard4>highercard2:
								highercard1=4
								highercard2=2
								highercard4=3
						if highercard2>highercard1 and highercard2>highercard4:
							if highercard1>highercard4:
								highercard1=3
								highercard2=4
								highercard4=2
							if highercard4>highercard1:
								highercard1=2
								highercard2=4
								highercard4=3
						if highercard4>highercard1 and highercard4>highercard2:
							if highercard1>highercard2:
								highercard1=3
								highercard2=2
								highercard4=4
							if highercard2>highercard1:
								highercard1=2
								highercard2=3
								highercard4=4
		if highercard1==highercard3 and highercard1==highercard4 and highercard1!=highercard2:
		#####1,3,4######
			if highercard3>highercard1:
				highercard3=5
			else:
				highercard3=0
			highercard1=CardClicked2(1)
			DeckCounter=DeckCounter-1
			highercard3=computertiecard(1,1)
#################################################part 7###############################################################################
			DeckCounter=DeckCounter-1
			highercard4=computertiecard(2,1)
			DeckCounter=DeckCounter-1
			if highercard1==highercard3 and highercard1!=highercard4:
				if highercard4>highercard1:
					highercard4=4
				else:
					highercard4=1
				highercard1=CardClicked2(2)
				DeckCounter=DeckCounter-1
				highercard3=computertiecard(1,2)
				DeckCounter=DeckCounter-1
				if highercard1==highercard3:
					highercard1=CardClicked2(3)
					DeckCounter=DeckCounter-1
					highercard3=computertiecard(1,3)
					DeckCounter=DeckCounter-1
					if highercard1==highercard3:
						####SUITS DECIDE########
						highercard1=suit
						highercard3=suit3
						if highercard1>highercard3:
							highercard1=3
							highercard3=2
						else:
							highercard1=2
							highercard3=3
			if highercard1==highercard4 and highercard1!=highercard3:
				if highercard3>highercard1:
					highercard3=4
				else:
					highercard3=1
				highercard1=CardClicked2(2)
				DeckCounter=DeckCounter-1
				highercard4=computertiecard(2,2)
				DeckCounter=DeckCounter-1
				if highercard1==highercard4:
					highercard1=CardClicked2(3)
					DeckCounter=DeckCounter-1
					highercard4=computertiecard(2,3)
					DeckCounter=DeckCounter-1
					if highercard1==highercard4:
						####SUITS DECIDE########
						highercard1=suit
						highercard4=suit4
						if highercard1>highercard4:
							highercard1=3
							highercard4=2
						else:
							highercard1=2
							highercard4=3
			if highercard3==highercard4 and highercard3!=highercard1:
				if highercard1>highercard3:
					highercard1=4
				else:
					highercard1=1
				highercard3=computertiecard(1,2)
				DeckCounter=DeckCounter-1
				highercard4=computertiecard(2,2)
				DeckCounter=DeckCounter-1
				if highercard3==highercard4:
					highercard3=computertiecard(1,3)
					DeckCounter=DeckCounter-1
					highercard4=computertiecard(2,3)
					DeckCounter=DeckCounter-1
					if highercard3==highercard4:
						####SUITS DECIDE########
						highercard3=suit3
						highercard4=suit4
						if highercard3>highercard4:
							highercard3=3
							highercard4=2
						else:
							highercard3=2
							highercard4=3

			if highercard1==highercard3 and highercard1==highercard4:
				highercard1=CardClicked2(2)
				highercard3=computertiecard(1,2)
				highercard4=computertiecard(2,2)
				if highercard1==highercard3 and highercard1!=highercard4:
					if highercard4>highercard1:
						highercard4=4
					else:
						highercard4=1
					highercard1=CardClicked2(3)
#################################################part 8##########################################
		if highercard1>highercard2 and highercard1>highercard3 and highercard1>highercard4:
			if highercard2>highercard3 and highercard2>highercard4:
				if highercard3>highercard4:
					newnumber=23
				else:
					newnumber=22
			if highercard3>highercard2 and highercard3>highercard4:
				if highercard2>highercard4:
					newnumber=21
				else:
					newnumber=19
			if highercard4>highercard2 and highercard4>highercard3:
				if highercard2>highercard3:
					newnumber=20
				else:
					newnumber=18
		if highercard2>highercard1 and highercard2>highercard3 and highercard2>highercard4:
			if highercard1>highercard3 and highercard1>highercard4:
				if highercard3>highercard4:
					newnumber=17
				else:
					newnumber=16
			if highercard3>highercard1 and highercard3>highercard4:
				if highercard1>highercard4:
					newnumber=11
				else:
					newnumber=5
			if highercard4>highercard1 and highercard4>highercard3:
				if highercard1>highercard3:
					newnumber=10
				else:
					newnumber=4
		if highercard3>highercard1 and highercard3>highercard2 and highercard3>highercard4:
			if highercard1>highercard2 and highercard1>highercard4:
				if highercard2>highercard4:
					newnumber=15
				else:
					newnumber=13
			if highercard2>highercard1 and highercard2>highercard4:
				if highercard1>highercard4:
					newnumber=9
				else:
					newnumber=3
			if highercard4>highercard1 and highercard4>highercard2:
				if highercard1>highercard2:
					newnumber=7
				else:
					newnumber=1
		if highercard4>highercard1 and highercard4>highercard2 and highercard4>highercard3:
			if highercard1>highercard2 and highercard1>highercard3:
				if highercard2>highercard3:
					newnumber=14
				else:
					newnumber=12
			if highercard2>highercard1 and highercard2>highercard3:
				if highercard1>highercard3:
					newnumber=8
				else:
					newnumber=2
			if highercard3>highercard1 and highercard3>highercard2:
				if highercard1>highercard2:
					newnumber=6
				else:
					newnumber=0
	return newnumber
def tiebreaker():
	global p1card
	global p2card
	global p3card
	global p4card
	if p1card==p2card and p1card==p3card and p1card==p4card:
		#print "all out tie"
		order=highercard(10)
		if order==0:
			p1card=1
			p2card=2
			p3card=3
			p4card=4
		if order==1:
			p1card=1
			p2card=2
			p3card=4
			p4card=3
		if order==2:
			p1card=1
			p2card=3
			p3card=2
			p4card=4
		if order==3:
			p1card=1
			p2card=3
			p3card=4
			p4card=2
		if order==4:
			p1card=1
			p2card=4
			p3card=2
			p4card=3
		if order==5:
			p1card=1
			p2card=4
			p3card=3
			p4card=2
		if order==6:
			p1card=2
			p2card=1
			p3card=3
			p4card=4
		if order==7:
			p1card=2
			p2card=1
			p3card=4
			p4card=3
		if order==8:
			p1card=2
			p2card=3
			p3card=1
			p4card=4
		if order==9:
			p1card=2
			p2card=3
			p3card=4
			p4card=1
		if order==10:
			p1card=2
			p2card=4
			p3card=1
			p4card=3
		if order==11:
			p1card=2
			p2card=4
			p3card=3
			p4card=1
		if order==12:
			p1card=3
			p2card=1
			p3card=2
			p4card=4
		if order==13:
			p1card=3
			p2card=1
			p3card=4
			p4card=2
		if order==14:
			p1card=3
			p2card=2
			p3card=1
			p4card=4
		if order==15:
			p1card=3
			p2card=2
			p3card=4
			p4card=1
		if order==16:
			p1card=3
			p2card=4
			p3card=1
			p4card=2
		if order==17:
			p1card=3
			p2card=4
			p3card=2
			p4card=1
		if order==18:
			p1card=4
			p2card=1
			p3card=2
			p4card=3
		if order==19:
			p1card=4
			p2card=1
			p3card=3
			p4card=2
		if order==20:
			p1card=4
			p2card=2
			p3card=1
			p4card=3
		if order==21:
			p1card=4
			p2card=2
			p3card=3
			p4card=1
		if order==22:
			p1card=4
			p2card=3
			p3card=1
			p4card=2
		if order==23:
			p1card=4
			p2card=3
			p3card=2
			p4card=1
	if p1card==p2card and p1card==p3card and p1card!=p4card:
		#print "three way tie1"

		order=highercard(6)
		if p4card>p1card:
			if order==0:
				p1card=1
				p2card=2
				p3card=3
				p4card=4
			if order==1:
				p1card=2
				p2card=1
				p3card=3
				p4card=4
			if order==2:
				p1card=2
				p2card=3
				p3card=1
				p4card=4
			if order==3:
				p1card=3
				p2card=1
				p3card=2
				p4card=4
			if order==4:
				p1card=3
				p2card=2
				p3card=1
				p4card=4
			if order==5:
				p1card=1
				p2card=3
				p3card=2
				p4card=4
		if p4card<p1card:
			if order==0:
				p1card=2
				p2card=3
				p3card=4
				p4card=1
			if order==1:
				p1card=2
				p2card=4
				p3card=3
				p4card=1
			if order==2:
				p1card=3
				p2card=2
				p3card=4
				p4card=1
			if order==3:
				p1card=3
				p2card=4
				p3card=2
				p4card=1
			if order==4:

				p1card=4
				p2card=2
				p3card=3
				p4card=1
			if order==5:
				p1card=4
				p2card=3
				p3card=2
				p4card=1
		
	if p1card==p2card and p1card!=p3card and p1card==p4card:
		#print "three way tie2"
		order=highercard(8)
		if p3card>p1card:
			if order==0:
				p1card=1
				p2card=2
				p3card=4
				p4card=3
			if order==1:
				p1card=1
				p2card=3
				p3card=4
				p4card=2
			if order==2:
				p1card=2
				p2card=1
				p3card=4
				p4card=3
			if order==3:
				p1card=2
				p2card=3
				p3card=4
				p4card=1
			if order==4:
				p1card=3
				p2card=1
				p3card=4
				p4card=2
			if order==5:
				p1card=3
				p2card=2
				p3card=4
				p4card=1
		if p3card<p1card:
			if order==0:
				p1card=2
				p2card=3
				p3card=1
				p4card=4
			if order==1:
				p1card=2
				p2card=4
				p3card=1
				p4card=3
			if order==2:
				p1card=3
				p2card=2
				p3card=1
				p4card=4
			if order==3:
				p1card=3
				p2card=4
				p3card=1
				p4card=2
			if order==4:
				p1card=4
				p2card=2
				p3card=1
				p4card=3
			if order==5:
				p1card=4
				p2card=3
				p3card=1
				p4card=2
	if p1card!=p2card and p1card==p3card and p1card==p4card:
		#print "three way tie3"
		order=highercard(9)
		if p2card>p1card:
			if order==0:
				p1card=1
				p2card=4
				p3card=2
				p4card=3
			if order==1:
				p1card=1
				p2card=4
				p3card=3
				p4card=2
			if order==2:
				p1card=2
				p2card=4
				p3card=1
				p4card=3
			if order==3:
				p1card=2
				p2card=4
				p3card=3
				p4card=1
			if order==4:
				p1card=3
				p2card=4
				p3card=1
				p4card=2
			if order==5:
				p1card=3
				p2card=4
				p3card=2
				p4card=1
		if p2card<p1card:
			if order==0:
				p1card=2
				p2card=1
				p3card=3
				p4card=4
			if order==1:
				p1card=2
				p2card=1
				p3card=4
				p4card=3
			if order==2:
				p1card=3
				p2card=1
				p3card=2
				p4card=4
			if order==3:
				p1card=3
				p2card=1
				p3card=4
				p4card=2
			if order==4:
				p1card=4
				p2card=1
				p3card=2
				p4card=3
			if order==5:
				p1card=4
				p2card=1
				p3card=3
				p4card=2
	if p4card==p3card and p2card==p4card and p2card!=p1card:
		#print "three way tie4"
		order=highercard(7)
		if p1card>p2card:
			if order==0:
				p1card=4
				p2card=1
				p3card=2
				p4card=3
			if order==1:
				p1card=4
				p2card=1
				p3card=3
				p4card=2
			if order==2:
				p1card=4
				p2card=2
				p3card=1
				p4card=3
			if order==3:
				p1card=4
				p2card=2
				p3card=3
				p4card=1
			if order==4:
				p1card=4
				p2card=3
				p3card=1
				p4card=2
			if order==5:
				p1card=4
				p2card=3
				p3card=2
				p4card=1
		if p1card<p2card:
			if order==0:
				p1card=2
				p2card=3
				p3card=4
				p4card=1
			if order==1:
				p1card=2
				p2card=4
				p3card=3
				p4card=1
			if order==2:
				p1card=3
				p2card=2
				p3card=4
				p4card=1
			if order==3:
				p1card=3
				p2card=4
				p3card=2
				p4card=1
			if order==4:
				p1card=4
				p2card=2
				p3card=3
				p4card=1
			if order==5:
				p1card=4
				p2card=3
				p3card=2
				p4card=1
	if p1card==p2card and p3card==p4card and p1card!=p3card:
		#print "two two way ties1"
		order=highercard(0)
		order2=highercard(5)
		if p1card>p3card:
			if order==0 and order2==0:
				p1card=4
				p2card=3
				p3card=1
				p4card=2				
			if order==0 and order2==1:
				p1card=4
				p2card=3
				p3card=2
				p4card=1
			if order==1 and order2==0:
				p1card=3
				p2card=4
				p3card=1
				p4card=2
			if order==1 and order2==1:
				p1card=3
				p2card=4
				p3card=2
				p4card=1
		if p1card<p3card:
			if order==0 and order2==0:
				p1card=1
				p2card=2
				p3card=3
				p4card=4				
			if order==0 and order2==1:
				p1card=1
				p2card=2
				p3card=4
				p4card=3
			if order==1 and order2==0:
				p1card=2
				p2card=1
				p3card=3
				p4card=4
			if order==1 and order2==1:
				p1card=2
				p2card=1
				p3card=4
				p4card=3
	if p1card==p3card and p2card==p4card and p1card!=p2card:
		#print "two two way ties2"
		order=highercard(1)
		order2=highercard(4)
		if p1card>p2card:
			if order==0 and order2==0:
				p1card=3
				p2card=1
				p3card=4
				p4card=2				
			if order==0 and order2==1:
				p1card=3
				p2card=2
				p3card=4
				p4card=1
			if order==1 and order2==0:
				p1card=4
				p2card=1
				p3card=3
				p4card=2
			if order==1 and order2==1:
				p1card=4
				p2card=2
				p3card=3
				p4card=1
		if p1card<p2card:
			if order==0 and order2==0:
				p1card=1
				p2card=3
				p3card=2
				p4card=4				
			if order==0 and order2==1:
				p1card=1
				p2card=4
				p3card=2
				p4card=3
			if order==1 and order2==0:
				p1card=2
				p2card=3
				p3card=1
				p4card=4
			if order==1 and order2==1:
				p1card=2
				p2card=4
				p3card=1
				p4card=3
	if p1card==p4card and p2card==p3card and p1card!=p2card:
		#print "two two way ties3"
		order=highercard(2)
		order2=highercard(3)
		if p1card>p2card:
			if order==0 and order2==0:
				p1card=3
				p2card=1
				p3card=2
				p4card=4				
			if order==0 and order2==1:
				p1card=3
				p2card=2
				p3card=1
				p4card=4
			if order==1 and order2==0:
				p1card=4
				p2card=1
				p3card=2
				p4card=3
			if order==1 and order2==1:
				p1card=4
				p2card=2
				p3card=1
				p4card=3
		if p1card<p2card:
			if order==0 and order2==0:
				p1card=1
				p2card=3
				p3card=4
				p4card=2				
			if order==0 and order2==1:
				p1card=1
				p2card=4
				p3card=3
				p4card=2
			if order==1 and order2==0:
				p1card=2
				p2card=3
				p3card=4
				p4card=1
			if order==1 and order2==1:
				p1card=2
				p2card=4
				p3card=3
				p4card=1
	if p1card==p2card and p1card!=p3card and p1card!=p4card and p2card!=p3card and p4card!=p2card and p4card!=p3card:
		#print "tie between 1 and 2"
		order=highercard(0)
		if p1card>p3card and p1card>p4card:
			if p3card>p4card:
				if order==0:
					p1card=3
					p2card=4
					p3card=2
					p4card=1				
				if order==1:
					p1card=4
					p2card=3
					p3card=2
					p4card=1
			if p3card<p4card:
				if order==0:
					p1card=3
					p2card=4
					p3card=1
					p4card=2				
				if order==1:
					p1card=4
					p2card=3
					p3card=1
					p4card=2			
		if p1card<p3card and p1card<p4card:
			if p3card>p4card:
				if order==0:
					p1card=1
					p2card=2
					p3card=4
					p4card=3				
				if order==1:
					p1card=2
					p2card=1
					p3card=4
					p4card=3
			if p3card<p4card:
				if order==0:
					p1card=1
					p2card=2
					p3card=3
					p4card=4				
				if order==1:
					p1card=2
					p2card=1
					p3card=3
					p4card=4
		if p1card>p3card and p1card<p4card:
			if order==0:
				p1card=2
				p2card=3
				p3card=1
				p4card=4				
			if order==1:
				p1card=3
				p2card=2
				p3card=1
				p4card=4
		if p1card<p3card and p1card>p4card:
			if order==0:
				p1card=2
				p2card=3
				p3card=4
				p4card=1				
			if order==1:
				p1card=3
				p2card=2
				p3card=4
				p4card=1
	if p1card==p3card and p1card!=p2card and p1card!=p4card and p2card!=p3card and p4card!=p2card and p4card!=p3card:
		#print "tie between 1 and 3"
		order=highercard(1)
		if p1card>p2card and p1card>p4card:
			if p2card>p4card:
				if order==0:
					p1card=3
					p2card=2
					p3card=4
					p4card=1				
				if order==1:
					p1card=4
					p2card=2
					p3card=3
					p4card=1
			if p2card<p4card:
				if order==0:
					p1card=3
					p2card=1
					p3card=4
					p4card=2				
				if order==1:
					p1card=4
					p2card=1
					p3card=3
					p4card=2			
		if p1card<p2card and p1card<p4card:
			if p2card>p4card:
				if order==0:
					p1card=1
					p2card=4
					p3card=2
					p4card=3				
				if order==1:
					p1card=2
					p2card=4
					p3card=1
					p4card=3
			if p2card<p4card:
				if order==0:
					p1card=1
					p2card=3
					p3card=2
					p4card=4				
				if order==1:
					p1card=2
					p2card=3
					p3card=1
					p4card=4
		if p1card>p2card and p1card<p4card:
			if order==0:
				p1card=2
				p2card=1
				p3card=3
				p4card=4				
			if order==1:
				p1card=3
				p2card=1
				p3card=2
				p4card=4
		if p1card<p2card and p1card>p4card:
			if order==0:
				p1card=2
				p2card=4
				p3card=3
				p4card=1				
			if order==1:

				p1card=3
				p2card=4
				p3card=2
				p4card=1
	if p1card==p4card and p1card!=p2card and p1card!=p3card and p2card!=p3card and p4card!=p2card and p4card!=p3card:
		#print "tie between 1 and 4"
		order=highercard(2)
		if p1card>p2card and p1card>p3card:
			if p2card>p3card:
				if order==0:
					p1card=3
					p2card=2
					p3card=1
					p4card=4				
				if order==1:
					p1card=4
					p2card=2
					p3card=1
					p4card=3
			if p2card<p3card:
				if order==0:
					p1card=3
					p2card=1
					p3card=2
					p4card=4				
				if order==1:
					p1card=4
					p2card=1
					p3card=2
					p4card=3			
		if p1card<p2card and p1card<p3card:
			if p2card>p3card:
				if order==0:
					p1card=1
					p2card=4
					p3card=3
					p4card=2				
				if order==1:
					p1card=2
					p2card=4
					p3card=3
					p4card=1
			if p2card<p3card:
				if order==0:
					p1card=1
					p2card=3
					p3card=4
					p4card=2				
				if order==1:
					p1card=2
					p2card=3
					p3card=4
					p4card=1
		if p1card>p2card and p1card<p3card:
			if order==0:
				p1card=2
				p2card=1
				p3card=4
				p4card=3				
			if order==1:
				p1card=3
				p2card=1
				p3card=4
				p4card=2
		if p1card<p2card and p1card>p3card:
			if order==0:
				p1card=2
				p2card=4
				p3card=1
				p4card=3				
			if order==1:
				p1card=3
				p2card=4
				p3card=1
				p4card=2
	if p2card==p4card and p1card!=p2card and p1card!=p3card and p2card!=p3card and p1card!=p4card and p4card!=p3card:
		#print "tie between 2 and 4"
		order=highercard(4)
		if p2card>p1card and p2card>p3card:
			if p1card>p3card:
				if order==0:
					p1card=2
					p2card=3
					p3card=1
					p4card=4				
				if order==1:
					p1card=2
					p2card=4
					p3card=1
					p4card=3
			if p1card<p3card:
				if order==0:
					p1card=1
					p2card=3
					p3card=2
					p4card=4				
				if order==1:
					p1card=1
					p2card=4
					p3card=2
					p4card=3			
		if p2card<p1card and p2card<p3card:
			if p1card>p3card:
				if order==0:
					p1card=4
					p2card=1
					p3card=3
					p4card=2				
				if order==1:
					p1card=4
					p2card=2
					p3card=3
					p4card=1
			if p1card<p3card:
				if order==0:
					p1card=3
					p2card=1
					p3card=4
					p4card=2				
				if order==1:
					p1card=3
					p2card=2
					p3card=4
					p4card=1
		if p2card>p1card and p2card<p3card:
			if order==0:
				p1card=1
				p2card=2
				p3card=4
				p4card=3				
			if order==1:
				p1card=1
				p2card=3
				p3card=4
				p4card=2
		if p2card<p1card and p2card>p3card:
			if order==0:
				p1card=4
				p2card=2
				p3card=1
				p4card=3				
			if order==1:
				p1card=4
				p2card=3
				p3card=1
				p4card=2
	if p2card==p3card and p1card!=p2card and p1card!=p3card and p2card!=p4card and p1card!=p4card and p4card!=p3card:
		#print "tie between 2 and 3"
		order=highercard(3)
		if p2card>p1card and p2card>p4card:
			if p1card>p4card:
				if order==0:
					p1card=2
					p2card=3
					p3card=4
					p4card=1				
				if order==1:
					p1card=2
					p2card=4
					p3card=3
					p4card=1
			if p1card<p4card:
				if order==0:
					p1card=1
					p2card=3
					p3card=4
					p4card=2				
				if order==1:
					p1card=1
					p2card=4
					p3card=3
					p4card=2			
		if p2card<p1card and p2card<p4card:
			if p1card>p4card:
				if order==0:
					p1card=4
					p2card=1
					p3card=2
					p4card=3				
				if order==1:
					p1card=4
					p2card=2
					p3card=1
					p4card=3
			if p1card<p4card:
				if order==0:
					p1card=3
					p2card=1
					p3card=2
					p4card=4				
				if order==1:
					p1card=3
					p2card=2
					p3card=1
					p4card=4
		if p2card>p1card and p2card<p4card:
			if order==0:
				p1card=1
				p2card=2
				p3card=3
				p4card=4				
			if order==1:
				p1card=1
				p2card=3
				p3card=2
				p4card=4
		if p2card<p1card and p2card>p4card:
			if order==0:
				p1card=4
				p2card=2
				p3card=3
				p4card=1				
			if order==1:
				p1card=4
				p2card=3
				p3card=2
				p4card=1
	if p3card==p4card and p1card!=p2card and p1card!=p3card and p2card!=p4card and p1card!=p4card and p2card!=p3card:
		#print "tie between 3 and 4"
		order=highercard(5)
		if p3card>p1card and p3card>p2card:
			if p1card>p2card:
				if order==0:
					p1card=2
					p2card=1
					p3card=3
					p4card=4				
				if order==1:
					p1card=2
					p2card=1
					p3card=4
					p4card=3
			if p1card<p2card:
				if order==0:
					p1card=1
					p2card=2
					p3card=3
					p4card=4				
				if order==1:
					p1card=1
					p2card=2
					p3card=4
					p4card=3			
		if p3card<p1card and p3card<p2card:
			if p1card>p2card:
				if order==0:
					p1card=4
					p2card=3
					p3card=1
					p4card=2				
				if order==1:
					p1card=4
					p2card=3
					p3card=2
					p4card=1
			if p1card<p2card:
				if order==0:
					p1card=3
					p2card=4
					p3card=1
					p4card=2				
				if order==1:
					p1card=3
					p2card=4
					p3card=2
					p4card=1
		if p3card>p1card and p3card<p2card:
			if order==0:
				p1card=1
				p2card=4
				p3card=2
				p4card=3				
			if order==1:
				p1card=1
				p2card=4
				p3card=3
				p4card=2
		if p3card<p1card and p3card>p2card:
			if order==0:
				p1card=4
				p2card=1
				p3card=2
				p4card=3				
			if order==1:
				p1card=4
				p2card=1
				p3card=3
				p4card=2

def calculatescores():
	global Player1score
	global Player2score
	global Player3score
	global Player4score
	global Player1rscore
	global index
	global chosencard2
	global chosencard3
	global chosencard4
	global chosenplace
	global p1card
	global p2card
	global p3card
	global p4card
	tracker=0
	p1card=(player_card_list[index]/4)+2
	p2card=((chosencard2)/4)+2
	p3card=((chosencard3)/4)+2
	p4card=((chosencard4)/4)+2
	tiebreaker()
	if chosenplace==1:
		if p1card>p2card and p1card>p3card and p1card>p4card:
			Player1score=Player1score+1
			Player1rscore=1
			tracker=1
		if (p1card>p2card and p1card>p3card and p1card<p4card) or (p1card>p3card and p1card>p4card and p1card<p2card) or (p1card>p2card and p1card>p4card and p1card<p3card):
			Player1score=Player1score+0
			Player1rscore=0
			tracker=1
		if tracker==0:
			Player1score=Player1score-1
			Player1rscore=-1
	if chosenplace==2:
		if p1card<p2card and p1card<p3card and p1card<p4card:
			Player1score=Player1score-1
			Player1rscore=-1
			tracker=1
		if (p1card>p2card and p1card>p3card and p1card<p4card) or (p1card>p3card and p1card>p4card and p1card<p2card) or (p1card>p2card and p1card>p4card and p1card<p3card):
			Player1score=Player1score+1
			Player1rscore=1
			tracker=1
		if tracker==0:
			Player1score=Player1score+0
			Player1rscore=0
	if chosenplace==3:
		if p1card>p2card and p1card>p3card and p1card>p4card:
			Player1score=Player1score-1
			Player1rscore=-1
			tracker=1
		if (p1card>p2card and p1card<p3card and p1card<p4card) or (p1card>p3card and p1card<p4card and p1card<p2card) or (p1card>p4card and p1card<p2card and p1card<p3card):
			Player1score=Player1score+1
			Player1rscore=1
			tracker=1
		if tracker==0:
			Player1score=Player1score+0
			Player1rscore=0
	if chosenplace==4:
		if p1card<p2card and p1card<p3card and p1card<p4card:
			Player1score=Player1score+1
			Player1rscore=1
			tracker=1
		if (p1card>p2card and p1card<p3card and p1card<p4card) or (p1card>p3card and p1card<p4card and p1card<p2card) or (p1card>p4card and p1card<p2card and p1card<p3card):


			Player1score=Player1score+0
			Player1rscore=0
			tracker=1
		if tracker==0:
			Player1score=Player1score-1
			Player1rscore=-1
	calculatep2score()
	calculatep3score()
	calculatep4score()
def calculatep2score():
	global Player2rscore
	global Player2score
	global chosenplace2
	global p1card
	global p2card
	global p3card
	global p4card
	tracker=0
	if chosenplace2==1:
		if p2card>p1card and p2card>p3card and p2card>p4card:
			Player2score=Player2score+1
			Player2rscore=1
			tracker=1
		if (p2card>p1card and p2card>p3card and p2card<p4card) or (p2card>p3card and p2card>p4card and p2card<p1card) or (p2card>p1card and p2card>p4card and p2card<p3card):
			Player2score=Player2score+0
			Player2rscore=0
			tracker=1
		if tracker==0:
			Player2score=Player2score-1
			Player2rscore=-1
	if chosenplace2==2:
		if p2card<p1card and p2card<p3card and p2card<p4card:
			Player2score=Player2score-1
			Player2rscore=-1
			tracker=1
		if (p2card>p1card and p2card>p3card and p2card<p4card) or (p2card>p3card and p2card>p4card and p2card<p1card) or (p2card>p1card and p2card>p4card and p2card<p3card):
			Player2score=Player2score+1
			Player2rscore=1
			tracker=1
		if tracker==0:
			Player2score=Player2score+0
			Player2rscore=0
	if chosenplace2==3:
		if p2card>p1card and p2card>p3card and p2card>p4card:
			Player2score=Player2score-1
			Player2rscore=-1
			tracker=1
		if (p2card>p1card and p2card<p3card and p2card<p4card) or (p2card>p3card and p2card<p4card and p2card<p1card) or (p2card>p4card and p2card<p1card and p2card<p3card):
			Player2score=Player2score+1
			Player2rscore=1
			tracker=1
		if tracker==0:
			Player2score=Player2score+0
			Player2rscore=0
	if chosenplace2==4:
		if p2card<p1card and p2card<p3card and p2card<p4card:
			Player2score=Player2score+1
			Player2rscore=1
			tracker=1
		if (p2card>p1card and p2card<p3card and p2card<p4card) or (p2card>p3card and p2card<p4card and p2card<p1card) or (p2card>p4card and p2card<p1card and p2card<p3card):
			Player2score=Player2score+0
			Player2rscore=0
			tracker=1
		if tracker==0:
			Player2score=Player2score-1
			Player2rscore=-1
def calculatep3score():
	global Player3rscore
	global Player3score
	global chosenplace3
	global p1card
	global p2card
	global p3card
	global p4card
	tracker=0
	if chosenplace3==1:
		if p3card>p2card and p3card>p1card and p3card>p4card:
			Player3score=Player3score+1
			Player3rscore=1
			tracker=1
		if (p3card>p2card and p3card>p1card and p3card<p4card) or (p3card>p1card and p3card>p4card and p3card<p2card) or (p3card>p2card and p3card>p4card and p3card<p1card):
			Player3score=Player3score+0
			Player3rscore=0
			tracker=1
		if tracker==0:
			Player3score=Player3score-1
			Player3rscore=-1
	if chosenplace3==2:
		if p3card<p2card and p3card<p1card and p3card<p4card:
			Player3score=Player3score-1
			Player3rscore=-1
			tracker=1
		if (p3card>p2card and p3card>p1card and p3card<p4card) or (p3card>p1card and p3card>p4card and p3card<p2card) or (p3card>p2card and p3card>p4card and p3card<p1card):
			Player3score=Player3score+1
			Player3rscore=1
			tracker=1
		if tracker==0:
			Player3score=Player3score+0
			Player3rscore=0
	if chosenplace3==3:
		if p3card>p2card and p3card>p1card and p3card>p4card:
			Player3score=Player3score-1
			Player3rscore=-1
			tracker=1
		if (p3card>p2card and p3card<p1card and p3card<p4card) or (p3card>p1card and p3card<p4card and p3card<p2card) or (p3card>p4card and p3card<p2card and p3card<p1card):
			Player3score=Player3score+1
			Player3rscore=1
			tracker=1
		if tracker==0:
			Player3score=Player3score+0
			Player3rscore=0
	if chosenplace3==4:
		if p3card<p2card and p3card<p1card and p3card<p4card:
			Player3score=Player3score+1
			Player3rscore=1
			tracker=1
		if (p3card>p2card and p3card<p1card and p3card<p4card) or (p3card>p1card and p3card<p4card and p3card<p2card) or (p3card>p4card and p3card<p2card and p3card<p1card):
			Player3score=Player3score+0
			Player3rscore=0
			tracker=1
		if tracker==0:
			Player3score=Player3score-1
			Player3rscore=-1
def calculatep4score():
	global Player4rscore
	global Player4score
	global chosenplace4
	global p1card
	global p2card
	global p3card
	global p4card
	tracker=0
	if chosenplace4==1:
		if p4card>p2card and p4card>p3card and p4card>p1card:
			Player4score=Player4score+1
			Player4rscore=1
			tracker=1
		if (p4card>p2card and p4card>p3card and p4card<p1card) or (p4card>p3card and p4card>p1card and p4card<p2card) or (p4card>p2card and p4card>p1card and p4card<p3card):
			Player4score=Player4score+0
			Player4rscore=0
			tracker=1
		if tracker==0:
			Player4score=Player4score-1
			Player4rscore=-1
	if chosenplace4==2:
		if p4card<p2card and p4card<p3card and p4card<p1card:
			Player4score=Player4score-1
			Player4rscore=-1
			tracker=1
		if (p4card>p2card and p4card>p3card and p4card<p1card) or (p4card>p3card and p4card>p1card and p4card<p2card) or (p4card>p2card and p4card>p1card and p4card<p3card):
			Player4score=Player4score+1
			Player4rscore=1
			tracker=1
		if tracker==0:
			Player4score=Player4score+0
			Player4rscore=0
	if chosenplace4==3:
		if p4card>p2card and p4card>p3card and p4card>p1card:
			Player4score=Player4score-1
			Player4rscore=-1
			tracker=1
		if (p4card>p2card and p4card<p3card and p4card<p1card) or (p4card>p3card and p4card<p1card and p4card<p2card) or (p4card>p1card and p4card<p2card and p4card<p3card):
			Player4score=Player4score+1
			Player4rscore=1
			tracker=1
		if tracker==0:
			Player4score=Player4score+0
			Player4rscore=0
	if chosenplace4==4:
		if p4card<p2card and p4card<p3card and p4card<p1card:
			Player4score=Player4score+1
			Player4rscore=1
			tracker=1
		if (p4card>p2card and p4card<p3card and p4card<p1card) or (p4card>p3card and p4card<p1card and p4card<p2card) or (p4card>p1card and p4card<p2card and p4card<p3card):
			Player4score=Player4score+0
			Player4rscore=0
			tracker=1
		if tracker==0:
			Player4score=Player4score-1
			Player4rscore=-1



def player2():
	global turn_id
	display_p4_num_of_cards(p4_card_list, p4_num_of_card)
    	pygame.display.update()
	turn_id=3
def player3():
	global turn_id
	display_p3_num_of_cards(p3_card_list, p3_num_of_card)
    	pygame.display.update()
	turn_id=4
def player4():
	global turn_id
	global Player1rscore
	global Player2rscore
	global Player3rscore
	global Player4rscore
	global chosenplace
	Player2rscore=0
	Player3rscore=0
	Player4rscore=0
	display_p2_num_of_cards(p2_card_list, p2_num_of_card)
	pygame.display.update()
	calculatescores()
	screen.blit(background, (750, 300), pygame.Rect(750, 300, 200, 62))
	screen.blit(write2("Results of Round"),(750,300))
	pygame.display.update()
	screen.blit(write2("Player 1:"),(750,325))
	screen.blit(write2("Player 2:"),(750,350))
	screen.blit(write2("Player 3:"),(750,375))
	screen.blit(write2("Player 4:"),(750,400))
	screen.blit(writenum2(Player1rscore),(840,325))
	screen.blit(writenum2(Player2rscore),(840,350))
	screen.blit(writenum2(Player3rscore),(840,375))
	screen.blit(writenum2(Player4rscore),(840,400))
	pygame.display.update()
	turn_id=1
	BACK=True
    	while BACK==True:
		for event in pygame.event.get():
			if event.type==QUIT:
				exit()
			if event.type==KEYDOWN:
				if event.key==27:
					DisplayScores(1)
					DisplayChoices(chosenplace)
					player4()
				if event.key==K_n:
					newgame()
				if event.key==K_SPACE:
					instructions(1)
					DisplayChoices(chosenplace)
					player4()
			if event.type==MOUSEBUTTONDOWN:
				BACK=False
				clicked=True
	nextround()
def nextround():
	global GameBegan
	global DeckCounter
	global index
	global index2
	global index3
	global index4
	global p2_card_list
	global p3_card_list
	global p4_card_list
	global player_card_list
	if DeckCounter>0:
		GameBegan=1
		screen.blit(background, (0,0))
		player_card_list[index]=CardsInDeck[DeckCounter-1]
		p2_card_list[index2]=CardsInDeck[DeckCounter-2]
		p3_card_list[index3]=CardsInDeck[DeckCounter-3]
		p4_card_list[index4]=CardsInDeck[DeckCounter-4]
		DeckCounter=DeckCounter-4
		display_all()
		screen.blit(write2("Press Space to Review Instructions"),(10,10))
		screen.blit(write2("Press ESC to see who is winning"),(10,35))
		screen.blit(write2("Press n to start a new game"),(10,60))
		pygame.display.update()
		time.sleep(1)
		begin=-1
	else:
		DisplayEndGameScores()
def ShowCard(speed,card_index):
    global player_card_rect
    global num_of_card
    screen.blit(num_to_cards(player_card_list[card_index]), (player_card_rect[card_index][0]+60*card_index+100, player_card_rect[card_index][1]))
    pygame.display.update()

def main():
    newgame()
    global begin
    global index
    index=-1
    begin=1
    global start_turn 
    global counter
    global card_clicked_list    
    global p2_card_clicked_list 
    global p3_card_clicked_list 
    global p4_card_clicked_list 
    global player_card_list 
    global player_card_rect 
    global p2_card_rect     
    global p3_card_rect     
    global p4_card_rect     
    global p2_card_list     
    global p3_card_list     
    global p4_card_list     
    global all_card_list    
    
    global org_player_card_x 
    global player_card_x     
    global player_card_y     
    global org_p2_card_y 
    global p2_card_x     
    global p2_card_y     
    global org_p3_card_x 
    global p3_card_x     
    global p3_card_y     
    global org_p4_card_y 
    global p4_card_x     
    global p4_card_y     
    global org_display_card_x 
    global display_card_x     
    global display_card_y     
    
    global click_move_y 
    global first_put       
    global turn_id 
    global clicked 
    global start3c 
    
    global num_of_card     
    global p2_num_of_card  
    global p3_num_of_card  
    global p4_num_of_card  
 
    
    
    global start_turn_id 
    global owner         
    global screen_width, screen_height
    
    
    while begin > 0:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
	    if event.type==KEYDOWN:
		if event.key==27:
			DisplayScores(0)
		if event.key==K_n:
			newgame()
		if event.key==K_SPACE:
			instructions(0)
			
            if event.type == MOUSEBUTTONDOWN and begin >0:
                if event.button == 1 and turn_id == 1:
                    CardClicked(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
	if turn_id==2 and clicked==True:
		player2()
	if turn_id==3:
		player3()
	if turn_id==4:
		player4()	    
    exit()
		
if __name__ == "__main__":
    main()
    
