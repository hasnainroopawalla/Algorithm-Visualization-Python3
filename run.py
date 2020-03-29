import pygame

# --- constants --- (UPPER_CASE names)


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


# rectangle = pygame.rect.Rect(176, 134, 37, 37)
# rectangle_draging = False

# rectangle2 = pygame.rect.Rect(270, 134, 37, 37)
# rectangle2_draging = False

addnode = pygame.rect.Rect(750, 550, 37, 37)  # Add Node Button

clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if addnode.collidepoint(event.pos):  # Add Node Button
                    print('add')

                elif rectangle.collidepoint(event.pos):
                    rectangle_draging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = rectangle.x - mouse_x
                    offset_y = rectangle.y - mouse_y
                elif rectangle2.collidepoint(event.pos):
                    rectangle2_draging = True
                    mouse_x, mouse_y = event.pos
                    offset_x = rectangle2.x - mouse_x
                    offset_y = rectangle2.y - mouse_y

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:            
                rectangle_draging = False           
                rectangle2_draging = False

        elif event.type == pygame.MOUSEMOTION:
            if rectangle_draging:
                mouse_x, mouse_y = event.pos
                rectangle.x = mouse_x + offset_x
                rectangle.y = mouse_y + offset_y
            elif rectangle2_draging:
                mouse_x, mouse_y = event.pos
                rectangle2.x = mouse_x + offset_x
                rectangle2.y = mouse_y + offset_y

    # - updates (without draws) -

    # empty

    # - draws (without updates) -

    screen.fill(WHITE)

    pygame.draw.rect(screen, RED, rectangle)
    pygame.draw.rect(screen, BLUE, rectangle2)
    pygame.draw.rect(screen, GREEN, addnode)


    pygame.display.flip()



    clock.tick(FPS)


pygame.quit()
