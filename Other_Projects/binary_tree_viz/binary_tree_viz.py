import pygame
from helpers import *

pygame.init()

window_resolution = [1200, 900]
display = pygame.display.set_mode(window_resolution, pygame.RESIZABLE)
pygame.display.set_caption(__file__.split("\\")[-1])

run = True
fps = 480  # 0 for unlimited
prev_time = time.time()
clock = pygame.time.Clock()

tree_depth = 7

root = Node('s')
# tree = construct_binary_tree(root, tree_depth)
tree = construct_random_binary_tree(root, tree_depth, 0.7)
print_binary_tree(tree)
position_list = binary_tree_position_list(tree)

# Text
pygame.font.init()
fps_font = pygame.font.SysFont(None, window_resolution[1] // 32)
coord_font = pygame.font.SysFont('leelawadeeuisemilight', window_resolution[1] >> 6)
stats_font = pygame.font.SysFont('leelawadeeuisemilight', int(window_resolution[1] / (tree_depth + 1)) >> 1)




while run:

    # Calculate delta time
    time_now = time.time()
    dt = time_now - prev_time + (1 / 2 ** 32)
    prev_time = time_now

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Resize window event
        if event.type == pygame.VIDEORESIZE:
            display = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            window_resolution = [event.w, event.h]


        # Keypresses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                tree_depth += 1
            if event.key == pygame.K_DOWN:
                tree_depth -= 1
            # tree = construct_binary_tree(root, tree_depth)
            tree = construct_random_binary_tree(root, tree_depth, 0.7)
            stats_font = pygame.font.SysFont('leelawadeeuisemilight', int(window_resolution[1] / (tree_depth + 1)) >> 1)

    # Draw
    display.fill(color_black)

    # for string in position_list:
    #     pos = string_to_position(string, tree_depth, window_resolution)
    #     # coord_text = coord_font.render(f"({','.join([str(e) for e in pos])})", True, color_white)
    #     # coord_rect = coord_text.get_rect(center=pos)
    #     # display.blit(coord_text, coord_rect)

    #     pygame.draw.circle(display, color_white, pos, 5)

    stats_text = stats_font.render(f"Tree depth: {tree_depth} | Nodes: {2 ** tree_depth - 1}", True, color_white)
    stats_rect = stats_text.get_rect(center=(window_resolution[0] / 2, window_resolution[1] / (tree_depth + 1) / 2))
    display.blit(stats_text, stats_rect)

    draw_binary_tree(tree, tree_depth, window_resolution, display)




    # show_fps(display, fps_font, dt)
    pygame.display.update()
    if fps != 0:
        clock.tick(abs(fps))
