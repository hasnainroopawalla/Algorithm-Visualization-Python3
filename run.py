import pygame
import random

nodes = []
nodes_dragging = []

def randomcolor():
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255) 
    return (r, g, b)

def randomposition():
    x = random.randrange(0, 750)
    y = random.randrange(0, 550)
    return x, y

def addnode():
    x, y = randomposition()
    color = randomcolor()
    rectangle = pygame.rect.Rect(x, y, 37, 37)
    rect = {'rect':rectangle, 'dragging':False, 'color':color}
    nodes.append(rect)


# Initialize Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WHITE = (255, 255, 255)
RED   = (255, 0, 0)
GREEN   = (0, 255, 0)
BLUE   = (0, 0, 255)

FPS = 60
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Graph")
# Initialize Screen


addnodebutton = pygame.rect.Rect(750, 550, 37, 37)  # Add Node Button

clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:

                if addnodebutton.collidepoint(event.pos):  # Add Node Button
                    addnode()

                else:
                    for node in nodes:
                        if node['rect'].collidepoint(event.pos):
                            node['dragging'] = True
                            mouse_x, mouse_y = event.pos
                            offset_x = node['rect'].x - mouse_x
                            offset_y = node['rect'].y - mouse_y

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:            
                for node in nodes:
                    if node['rect'].collidepoint(event.pos):
                        node['dragging'] = False

        elif event.type == pygame.MOUSEMOTION:
            for node in nodes:
                if node['dragging']:
                    mouse_x, mouse_y = event.pos
                    node['rect'].x = mouse_x + offset_x
                    node['rect'].y = mouse_y + offset_y

    screen.fill(WHITE)

    pygame.draw.rect(screen, GREEN, addnodebutton)

    for i in nodes:
        pygame.draw.rect(screen, i['color'], i['rect'])


    pygame.display.flip()



    clock.tick(FPS)


pygame.quit()
