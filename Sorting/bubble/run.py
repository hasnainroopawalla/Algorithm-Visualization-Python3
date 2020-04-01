import pygame
import random
import bubble
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

# Initialize Screen
SCREEN_WIDTH = NUMBER_OF_ELEMENTS
SCREEN_HEIGHT = NUMBER_OF_ELEMENTS

FPS = 60
pygame.init()

font = pygame.font.Font("freesansbold.ttf", 15)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bubble Sort")
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
                plotnum = bubble.sortnum(num)
                
    screen.fill(WHITE)

    # pygame.draw.rect(screen, GREEN, addnodebutton)
    # screen.blit(font.render('Press Enter to start sorting', True, (0,0,0)), (800, 557))
    # screen.blit(font.render('Press Space to shuffle numbers', True, (0,0,0)), (767, 579))
    if c==0:
        for i in range(len(num)):
            pygame.draw.line(screen, (255,0,0), (i, SCREEN_HEIGHT), (i, SCREEN_HEIGHT-num[i]))

    else:
        for i in plotnum:
            for j in range(len(i)):
                pygame.draw.line(screen, (255,0,0), (j, SCREEN_HEIGHT), (j, SCREEN_HEIGHT-i[j]))
                pygame.display.flip()
            screen.fill(WHITE)
            #time.sleep(0.05)
        c = 0
        print('Sorted')

    pygame.display.flip()
    clock.tick(FPS)
 
pygame.quit()
