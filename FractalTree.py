import pygame, sys, math

pygame.init()
width, height = 800, 600
bg_color = (255, 255, 255)
tree_color = (0, 0, 0)
scale_factor = 0.7

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Fractal Tree")

init_length = 100
current_angle = math.pi / 2
init_depth = 8

def draw_branch(x, y, length, angle, depth):
    if depth == 0:
        return
    else:
        x_end = x + length * math.cos(angle)
        y_end = y - length * math.sin(angle)

        # Draw the branch
        pygame.draw.line(screen, tree_color, (x, y), (x_end, y_end), 2)
        # sub-branches
        draw_branch(x_end, y_end, length * scale_factor, angle - current_angle, depth - 1)
        draw_branch(x_end, y_end, length * scale_factor, angle + current_angle, depth - 1)

def main():
    global current_angle

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEMOTION:
                current_angle = (event.pos[0] - width / 2) * 0.01

        screen.fill(bg_color)
        draw_branch(width // 2, height, init_length, math.pi / 2, init_depth)
        pygame.display.flip()

if __name__ == "__main__":
    main()
