import pygame
import time

pygame.init()

WINDOW_RESOLUTION = (1024, 1024)
image_resolution = [16, 16]
transform_resolution = (WINDOW_RESOLUTION[0] / image_resolution[0], WINDOW_RESOLUTION[1] / image_resolution[1])
display = pygame.display.set_mode(WINDOW_RESOLUTION, pygame.RESIZABLE)
pygame.display.set_caption(__file__.split("\\")[-1])

run = True
time_prev = time.time()
clock = pygame.time.Clock()

# Colors
color_black = (0, 0, 0)
color_white = (255, 255, 255)
color_red = (255, 0, 0)
color_yellow = (255, 255, 0)
color_green = (0, 255, 0)
color_cyan = (0, 255, 255)
color_blue = (0, 0, 255)

# Text
pygame.font.init()
fps_font = pygame.font.SysFont(None, WINDOW_RESOLUTION[1] // 32)
font = pygame.font.SysFont(None, int(transform_resolution[1] / 4))


def show_fps(delta_time, text_color=(0, 255, 0), outline_color=(0, 0, 0)):
    fps_text = fps_font.render(f"FPS: {int(1 / delta_time)}", True, text_color)
    fps_outline = fps_font.render(f"FPS: {int(1 / delta_time)}", True, outline_color)
    display.blit(fps_outline, (-1, -1))
    display.blit(fps_outline, (-1, 1))
    display.blit(fps_outline, (1, -1))
    display.blit(fps_outline, (1, 1))
    display.blit(fps_text, (0, 0))


class Node:
    def __init__(self, pos, g=0, end_pos=[0, 0], passable=True, cost=1, start=False, end=False, draw_text=True):
        self.pos = list(pos)
        self.g = g
        self.end_pos = end_pos
        self.passable = passable
        self.cost = cost
        self.start = start
        self.end = end
        self.draw_text = draw_text
        self.h = abs(self.end_pos[0] - self.pos[0]) + abs(self.end_pos[1] - self.pos[1])
        self.f = self.g + self.h
        self.color = color_green if start else color_red if end else color_cyan

    def create_children(self):
        positions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        children = []
        for pos in positions:
            x = self.pos[0] + pos[0]
            y = self.pos[1] + pos[1]
            add_child = True
            node_cost = self.cost
            for node in nodes:
                if node.pos[0] == x and node.pos[1] == y and not node.passable:
                    add_child = False
                node_cost = node.cost
            if add_child:
                children.append(Node([x, y], self.g + node_cost, self.end_pos, False))
        return sorted(children, key=lambda node: node.f)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color,
                         [self.pos[0] * transform_resolution[0], self.pos[1] * transform_resolution[1],
                          *transform_resolution])
        if self.draw_text:
            stats = [font.render(f"g = {self.g}", True, color_blue),
                     font.render(f"h = {self.h}", True, color_blue),
                     font.render(f"f = {self.f}", True, color_blue),
                     font.render(f"pos = {', '.join(map(str, self.pos))}", True, color_blue)]
            for i, stat in enumerate(stats):
                display.blit(stat, [self.pos[0] * transform_resolution[0] + 2,
                                    self.pos[1] * transform_resolution[1] + i * transform_resolution[1] / 4 +
                                    transform_resolution[1] / 16])


def set_start_and_end(start, end):
    return [Node(start, start=True, passable=False, end_pos=end), Node(end, end=True, passable=True, end_pos=end)]


start = [1, 1]
end = [11, 12]
nodes = set_start_and_end(start, end)

def search(start, end, nodes: [Node]):
    children = nodes[0].create_children()
    search = True
    while search:
        nodes += children
        children = children[0].create_children()
        for child in children:
            print(child.pos)
            if child.pos == end:
                search = False
                break

        for node in nodes:
            node.draw(display)
            pygame.display.update()
        time.sleep(0.5)

search([1,1], [11,12], nodes)


while run:

    # Calculate dt
    time_now = time.time()
    dt = time_now - time_prev
    time_prev = time_now

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Resize window event
        if event.type == pygame.VIDEORESIZE:
            display = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

        # Keypresses
        # if event.type == pygame.KEYDOWN:
        # if event.key == pygame.K_1:

        mouse_pos = pygame.mouse.get_pos()
        mouse_pos = [mouse_pos[0] // transform_resolution[0], mouse_pos[1] // transform_resolution[1]]

        # if pygame.mouse.get_pressed()[0]:
        #     add = True
        #     for node in nodes:
        #         if node.pos == mouse_pos:
        #             add = False
        #             break
        #     if add:
        #         nodes.append(Node(mouse_pos))

    display.fill((29, 29, 29))

    pygame.draw.rect(display, (40, 40, 40),
                     [mouse_pos[0] * transform_resolution[0], mouse_pos[1] * transform_resolution[1],
                      *transform_resolution])

    for node in nodes:
        node.draw(display)

    # Grid
    for i in range(image_resolution[0]):
        for j in range(image_resolution[1]):
            pygame.draw.line(display, color_black, [i * transform_resolution[0], 0],
                             [i * transform_resolution[0], WINDOW_RESOLUTION[1]])
            pygame.draw.line(display, color_black, [0, j * transform_resolution[1]],
                             [WINDOW_RESOLUTION[0], j * transform_resolution[1]])

    show_fps(dt)
    pygame.display.update()
    clock.tick(480)
