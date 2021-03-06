import math
import random
import wave
import pickle
import textinput
import pygame

import pygame
from pygame import mixer
import  sys, eztext

# Intialize the pygame
pygame.init()

# create the screen
scrWidth = 600
scrHeight = 800
screen = pygame.display.set_mode((800, 600))

# user input code


# Background
background = pygame.image.load('background.png')

# caution icon
cautionIcon = pygame.image.load('caution1.png')
cautionIcon2 = pygame.image.load('caution2.png')
cautionList = [cautionIcon, cautionIcon2]

# Sound
#   get playing rate
song_frequency = wave.open("background.wav").getframerate()
print(song_frequency)
print(song_frequency* 10)
pygame.mixer.init(frequency= song_frequency * 5, allowedchanges = 1 )
pygame.mixer.music.load("background.wav")
#pygame.mixer.music.play(-1)
"""
mixer.music.load("background.wav")
mixer.music.play(-1)
"""

# Caption and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)


# High Score

# grab from file
pickle_in = open("highScores.pkl","rb")
highScores = pickle.load(pickle_in)
print("these are high scores")
print(highScores)
#d = { line.split()[0] : line.split()[1] for line in open("highScores.csv") }


scoresList = {}
# write to file
highScores = {'1st': ["name1", "10"], '2nd':["name2", "8"],'3rd': ["name3", "6"],'4th': ["name4", "5"],'5th': ["name5","4"],'6th': ["name6","3"]}
f = open("highScores.pkl", "wb")
pickle.dump(highScores, f)
f.close()

# Player
shipList = []
shipList.append('vaccine.png') ### ding ding
shipList.append('python-file.png')
shipList.append('player.png')

playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

# Enemy
enemyImg = []
#enemyX = []
#enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

enemyX = []
betterEnemySpacer = 90
lowerbound = - 90
for i in range(num_of_enemies):
    x = 0
    x = random.randint(lowerbound + betterEnemySpacer, betterEnemySpacer)
    while(x in enemyX):
        x =  random.randint(lowerbound + betterEnemySpacer, betterEnemySpacer) # old values 50 and 150
    enemyX.append(x)
    betterEnemySpacer += 90

enemyY = []
for i in range(num_of_enemies):
    y = 0
    y = random.randint(50,150) 
    while(y in enemyY):
        y =  random.randint(50, 150)
    enemyY.append(y)


for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png')) # ding ding
    #enemyX.append(random.randint(0, 736))
    #enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

# Bullet

# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving

bulletImg = pygame.image.load('bullet.png') # ding ding
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

# Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
testY = 10

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 60) #64 OLD VALUE


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def grad():
    wrd = font.render("Graduation", True, (255,255,255))
    screen.blit(wrd, (300, 550))

def pausedmsg():
    wrd = font.render("Paused", True, (255,255,255))
    screen.blit(wrd, (300, 200))

newHS = 0
def game_over_text():
    txtbx = eztext.Input(maxlength=45, color=(255,0,0), prompt='Enter Initials: ')
    clock = pygame.time.Clock()
    
    global enter_high_score
    while enter_high_score:
        clock.tick(30)


        # events for txtbx
        events = pygame.event.get()
        # process other events
        for event in events:
            if event.type == pygame.QUIT:
                enter_high_score = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    global newHS
                    newHS = txtbx.value
                    enter_high_score = False

        # update txtbx

        txtbx.update(events)
        # blit txtbx on the sceen
        txtbx.draw(screen)
        # refresh the display
        pygame.display.flip()


    #txtin = textinput.TextInput()
    #events = pygame.event.get()
    #for event in events:
     #   if event.type ==pygame.QUIT:
      #      exit()
        
        #Feed it with events every frame
        #txtin.update(event)
        #Blit it's surface onto the screen
        #screen.blit(txtin.get_surface(),(200,200))

        #if txtin.update(events):
         #   newHS = textinput.get_text()

  


    k, stR = load_highscore_from_file()
    highScores = k

    highScores["5th"]= newHS,score_value

    # store file, only top 3
    store_highscore_in_file(k, top_n=6)

    #load back in new dict and str
    kk, hsSTR = load_highscore_from_file()
   

    endgame= ["GAME OVER", ":High Scores:", str(highScores["1st"][0])+ ": "+str(highScores["1st"][1]) , str(highScores["2nd"][0])+ ": " + str(highScores["2nd"][1]) ,
                str(highScores["3rd"][0])+ ": " + str(highScores["3rd"][1]),str(highScores["4th"][0])+ ": "+str(highScores["4th"][1]),
                str(highScores["5th"][0])+ ": " + str(highScores["5th"][1]),]
    label = []
    
    for line in endgame:
        label.append(over_font.render(line, True,(255,255,255)))
    
    scoreDesc = 50
    for line in label:
        #screen.blit(line,(scrWidth/8+ (int(line)*64), scrHeight/8+(15*int(line))))
        screen.blit(line,(200, 50 + scoreDesc ))
        scoreDesc +=54

   

    #over_text = over_font.render("game over", True, (255,255,255))
    #screen.blit(over_text, (200, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

