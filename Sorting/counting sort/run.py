import pygame
import random
import countingsort
import time

num = []
plotnum = []
NUMBER_OF_ELEMENTS = 200

def genlist():
    num = []
    for i in range(1, NUMBER_OF_ELEMENTS+1):
        num.append(i)
    random.shuffle(num)
    return num

WHITE = (255, 255, 255)
RED = (255,0,0)

# Initialize Screen
SCREEN_WIDTH = NUMBER_OF_ELEMENTS
SCREEN_HEIGHT = NUMBER_OF_ELEMENTS

FPS = 60
pygame.init()

font = pygame.font.Font("freesansbold.ttf", 15)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Counting Sort")
# Initialize Screen

clock = pygame.time.Clock()

running = True
c = 0

while running:

    for event in pygame.event.get():

        mx, my = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if pygame.key.name(event.key)=='space':
                num = genlist()

            if pygame.key.name(event.key)=='return':
                c = 1
                start = time.time()
                plotnum = countingsort.sortnum(num,max(num))
                end = time.time()
                
    screen.fill(WHITE)

    if c==0:
        for i in range(len(num)):
            pygame.draw.line(screen, RED, (i, SCREEN_HEIGHT), (i, SCREEN_HEIGHT-num[i]))

    else:
        for i in plotnum:
            for j in range(len(i)):
                pygame.draw.line(screen, RED, (j, SCREEN_HEIGHT), (j, SCREEN_HEIGHT-i[j]))
                pygame.display.flip()
            screen.fill(WHITE)
        c = 0
        print('\nCounting Sort:-\nNumber of Elements:',NUMBER_OF_ELEMENTS, '. Time Taken:', round(end-start,4),'sec')

    pygame.display.flip()
    clock.tick(FPS)
 
pygame.quit()
