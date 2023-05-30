import pygame
import sys
import time

# Global variables
XO = 'x'
winner = None
draw = None
window_width = 400
window_height = 400
white = (255, 255, 255)
line_color = (0, 0, 0)
baord = [[None]*3, [None]*3, [None]*3]

pygame.init()
fps = 30
clock = pygame.time.Clock()
screen = pygame.display.set_mode((window_width, window_height + 100), 0, 32)
pygame.display.set_caption("Tic Tac Toe")
initiating_window = pygame.image.load("images\modified_cover-100x100.png")
x_img = pygame.image.load("images\X_modified-100x100.png")
o_img = pygame.image.load("images\o_modified-100x100.png")
initiating_window = pygame.transform.scale(
    initiating_window, (window_width, window_height + 100))
x_img = pygame.transform.scale(x_img, (80, 80))
o_img = pygame.transform.scale(o_img, (80, 80))


def game_initiating_window():
    screen.blit(initiating_window, (0, 0))
    pygame.display.update()
    time.sleep(3)
    screen.fill(white)

    pygame.draw.line(screen, line_color, (window_width / 3, 0),
                     (window_width/3, window_height), 7)
    pygame.draw.line(screen, line_color, (window_width / 3 * 2, 0),
                     (window_width/3*2, window_height), 7)

    pygame.draw.line(screen, line_color, (0, window_height/3),
                     (window_width, window_height/3), 7)
    pygame.draw.line(screen, line_color, (0, window_height/3*2),
                     (window_width, window_height/3*2), 7)
    draw_status()


def draw_status():

    global draw
    if winner is None:
        message = XO.upper() + "'s Turn"
    else:
        message = winner.upper() + " won !"
    if draw:
        message = 'Game Draw!'

    font = pygame.font.Font(None, 30)

    text = font.render(message, 1, (255, 255, 255))

    screen.fill((0, 0, 0), (0, 400, 500, 100))
    text_rect = text.get_rect(center = (window_width / 2, 500-50))
    screen.blit(text, text_rect)
    pygame.display.update
