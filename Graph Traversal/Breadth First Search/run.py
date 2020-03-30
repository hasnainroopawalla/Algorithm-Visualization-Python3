import pygame
import random
import bfs

nodes = []
nodes_text = []
graph = {}
source = ''
destination = ''

def createlink(slink, dlink):
    if dlink not in graph[slink]:
        graph[slink].append(dlink)
    
        if slink not in graph[dlink]:
            graph[dlink].append(slink)
       
        return 1
    else:
        return 'Route Exists'

    
    
def getpath():
    print()

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
    txt = chr(len(nodes)+65)
    rectangle = pygame.rect.Rect(x, y, 37, 37) 

    node_text = font.render(txt, True, (0,0,0))
    nodes_text.append({'text':node_text, 'dragging':False, 'pos':(x+12, y+12), 'id':txt})
    nodes.append({'rect':rectangle, 'dragging':False, 'color':color, 'id':txt})

    graph[txt] = []
 

# Initialize Screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WHITE = (255, 255, 255)
RED   = (255, 0, 0)
GREEN   = (0, 255, 0)
BLUE   = (0, 0, 255)

FPS = 60
pygame.init()
font = pygame.font.Font("freesansbold.ttf", 15)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Breadth First Search")
addnodebutton = pygame.rect.Rect(740, 555, 50, 37)  # Add Node Button
# Initialize Screen

c = 0
result = []
clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():

        mx, my = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:

                if addnodebutton.collidepoint(event.pos):  # Add Node Button
                    addnode()

                else:  # Dragging
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
    
                        for t in nodes_text:  # Move Text
                            if (t['id']==node['id']):
                                t['pos'] = (node['rect'][0]+12, node['rect'][1]+12)
                                break

        elif event.type == pygame.MOUSEMOTION:
            for node in nodes:
                if node['dragging']:
                    mouse_x, mouse_y = event.pos
                    node['rect'].x = mouse_x + offset_x
                    node['rect'].y = mouse_y + offset_y
        
    
        elif event.type == pygame.KEYDOWN:

            if pygame.key.name(event.key)=='space':
                print(graph)

            elif pygame.key.name(event.key)=='return':
                result = bfs.bfs_shortest_path(graph, source, destination)
               

            elif pygame.key.name(event.key)=='s': # SELECT SOURCE
                for node in nodes:
                    if node['rect'].collidepoint((mx, my)):
                        source = node['id']
                        print('source set:',source)


            elif pygame.key.name(event.key)=='d':  # SELECT DESTINATION
                for node in nodes:
                    if node['rect'].collidepoint((mx, my)):
                            destination = node['id']
                            print('destination set:',destination)

            elif pygame.key.name(event.key)=='l':
                for node in nodes:
                    if node['rect'].collidepoint((mx, my)):

                        if c==1:
                            dlink = node['id']
                            createlink(slink, dlink)
                            c = 0
                        else:
                            slink = node['id']
                            c+=1

    screen.fill(WHITE)

    pygame.draw.rect(screen, GREEN, addnodebutton)
    screen.blit(font.render('Source: '+source, True, (0,0,0)), (654, 557))
    screen.blit(font.render('Destination: '+destination, True, (0,0,0)), (620, 579))
    screen.blit(font.render('ADD', True, (0,0,0)), (746, 567))

    for i in nodes:
        pygame.draw.rect(screen, i['color'], i['rect'])
        
    for i in nodes_text:
        screen.blit(i['text'], i['pos'])


    
    for i in graph:  # Draw Links
        for node in nodes:   # get coordinates
            if(node['id']==i):
                sx, sy = node['rect'][0], node['rect'][1]
                break
        for j in graph[i]:
            for node in nodes:   # get coordinates
                if(node['id']==j):
                    dx, dy = node['rect'][0],node['rect'][1]
                    break      
            pygame.draw.line(screen, (0,0,0), (sx, sy), (dx, dy))

    if result:
        for i in range(len(result)):
            if (i==len(result)-1):
                break
            else:
                for node in nodes:   # get coordinates
                    if(node['id']==result[i]):
                        sx, sy = node['rect'][0], node['rect'][1]
                        break
                
                for node in nodes:   # get coordinates
                    if(node['id']==result[i+1]):
                        dx, dy = node['rect'][0], node['rect'][1]
                        break
            
                pygame.draw.line(screen, (255,0,0), (sx, sy), (dx, dy))
            

            #result = []


    pygame.display.flip()
    clock.tick(FPS)
 
pygame.quit()
