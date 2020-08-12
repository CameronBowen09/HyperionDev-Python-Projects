import pygame # Imports a game library that lets you use specific functions in your program.
import random # Import to generate random numbers.

#Initialize the pygame models
pygame.init()

#A screen is being created here
screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

#This creates the player and the enemys 
player = pygame.image.load("Player.jpg")
enemy1 = pygame.image.load("Enemy.jpg")
enemy2 = pygame.image.load("Enemy2.jpg")
enemy3 = pygame.image.load("Enemy3.jpg")
reward = pygame.image.load("Reward.jpg")

#Resizing the images for the game
player = pygame.transform.scale(player,[150,150])
enemy1 = pygame.transform.scale(enemy1,[150,150])
enemy2 = pygame.transform.scale(enemy2,[150,150])
enemy3 = pygame.transform.scale(enemy3,[150,150])
reward = pygame.transform.scale(reward,[100,150])

#Store player, enemies and rewards width and height
player_height = player.get_height()
player_width = player.get_width()
enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width()
enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()
enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()
reward_height = reward.get_height()
reward_width = reward.get_width()

#Store the position of the player
playerXPosition = 100
playerYPosition = 50

#Store the position of the enemies
enemy1XPosition = screen_width
enemy1YPosition = random.randint(0, screen_height - enemy1_height)
enemy2XPosition = screen_width
enemy2YPosition = random.randint(0, screen_height - enemy2_height)
enemy3XPosition = screen_width
enemy3YPosition = random.randint(0, screen_height - enemy3_height)

#Store the position of the reward
rewardXPosition = screen_width
rewardYPosition = random.randint(0, screen_height - reward_height)

#Store boolean value for keys, checks if the keys are being pressed
KeyUp = False
KeyDown = False
KeyLeft = False
KeyRight = False

#This is a game loop that will continue to run unless user quits the game
while 1:
    screen.fill(0) #Clears the screen
    screen.blit(player, (playerXPosition, playerYPosition)) #This draws the player, enemies and reward at the position given to them
    screen.blit(enemy1, (enemy1XPosition, enemy1YPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    screen.blit(reward, (rewardXPosition, rewardYPosition))

    pygame.display.flip() #Updated the screen

    #This loops trough events in the game
    for event in pygame.event.get():

        #This event checks if the user quits the game, is so stop game
        if event.type == pygame.quit:
            pygame.quit()
            exit(0)

        #This even checks if the user has pressed the down key
        if event.type == pygame.KEYDOWN:
            #Test is the key pressed is the one wanted
            if event.key == pygame.K_UP:
                KeyUp = True
            if event.key == pygame.K_DOWN:
                KeyDown = True
            if event.key == pygame.K_LEFT:
                KeyLeft = True
            if event.key == pygame.K_RIGHT:
                KeyRight = True
        
        #This even checks if the key is up (Not pressed by user)
        if event.type == pygame.KEYUP:
            #Test if the key released is the one wanted
            if event.key == pygame.K_UP:
                KeyUp = False
            if event.key == pygame.K_DOWN:
                KeyDown = False
            if event.key == pygame.K_LEFT:
                KeyLeft = False
            if event.key == pygame.K_RIGHT:
                KeyRight = False

    if KeyUp == True:
        if playerYPosition > 0: #This makes sure that the user does not move the player above the window.
            playerYPosition -= 1
    if KeyDown == True:
        if playerYPosition < screen_height - player_height: #This makes sure that the user does not move the player below the window.
            playerYPosition += 1
    if KeyLeft == True:
        if playerXPosition > 0: #This makes sure the user does not move the player to far left 
            playerXPosition -= 1
    if KeyRight == True:
        if playerXPosition < screen_width - player_width: #This makes sure the user does not move the player to far right
            playerXPosition += 1
    
    #Bounding a box for the player
    playerBox = pygame.Rect(player.get_rect())
    playerBox.top = playerYPosition #This updates the box to move with the players actions
    playerBox.left = playerXPosition

    #Bounding a box for the ememies
    enemy1Box = pygame.Rect(enemy1.get_rect())
    enemy1Box.top = enemy1YPosition
    enemy1Box.left = enemy1XPosition
    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition
    enemy3Box = pygame.Rect(enemy2.get_rect())
    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition

    #Bounding a box for the reward
    rewardBox = pygame.Rect(reward.get_rect())
    rewardBox.top = rewardYPosition
    rewardBox.left = rewardXPosition

    #Test collision of the boxes
    if playerBox.colliderect(enemy1Box):
        print("You lose!")
        pygame.quit()
        exit(0)
    if playerBox.colliderect(enemy2Box):
        print("You lose!")
        pygame.quit()
        exit(0)
    if playerBox.colliderect(enemy3Box):
        print("You lose!")
        pygame.quit()
        exit(0)
    if playerBox.colliderect(rewardBox):
        print("You win!")
        pygame.quit()
        exit(0)
    
    #Make enemies approach the player
    enemy1XPosition -= 0.15
    enemy2XPosition -= 0.20
    enemy3XPosition -= 0.10

    #Make reward approach the player
    rewardXPosition -= 0.07