import pygame
import sys
import random
import pdb
pygame.init()
x = 900
y = 600
player_health = 100
player_x = x // 2
player_y = y // 2
clock = pygame.time.Clock()
player_img = pygame.image.load("images/Player.png")
bg_img = pygame.image.load("images/grey.jpg")
step_sound = pygame.mixer.Sound("sounds/step.mp3")
playerstep = 5
step_sound_cooldown = 700
screen = pygame.display.set_mode((x, y))
last_step_sound = pygame.time.get_ticks()
pygame.display.set_caption("Random game")
class Zombie():
    def __init__(self):
        self.image = pygame.image.load("images/Zombie.jpg")
        self.x = 500
        self.y = 500
        self.speed = 2
    def movement(self, player_x, player_y):
        if self.x < player_x:
            self.x += self.speed
        elif self.x > player_x:
            self.x -= self.speed
        if self.y < player_y:
            self.y += self.speed
        elif self.y > player_y:
            self.y -= self.speed
    def image_blit(self, screen):
        screen.blit(self.image,(self.x, self.y))

def player_movement(x,y,playerstep,step_sound,current_time,last_step_sound,step_sound_cooldown):
    # Handle movement on key press inside event loop
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:    
        x -= playerstep 
        if current_time - last_step_sound > step_sound_cooldown:
            step_sound.play()
            last_step_sound = current_time
    if keys[pygame.K_RIGHT]:
        x += playerstep
        if current_time - last_step_sound > step_sound_cooldown:
            step_sound.play()
            last_step_sound = current_time

    if keys[pygame.K_UP]:
        y += -playerstep
        if current_time - last_step_sound > step_sound_cooldown:
            step_sound.play()
            last_step_sound = current_time
    if keys[pygame.K_DOWN]:
        y += playerstep
        if current_time - last_step_sound > step_sound_cooldown:
            step_sound.play()
            last_step_sound = current_time


    # Boundary checks
    if x > 854:
        x = 854
    if x < 0:
        x = 0
    if y > 545:
        y = 545
    if y < 0:
        y = 0
    return x,y,last_step_sound,current_time

zombie = Zombie()
while True:
    # noinspection PyRedeclaration
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(bg_img,(0,0))
    screen.blit(player_img,(player_x,player_y))

    player_x,player_y,last_step_sound,current_time = player_movement(player_x,player_y,playerstep,step_sound,current_time,
    last_step_sound,step_sound_cooldown)

    zombie.image_blit(screen)
    zombie.movement(player_x,player_y)





    pygame.display.flip()
    clock.tick(60)