import pygame
import random
import sys

pygame.init()
width, height = 700, 700
surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Sand Simulation')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SAND = (187, 117, 37)

SAND_CELL_WIDTH = 5
SAND_CELL_HEIGHT = 5

class SandCell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = SAND_CELL_WIDTH
        self.height = SAND_CELL_HEIGHT

def draw_window(moving_sand, sand_map):
    surface.fill(BLACK)

    for sand in moving_sand :
        rect = pygame.Rect(sand.x * SAND_CELL_WIDTH, sand.y * SAND_CELL_HEIGHT, sand.width, sand.height)
        pygame.draw.rect(surface, SAND, rect)

    for y in range(height // SAND_CELL_HEIGHT):
        for x in range(width // SAND_CELL_WIDTH):
            if sand_map[y][x] == 'X':
                rect = pygame.Rect(x * SAND_CELL_WIDTH, y * SAND_CELL_HEIGHT, SAND_CELL_WIDTH, SAND_CELL_HEIGHT)
                pygame.draw.rect(surface, SAND, rect) 

    pygame.display.update()

def is_sand_here(sand_map, x, y):
    if y < 0 or y >= (height // SAND_CELL_HEIGHT):
        return True

    if x < 0 or x >= (width // SAND_CELL_WIDTH):
        return True

    return sand_map[y][x] == 'X'

def main():
    sand_map = []
    moving_sand = []
    rand_n = 0

    clock = pygame.time.Clock()
    fps = 40

    for y in range(height // SAND_CELL_HEIGHT):
        sand_map.append([])
        for x in range(width // SAND_CELL_WIDTH):
            sand_map[y].append('.')

    adding = False

    while True:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                adding = True

            if event.type == pygame.MOUSEBUTTONUP:
                adding = False;

        if adding:
            pos = pygame.mouse.get_pos()
            x = pos[0] // SAND_CELL_WIDTH
            y = pos[1] // SAND_CELL_HEIGHT
            if not is_sand_here(sand_map, x, y):
                sand = SandCell(x, y)
                moving_sand.append(sand)

        for sand in moving_sand:
            if not is_sand_here(sand_map, sand.x, sand.y + 1):
                sand.y += 1
            elif not is_sand_here(sand_map, sand.x - 1, sand.y + 1) or not is_sand_here(sand_map, sand.x + 1, sand.y + 1):
                sand.y += 1
                if not is_sand_here(sand_map, sand.x - 1, sand.y) and is_sand_here(sand_map, sand.x + 1, sand.y):
                    sand.x -= 1
                elif is_sand_here(sand_map, sand.x - 1, sand.y) and not is_sand_here(sand_map, sand.x + 1, sand.y):
                    sand.x += 1
                else:
                    rand_n = random.choice([-1, 1])
                    sand.x += rand_n
            else:
                moving_sand.remove(sand)
                sand_map[sand.y][sand.x] = 'X'

        draw_window(moving_sand, sand_map)

if __name__ == '__main__':
    main()
