import random, os
import time 
import pygame
from pygame.locals import *
from sys import exit

background_image_filename = 'Image/test.jpg'
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

def display_desktop_cards(list, num):
    for x in range(0, num):
        screen.blit(Back_Card, (800, 300))

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
			screen.blit(pygame.transform.rotate(num_to_cards(p2_card_list[0]),90),(p2_card_rect[x][0]-100,100+100*x))			if x!=0:
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


def ini_random_cards(p_card_list, p_id):
    global all_card_list
    global turn_id
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
        return P_2c
    if 1==num:
        return P_2d
    if 2==num:
        return P_2h
    if 3==num:
        return P_2s
    if 4==num:
        return P_3c
    if 5==num:
        return P_3d 
    if 6==num:
        return P_3h
    if 7==num:
        return P_3s
    if 8==num:
        return P_4c
    if 9==num:
        return P_4d
    if 10==num:
        return P_4h
    if 11==num:
        return P_4s
    if 12==num:
        return P_5c
    if 13==num:
        return P_5d
    if 14==num:
        return P_5h
    if 15==num:
        return P_5s
    if 16==num:
        return P_6c
    if 17==num:
        return P_6d
    if 18==num:
        return P_6h
    if 19==num:
        return P_6s
    if 20==num:
        return P_7c
    if 21==num:
        return P_7d
    if 22==num:
        return P_7h
    if 23==num:
        return P_7s
    if 24==num:
        return P_8c
    if 25==num:
        return P_8d
    if 26==num:
        return P_8h
    if 27==num:
        return P_8s
    if 28==num:
        return P_9c
    if 29==num:
        return P_9d
    if 30==num:
        return P_9h
    if 31==num:
        return P_9s
    if 32==num:
        return P_10c
    if 33==num:
        return P_10d
    if 34==num:
        return P_10h
    if 35==num:
        return P_10s
    if 36==num:
        return P_11c
    if 37==num:
        return P_11d
    if 38==num:
        return P_11h
    if 39==num:
        return P_11s
    if 40==num:
        return P_12c
    if 41==num:
        return P_12d
    if 42==num:
        return P_12h
    if 43==num:
        return P_12s
    if 44==num:
        return P_13c
    if 45==num:
        return P_13d
    if 46==num:
        return P_13h
    if 47==num:
        return P_13s
    if 48==num:
        return P_1c
    if 49==num:
        return P_1d
    if 50==num:
        return P_1h
    if 51==num:
        return P_1s

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
def backtogame():
	global index
	display_all()
	screen.blit(write2("Press Space to Review Instructions"),(10,10))
	pygame.display.update()
	if index>=0:
		ShowCard([0,-1], index)
		DisplayChoices(0)
def newgame():
    	global GameBegan
    	GameBegan=0
	screen.blit(background, (0,0))
	screen.blit(write3("Welcome to Places Everyone"),(600,100))
	screen.blit(write4("Hit space for instructions"),(700,250))
	screen.blit(write3("OR"),(775,325))
	screen.blit(write("Choose Your Computer's Difficulty"),(700,400))
	screen.blit(write("Hit 1 for easy"),(700,425))
	screen.blit(write("Hit 2 for medium"),(700,450))
	screen.blit(write("Hit 3 for hard"),(700,475))
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
					instructions()
					BACK=False
				else:
					GameBegan=1
					BACK=False
	initializeGame()
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
    global desktop_card_list
    global desktop_card_rect
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
    global put_card_alreay 
    global first_put       
    global turn_id 
    global clicked 
    global start3c 
    
    global num_of_card     
    global p2_num_of_card  
    global p3_num_of_card  
    global p4_num_of_card  
    global num_of_desktop_card 
    
    
    global start_turn_id 
    global owner         
    global screen_width, screen_height
    
    global winner
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
	    desktop_card_list = [0] * 5
	    desktop_card_rect = [[0,0], [0,0], [0,0], [0,0], [0,0]]
	    p2_card_list     = [0] * 5
	    p3_card_list     = [0] * 5
	    p4_card_list     = [0] * 5
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
            num_of_desktop_card = 0

            
            random.seed()
            p4_card_list = ini_random_cards(p4_card_list, 4)
            p3_card_list = ini_random_cards(p3_card_list, 3)
            p2_card_list = ini_random_cards(p2_card_list, 2)
            player_card_list = ini_random_cards(player_card_list, 1)
            
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


            for i in range(0,5):
                desktop_card_rect[i][1] = display_card_y

            start_turn = 0
			
            display_all()
	    screen.blit(write2("Press Space to Review Instructions"),(10,10))
            pygame.display.update()
            
            time.sleep(1)
	    begin=-1
