import pygame 
import random
from pygame import mixer
from enum import Enum

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Tanks')
FPS = 30

clock = pygame.time.Clock()

f1 = pygame.font.SysFont(None, 30)
text1 = f1.render(":Lives", 1, (255, 17, 0))

f2 = pygame.font.SysFont(None, 30)
text2 = f2.render(":Lives", 1, (100, 150, 250 ))
sound1=r'C:\Users\Аида\Documents\python\tanksgame\start.wav'
pygame.mixer.music.load(sound1)
pygame.mixer.music.play(-1)
sound2=r'C:\Users\Аида\Documents\python\tanksgame\boom.wav'
#pygame.mixer.Sound(sound2).play()
sound3=r'C:\Users\Аида\Documents\python\tanksgame\bullet.wav'
#pygame.mixer.Sound(sound3).play()


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
   
class Bullet:

    def __init__(self, bx, by, bcolor, bspeed):
        self.bx = bx
        self.by = by
        self.bxspeed = bspeed
        self.byspeed = bspeed
        self.bcolor = bcolor
        self.run = False
        self.r = 5

    def draw(self):
        pygame.draw.circle(screen, self.bcolor, (self.bx, self.by), self.r)
        
  
    def shoot(self):
        if a.direction == Direction.RIGHT:
            self.bx = a.x + 60
            self.by = a.y + 20
            self.bxspeed = 10
            self.byspeed = 0
            self.run = True
                
        if a.direction == Direction.LEFT:
            self.bx = a.x - 20
            self.by = a.y + 20
            self.bxspeed = -10
            self.byspeed = 0
            self.run = True
                
        if a.direction == Direction.UP:
            self.bx = a.x + 20
            self.by = a.y - 20
            self.bxspeed = 0
            self.byspeed = -10
            self.run = True
                
        if a.direction == Direction.DOWN:
            self.bx = a.x + 20
            self.by = a.y + 60
            self.bxspeed = 0
            self.byspeed = 10
            self.run = True
        
    def popadanie(self):
# стрельба снизу
        if (-45<=(a.x - self.bx)<= 10) and (-45<=(a.y-self.by)<= 45):    
            self.run = False
            a.score -= 1
            pygame.mixer.Sound(sound2).play()
            #sound2.play()
# стрельба сверху
        elif (-45<=(a.x - self.bx)<= 10) and (-45<=(a.y-self.by)<= 10):
            self.run = False
            a.score -= 1
            pygame.mixer.Sound(sound2).play()
            #sound2.play()
# стрельба слева
        elif (-45<=(a.x - self.bx)<= 10) and (-10<=(a.y-self.by)<= 45):
            self.run = False
            a.score -= 1
            pygame.mixer.Sound(sound2).play()
            #sound2.play()
# стрельба справа
        elif (-45<=(a.x - self.bx)<= 10) and (-45<=(a.y-self.by)<= 10):
            self.run = False
            a.score -= 1
            pygame.mixer.Sound(sound2).play()
            #sound2.play()
# вышел за поле
        elif self.bx > 800 or self.bx < 0 or self.by <0 or self.by > 600:
            self.run = False


bullet1 = Bullet(850, 850, (193, 0, 32), 10)
bullet2 = Bullet(850, 850, (193, 0, 32), 10)
bullets = [bullet1, bullet2]

class Tank:
    global score
    def __init__(self, x, y, speed, color, score, d_right = pygame.K_RIGHT, d_left = pygame.K_LEFT, d_up = pygame.K_UP, d_down = pygame.K_DOWN):
        self.x = x
        self.y = y
        self.speed = speed
        self.color = color
        self.width = 45
        self.direction = Direction.RIGHT
        self.KEY = {d_right: Direction.RIGHT, d_left: Direction.LEFT, d_up: Direction.UP, d_down: Direction.DOWN} 
        self.score = score

    def draw(self):
        tank_c = (self.x + int(self.width/2), self.y + int(self.width/2))
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.width), 2)
        pygame.draw.circle(screen, self.color, tank_c, int(self.width/2))

        if self.direction == Direction.RIGHT:
            pygame.draw.line(screen, self.color, tank_c, (self.x + self.width + int(self.width/2), self.y + int(self.width/2)), 4)
        if self.direction == Direction.LEFT:
            pygame.draw.line(screen, self.color, tank_c, (self.x - int(self.width/2), self.y + int(self.width/2)), 4)
        if self.direction == Direction.UP:
            pygame.draw.line(screen, self.color, tank_c, (self.x + int(self.width/2), self.y - int(self.width/2)), 4)
        if self.direction == Direction.DOWN:
            pygame.draw.line(screen, self.color, tank_c, (self.x + int(self.width/2), self.y + self.width + int(self.width/2)), 4)
        

    def change_direction(self, direction):
        self.direction = direction

    def move(self):
        if self.direction == Direction.LEFT:
            self.x -= self.speed
        if self.direction == Direction.RIGHT:
            self.x += self.speed
        if self.direction == Direction.UP:
            self.y -= self.speed
        if self.direction == Direction.DOWN:
            self.y += self.speed
        if self.x > 770:
            self.x = 0
        if self.x < 0:
            self.x = 740
        if self.y < 0:
            self.y = 600
        if self.y > 600:
            self.y = 0
        self.draw()
        


mainloop = True
tank1 = Tank(300, 300, 2, (255, 17, 0), 3)
tank2 = Tank(100, 100, 2, (100, 150, 250), 3, pygame.K_d, pygame.K_a, pygame.K_w, pygame.K_s)
n = [tank1, tank2]


while mainloop:
    mill = clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False
            
            if event.key in tank1.KEY.keys():
                tank1.change_direction(tank1.KEY[event.key])
            if event.key in tank2.KEY.keys():
                tank2.change_direction(tank2.KEY[event.key])
        
            
    screen.fill((0, 0, 0))
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE and not bullet2.run:
            a = n[1]
            bullet2.shoot()
            pygame.mixer.Sound(sound3).play()
        if event.key == pygame.K_RETURN and not bullet1.run:
            a = n[0]
            bullet1.shoot()
            pygame.mixer.Sound(sound3).play()
            
    if bullet1.run == True:
        bullet1.bx += bullet1.bxspeed
        bullet1.by += bullet1.byspeed
        bullet1.draw()
        a = n[1]
        bullet1.popadanie()
        pygame.mixer.Sound(sound3).play()
        
        
    if bullet2.run == True:
        bullet2.bx += bullet2.bxspeed
        bullet2.by += bullet2.byspeed
        bullet2.draw()
        a = n[0]
        bullet2.popadanie()
        pygame.mixer.Sound(sound3).play()
        
    l1 = pygame.font.SysFont(None, 30)
    score1 = f1.render(str(tank1.score), 1, (255, 17, 0))
    l2 = pygame.font.SysFont(None, 30)
    score2 = f2.render(str(tank2.score), 1, (100, 150, 250))
    if tank1.score==0: 
        mainloop=False
    elif tank2.score==0:
        mainloop= False


    tank1.move()
    tank2.move()
    
    
    screen.blit(text1, (110, 550))
    screen.blit(text2, (700, 550))
    screen.blit(score1, (90, 550))
    screen.blit(score2, (680, 550))
    pygame.display.flip()

