import pygame

# Solid colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)

# Textures
GRASS = pygame.image.load("resources\\grass.png")
DIRT = pygame.image.load("resources\\dirt.png")
STONE = pygame.image.load("resources\\stone.png")
DEEPSLATE = pygame.image.load("resources\\deepslate.png")
BEDROCK = pygame.image.load("resources\\bedrock.png")
ICE = pygame.image.load("resources\\ice.png")
GLASS = pygame.image.load("resources\\glass.png")

TOP_LAYERS = [1, 2]

BOTTOM_LAYERS = [1, 2]


def main():
    print(__file__.split("\\")[-1])


if __name__ == "__main__":
    main()