# forked from stack overflow "https://stackoverflow.com/questions/16726354/saving-the-highscore-for-a-python-game"
def store_highscore_in_file(dictionary, fn = "./high.txt", top_n=0):
    """Store the dict into a file, only store top_n highest values."""
    with open(fn,"w") as f:
        for idx,(rank, plyr) in enumerate(sorted(dictionary.items(), key= lambda x:x[0][1])):
            f.write(f"{rank}:{plyr[0]}:{plyr[1]}\n")
            if top_n and idx == top_n-1:
                break

def load_highscore_from_file(fn = "./high.txt"):
    """Retrieve dict from file"""
    hs = {}
    hstr =""
    try:
        with open(fn,"r") as f:
            for line in f:

                #name,_,points = line.partition(":")

                els  = line.split(":")
               
                hs[els[0]]= els[1], int(els[2])
                hstr += "\n" + els[1] + els[2]
    except FileNotFoundError:
        return {}
    return hs, hstr


# Game Loop
shipSelection = True
paused = False
running = True
enter_high_score = True

# ship selection state
while running and shipSelection:
    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                selection = 0
                playerImg = pygame.image.load(shipList[selection])
                shipSelection = False
            if event.key == pygame.K_2:
                selection = 1
                playerImg = pygame.image.load(shipList[selection])
                shipSelection = False

            if event.key == pygame.K_3:
                selection = 2
                playerImg = pygame.image.load(shipList[selection])
                shipSelection = False
    spacer = 1
    for shipOption in shipList:
        screen.blit( pygame.image.load(shipOption), ( 450, (150+spacer)))
        spacer += 120  

     #code for ship selection text
    shipSelectionText = ["Choose your ship!", "Option (1):", "Option (2):", "Option (3):","Press numeric key"]
    ssLabel = []

    for word in shipSelectionText:
        ssLabel.append(over_font.render(word, True, (255,255,255)))
    
    textSpacer = -120
    for word in ssLabel:
        screen.blit(word, (135, (150 + textSpacer)))
        textSpacer += 120  
    pygame.display.update()
   

cautionflag = False
# game start state
while running and not shipSelection:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))

    
    screen.blit(background, (0, 0))
    #pygame.draw.rect(screen, (255,0,0), (300,300,400,400))
    pygame.draw.lines(screen,(255,255,0), False, [[0,300],[800,300]], 3 )
    pygame.draw.lines(screen,(255,0,0), False, [[0,476],[800,476]], 5 )

    if (not paused):
        screen.blit(font.render("Press P to pause", True, (255,255,255)), (300, 20))
        
        

    # Background Image rendering
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        
        
       
        

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused
            if event.key == pygame.K_LEFT and not paused:
                playerX_change = -5
            if event.key == pygame.K_RIGHT and not paused:
                playerX_change = 5
            if event.key == pygame.K_UP and not paused:
                playerY_change = -5
            if event.key == pygame.K_DOWN and not paused:
                playerY_change = 5
            if event.key == pygame.K_SPACE and not paused:
                if bullet_state == "ready":
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound.play()
                    # Get the current x cordinate of the spaceship
                    bulletX, bulletY = playerX, playerY
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                playerX_change = 0
                playerY_change = 0

#pygame.draw.lines(screen,(255,255,0), False, [[0,300],[800,300]], 3 )
 #   pygame.draw.lines(screen,(255,0,0), False, [[0,476],[800,476]], 5 )
    
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    playerY += playerY_change
    if playerY <= 305:
        playerY = 305
    elif playerY >= 476:
        playerY = 476
    

    if(cautionflag == True):
        screen.blit(cautionList[random.randint(0,2) % 2], (650, 400))
    # Enemy Movement
    if not paused:
        cautionflag = False
        for i in range(num_of_enemies):

            #caution, enemy  closing in
            if (enemyY[i]> 300 ):
                cautionflag = True
               
            elif ( cautionflag):
                 cautionflag = True
            else:
                cautionflag = False
            #if(enemyY[i] >= 2000):
             #   cautionflag = False

           

            # Game Over ###CHANGED FROM 440, or 110 to insta Game over or past playerY coordinate
            if enemyY[i] > playerY or  enemyY[i] > 440: # insta game over
                for j in range(num_of_enemies):
                    enemyY[j] = 2000
                cautionflag = False
                game_over_text()
                break

            enemyX[i] += enemyX_change[i]
            if enemyX[i] <= 0:
                enemyX_change[i] = 4
                enemyY[i] += enemyY_change[i]
            elif enemyX[i] >= 736:
                enemyX_change[i] = -4
                enemyY[i] += enemyY_change[i]

            # Collision
            collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
            if collision:
                explosionSound = mixer.Sound("explosion.wav")
                explosionSound.play()
                bulletY = 480
                bullet_state = "ready"
                score_value += 1

                x = random.randint(0, 736)
                while(x in enemyX):
                    x =  random.randint(0, 736)
                enemyX[i] = x


                y = random.randint(50, 150)
                while(y in enemyY):
                    y =  random.randint(50, 150)
                enemyY[i] = y
                #enemyX[i] = random.randint(0, 736)
                #enemyY[i] = random.randint(50, 150)
                # respawns randoms again ###############

            enemy(enemyX[i], enemyY[i], i)

        # Bullet Movement
        if bulletY <= 0:
            bulletY = 480
            bullet_state = "ready"

        if bullet_state == "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

        #grad()
        player(playerX, playerY)
        show_score(textX, testY)
        pygame.display.update()
        
