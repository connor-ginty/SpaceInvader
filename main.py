import pygame
from pygame import mixer
import random
import math

# Initialize pygame
pygame.init()

# Create the screen
SCREENWIDTH = 800
SCREENHEIGHT = 600
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

# Background
background = pygame.image.load('space2.png')

# Sound
mixer.music.load("background.wav")
mixer.music.play(-1)

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

# Bullet
# Ready - You can't see the bullet on the screen.
# Fire - The bullet is currently moving.
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
buttletX_change = 0
bulletY_change = 2
bullet_state = "ready"

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

global num_of_enemies
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(0.3)
    enemyY_change.append(40)

# Score
global score_value
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10
        
def player(x, y):
    screen.blit(playerImg, (x, y))
    # blit = draw

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    # Formula for caluclating distance between coordinates
    distance = math.sqrt(math.pow((enemyX - bulletX), 2) + math.pow((enemyY - bulletY), 2))
    if distance < 36: # Hit box, bigger number means easier to hit
        return True
    else:
        return False

# Starting Menu
start_title_font = pygame.font.Font('freesansbold.ttf', 64)
start_game_font = pygame.font.Font('freesansbold.ttf', 32)

#Game Over text
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x,y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 0))
    screen.blit(score, (x,y))

def game_over_text():
        over_text = over_font.render("GAME OVER", True, (255, 255, 0))
        screen.blit(over_text, (200, 250))

def start_menu_text():
        start_title = start_title_font.render("Space Invaders", True, (255, 255, 0))
        screen.blit(start_title, (400, 300))

        start_game = start_game_font.render("Press Space to Start", True, (255, 255, 0))
        screen.blit(start_game, (300, 350))

# Infinite Game Loop
running = True
while (running):

    # Stays in the background
    screen.fill((0, 0, 32))  # RGB
    # Background image
    screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed, check whether is right or left.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.4
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.4
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound("laser.wav")
                    bullet_sound.play()
                    # Get the current x coordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
        
    
    playerX += playerX_change

    # Creating Borders
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy movement
    for i in range(num_of_enemies):
    
    #Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000 #removing enemies from sight on game screen
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0: # moving to the right
            enemyX[i] = 0
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
            #Difficulty scaling - ugly but works
            if score_value >= 10:
                enemyX_change[i] += 0.05
                if score_value >= 20:
                    enemyX_change[i] += 0.05
                    if score_value >= 30:
                        enemyX_change[i] += 0.05
                        if score_value >= 40:
                            enemyX_change[i] += 0.05
                            if score_value >= 50:
                                enemyX_change[i] += 0.05
                                if score_value >= 60:
                                    enemyX_change[i] += 0.05
                                    if score_value >= 70:
                                        enemyX_change[i] += 0.05
                                        if score_value >= 80:
                                            enemyX_change[i] += 0.05
                                            if score_value >= 70:
                                                enemyX_change[i] += 0.05
                                                if score_value >= 80:
                                                    enemyX_change[i] += 0.05

        elif enemyX[i] >= 736: # moving to the left
            enemyX[i] = 736
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]
            #Difficulty scaling - ugly but works
            if score_value >= 10:
                enemyX_change[i] -= 0.05
                if score_value >= 20:
                    enemyX_change[i] -= 0.05
                    if score_value >= 30:
                        enemyX_change[i] -= 0.05
                        if score_value >= 40:
                            enemyX_change[i] -= 0.05
                            if score_value >= 50:
                                enemyX_change[i] -= 0.05
                                if score_value >= 60:
                                    enemyX_change[i] -= 0.05
                                    if score_value >= 70:
                                        enemyX_change[i] -= 0.05
                                        if score_value >= 80:
                                            enemyX_change[i] -= 0.05
                                            if score_value >= 90:
                                                enemyX_change[i] -= 0.05
                                            if score_value >= 100:
                                                enemyX_change[i] -= 0.05


        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)

        if collision:
        # Resetting bullet
            explosion_sound = mixer.Sound("explosion.wav")
            explosion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0,735)
            enemyY[i] = random.randint(50,150)
            
        enemy(enemyX[i], enemyY[i], i)     # Enemy starting position

    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    show_score(textX, textY)
    player(playerX, playerY)  # Player starting position
    # scale_difficulty()
    pygame.display.update()
