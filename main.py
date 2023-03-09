import pygame
import random
from pygame. constants import QUIT

pygame.init()

screen = width, height, = 800, 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

main_surface = pygame.display.set_mode(screen)

radius = 20

ball = pygame.Surface((25, 25))
ball_color = ball.fill(WHITE)
ball_rect = ball.get_rect()
ball_speed = [1, 1]

is_wotking = True

def create_random_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)

  random_color = (r, g, b)

  return random_color

while is_wotking: 
  for event in pygame.event.get():
    if event.type == QUIT:
      is_wotking = False

  main_surface.fill(BLACK)

  ball_rect = ball_rect.move(ball_speed)

  if ball_rect.bottom >= height or ball_rect.top <= 0:
    ball_speed[1] = -ball_speed[1]
    ball_color = ball.fill(create_random_color())

  if ball_rect.right >= width or ball_rect.left <= 0:
    ball_speed[0] = -ball_speed[0]
    ball_color = ball.fill(create_random_color())

    
  main_surface.blit(ball, (ball_rect))
  pygame.display.flip()