def instructions():
	global GameBegan
	screen.blit(background, (0,0))
	screen.blit(write2("instructions"),(700,10))
	screen.blit(write2("__________"),(700,11))
	screen.blit(write2("First, 5 cards are dealt to each player"),(500,60))
	screen.blit(write2("Next, the player will select one card to view"),(500,85))
	screen.blit(write2("The player then selects at which place he/she thinks that "),(500,110))
	screen.blit(write2("the card will rank against the other players selected cards"),(500,135))
	screen.blit(write2("Then all players will show their cards and scoring will take place as follows"),(500,160))
	screen.blit(write2("1 point for a correct guess"),(600,185))
	screen.blit(write2("0 points for being one place off of the correct place"),(600,210))
	screen.blit(write2("-1 points for being two places off and so on and so forth"),(600,235))
	screen.blit(write2("Play ends after the deck runs out"),(500,260))
	screen.blit(write2("In the case of a tie, players with the same card choose another card out of "),(500,285))
	screen.blit(write2("their five and the higher card gets the higher place"),(500,310))
	screen.blit(write2("If there is a five card tie with the deck gone, suit will be used to break the"),(500,335))
	screen.blit(write2("tie with this order from highest to lowest, Spades, Clubs, Hearts, and Diamonds."),(500,360))
	screen.blit(write2("If there is a tie in points at the end of the game, another round is given with "),(500,385))
	screen.blit(write2("a reshuffled deck until someone pulls ahead in points"),(500,410))
	screen.blit(write2("Note: Ace is high"),(500,435))
	screen.blit(write2("Good luck!"),(500,460))
	if GameBegan==0:
		screen.blit(write2("Left click to go back to the main menu"),(500,550))
	if GameBegan==1:
		screen.blit(write2("Left click to go back to the game"),(500,550))
	pygame.display.update()
	BACK=True
	while BACK==True:
		for event in pygame.event.get():
			if event.type== QUIT:
				exit()
			if event.type==MOUSEBUTTONDOWN:
				if GameBegan==0:
					newgame()
				backtogame()
				BACK=False
			if event.type==KEYDOWN:
				if event.key==K_n:
					newgame()
					BACK=False
				else:
					BACK=False
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
    global desktop_card_list
    global desktop_card_rect
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
    global num_of_desktop_card 
    
    
    global start_turn_id 
    global owner         
    global screen_width, screen_height
    
    global winner
    
    while begin > 0:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
	    if event.type==KEYDOWN:
		if event.key==27:
			DisplayScores() #modify to exit
		if event.key==K_n:
			newgame()
		if event.key==K_SPACE:
			instructions()			
            if event.type == MOUSEBUTTONDOWN and begin >0:
                if event.button == 1 and turn_id == 1:
                    CardClicked(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
		    ChoosePlace()
		    turn_id=2

        #pygame.display.update()
       # if 0 == num_of_card or 0 == p2_num_of_card or 0 == p3_num_of_card or 0 == p4_num_of_card:
            #time.sleep(4)
    exit()
		
if __name__ == "__main__":
    main()
    
