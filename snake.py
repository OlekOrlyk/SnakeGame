import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
screen_width = 50
segment_width = 10
segment_height = 10

segment_margin = 3

x_change = 0
y_change = 1


def to_screen(number):
    return number * (segment_height + segment_margin)


def has_hit(snake_segments, x, y):
    for segment in snake_segments:
        if segment.x == x and segment.y == y:
            return True
    return False


class Segment(pygame.sprite.Sprite):
    def __init__(self, colour=WHITE):
        super(Segment, self).__init__()
        self.x = 0
        self.y = 0
        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(colour)

        self.rect = self.image.get_rect()

    def move(self, x, y):
        self.x = x
        self.y = y
        self.rect.x = to_screen(x)
        self.rect.y = to_screen(y)
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont( "monospace", 15)


food = Segment(RED)
food.move(10, 10)
screen = pygame.display.set_mode([to_screen(screen_width), to_screen(screen_width)])

pygame.display.set_caption('Snake Example')
allspriteslist = pygame.sprite.Group()
foodlist = pygame.sprite.Group()
foodlist.add(food)
snake_segments = []
for i in range(2):
    segment = Segment()
    segment.move(i, 2)
    snake_segments.append(segment)
    allspriteslist.add(segment)
clock = pygame.time.Clock()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x_change == 0:
                x_change = -1
                y_change = 0

            if event.key == pygame.K_RIGHT and x_change == 0:
                x_change = 1
                y_change = 0
            if event.key == pygame.K_UP and y_change == 0:
                x_change = 0
                y_change = -1
            if event.key == pygame.K_DOWN and y_change == 0:
                x_change = 0
                y_change = 1

    x = snake_segments[0].x + x_change
    y = snake_segments[0].y + y_change

    if x == -1:
        x = 49
    if x == 50:
        x = 0

    if y == -1:
        y = 49
    if y == 50:
        y = 0

    segment = Segment()
    segment.move(x, y)

    if has_hit(snake_segments, x, y):
        pygame.quit()

    snake_segments.insert(0, segment)
    allspriteslist.add(segment)

    if food.x == x and food.y == y:
        food.move(random.randint(0, screen_width - 1), random.randint(0, screen_width - 1))
    else:
        old_segment = snake_segments.pop()
        allspriteslist.remove(old_segment)

    screen.fill(BLACK)
    label = myfont.render("Score:"+ str((len(snake_segments)-2) *7),1, (255,255,0))
    screen.blit(label, (0, 0))
    allspriteslist.draw(screen)
    foodlist.draw(screen)

    pygame.display.flip()

    clock.tick(10)
pygame.quit()
