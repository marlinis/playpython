import pygame
import math
import random

# inicializando pygame
pygame.init()

# creando la pantalla del juego
screen = pygame.display.set_mode((800, 600))

# cargando background
background = pygame.image.load('background.png')

# Modificando Titulo e iconno
pygame.display.set_caption("Invasores del Espacio")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)


# incoporando player o nave espacial al juego.
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0


# incoporando enemy al juego.
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.3)
    enemyY_change.append(40)

# agregando bullet o disparos
# Ready - No puedes ver la bala en la pantalla.
# Fire - La bala se está moviendo actualmente.
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

score = 0

def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))
    
def fire_bullet(x, y):
    global bullet_state 
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))
    
def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY,2)))
    if distance < 27:
        return True
    else:
        return False      
   
# Bucle del juego
running = True
while running:

    # RGB, rojo, Verde y Amarillo
    screen.fill((0, 0, 0))
    # playerY -= 0.1
    
    # agregando el background
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # si se presiona una tecla, verifique si es derecha o izquierda
        if event.type == pygame.KEYDOWN:
            # print('Presente movimiento de teclas')
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    # obtener la coordenada x actual de la nave espacial
                    bulletX = playerX
                    fire_bullet(playerX, bulletY)
                
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # comprobar los límites o la nave espacial para que no se salga de los límites
    playerX += playerX_change
  
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Movieminetos de los enemigos, iagual comprobar los límites del enemigo para que no se salga de los límites
    for i in range(num_of_enemies):
        
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]
            
        # Colisión
        collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score += 1  
            print(score)  
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150) 
            
        enemy(enemyX[i], enemyY[i], i)
        
    # Bullet movimientos   
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
        
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
     
     
    
    player(playerX, playerY)
    
    pygame.display.update()

