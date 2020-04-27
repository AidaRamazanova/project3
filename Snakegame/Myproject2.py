import pygame
import random

pygame.init()
pygame.display.set_caption('Snakegame')
screen = pygame.display.set_mode((600, 600))
score_sur = pygame.Surface((120,20))
score_shrift = pygame.font.Font(None, 30)

backgroundImage = pygame.image.load("background.jpg")
foodImage = pygame.image.load("food.png")
endgameImage = pygame.image.load("endgame.jpg")




class Snake:
    def __init__(self):
        self.size=1
        self.elements=[[100, 100]]
        self.radius=10
        self.dx=5 #направо
        self.dy=0
        self.is_add = False
        self.score=0
        

    def draw(self):
        for element in self.elements:
            pygame.draw.circle(screen,(250, 0, 0), element, self.radius)

    def add_to_snake(self):
        self.size +=1
        self.elements.append([0, 0])
        self.is_add = False

    def move(self):
        if self.is_add:
            self.add_to_snake()
        
        for i in range(self.size -1, 0, -1):
            self.elements[i][0] = self.elements[i-1][0]
            self.elements[i][1] = self.elements[i-1][1]

        self.elements[0][0] +=self.dx
        self.elements[0][1] +=self.dy

class Food:
    def __init__(self):
        self.x=random.randint(20,590)
        self.y=random.randint(20,580)
    def draw(self):
        screen.blit(foodImage, (self.x, self.y))    
def Collision():
     if (food.x>= snake.elements[0][0]-20 and food.x<snake.elements[0][0]+20) and  (food.y >= snake.elements[0][1] -20 and food.y<snake.elements[0][1] +20):
        snake.is_add = True  
        if snake.is_add == True:
            snake.score += 1
            food.x = random.randint(10, 550)
            food.y = random.randint(10, 580)  

def Score(x,y,score):
    score_sur.fill((0,0,0))
    score_sur.blit(score_shrift.render("SCORE:"+str(snake.score), 1, (255,255,255)), (0,0))
    screen.blit(score_sur,(0,0))


def border():
        if snake.elements[0][0]>=600 or snake.elements[0][0]<=20 or snake.elements[0][1]<=20 or snake.elements[0][1]>=590:
            return True
        return False  

def endgame():
    snake.dx=0
    snake.dy=0
    snake.radius=0            

snake = Snake()
food=Food()
running = True

d = 10

FPS = 30
score=0

clock = pygame.time.Clock()

k1_pressed = False

while running:
    mill = clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False
        if event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                 running = False
            if event.key == pygame.K_RIGHT:
                snake.dx = d
                snake.dy = 0
            if event.key == pygame.K_LEFT:
                snake.dx =-d
                snake.dy = 0
            if event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -d
            if event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = d
            if event.key == pygame.K_1:
                snake.is_add = True
            if border():
                endgame()
                backgroundImage=endgameImage
        



        screen.blit(backgroundImage, (0, 0))
        snake.move()
        
        Collision()
        food.draw()
        snake.draw()
        Score(0,0,score)
        pygame.display.flip()

        
        clock.tick(15)