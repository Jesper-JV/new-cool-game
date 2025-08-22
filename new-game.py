import pygame
import sys
import random
import pdb
import math
square_root = math.sqrt(0)
pygame.init()
white = (0,0,0)
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
step_sound_cooldown = 600
screen = pygame.display.set_mode((x, y))
last_step_sound = pygame.time.get_ticks()
pygame.display.set_caption("Random game")

# noinspection PyShadowingNames
class Zombie:
    def __init__(self):
        self.image = pygame.image.load("images/Zombie.jpg")
        self.x = 500
        self.y = 500
        self.speed = 2

    # noinspection PyShadowingNames
    def movement(self, player_x, player_y,player_health):
        if self.x < player_x:
            self.x += self.speed
        elif self.x > player_x:
            self.x -= self.speed
        if self.y < player_y:
            self.y += self.speed
        elif self.y > player_y:
            self.y -= self.speed
        if player_x + 50 > self.x > player_x - 50 and player_y + 50 > self.y > player_y - 50 and player_health > 0:
            player_health -= 1
        return player_health
    def image_blit(self, screen):
        screen.blit(self.image,(self.x, self.y))

class Text:
    def __init__(self,size,text,color,x,y,font='freesansbold.ttf'):
        self.font = pygame.font.SysFont(font,size)
        self.text = self.font.render(text, True,color)
        self.text_rect = self.text.get_rect(center=(x,y))
    def image_blit(self,screen):
        screen.blit(self.text,self.text_rect)
    def refresh_text(self,text,color):
        self.text = self.font.render(str(text), True,color)

def player_movement(x, y, playerstep, step_sound, current_time, last_step_sound, step_sound_cooldown):
    keys = pygame.key.get_pressed()
    moving = False  # Flag to check if player moved

    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        moving = True
        if keys[pygame.K_UP] or keys[pygame.K_DOWN]:
            x -= math.sqrt(playerstep * 2)
        else:
            x -= playerstep

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        moving = True
        if keys[pygame.K_UP] or keys[pygame.K_DOWN]:
            x += math.sqrt(playerstep * 2)
        else:
            x += playerstep

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        moving = True
        if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
            y -= math.sqrt(playerstep * 2)
        else:
            y -= playerstep

    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        moving = True
        if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
            y += math.sqrt(playerstep * 2)
        else:
            y += playerstep

    # Only play sound if moving and cooldown passed
    if moving and (current_time - last_step_sound > step_sound_cooldown):
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

    return x, y, last_step_sound, current_time

player_health_text = Text(30,str(player_health),white,740,20)
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

    player_health_text.image_blit(screen)
    player_health_text.refresh_text("player health: " + str(player_health),white)

    zombie.image_blit(screen)
    player_health = zombie.movement(player_x,player_y,player_health)

    pygame.display.flip()
    clock.tick(60)