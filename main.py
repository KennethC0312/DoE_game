import sys
import pygame
import time
from pygame.locals import QUIT
from digging import *
from maze_level import *
from const import *
from non_const import *
from pick_up_animations import*

#
clock = pygame.time.Clock()
#
screen = pygame.display.set_mode((21 * block_dim, 21*block_dim))
pygame.display.set_caption("A cool Game")
#
cover_surf = pygame.Surface((screen_size, screen_size))
cover_surf.fill((0, 0, 0))
cover_surf.set_colorkey((0, 1, 255))
pygame.draw.circle(cover_surf, (0, 1, 255), (x_mask, y_mask), radius)
clip_rect = pygame.Rect(0, 0, screen_size, screen_size)
#
no_dig = pick_up('no', str(0), str(0), str(0), cover_surf, screen)
#
inventory = {
  'armour': 0,
  'sword' : 10,
  'torch' : 0,
}
#
while True:
  if inventory['torch'] == 1:
    radius = 150
  elif inventory['torch'] == 2:
    radius = 200
  screen.fill(black)
  cover_surf.fill((0, 0, 0))
  pygame.draw.circle(cover_surf, (0, 1, 255), (x_mask, y_mask), radius)
  screen.set_clip(clip_rect)
  for i in range(len(maze[level])):
    for n in range(len(maze[level][i])):
      if maze[level][i][n] == 0:
        pygame.draw.rect(screen, (255, 255, 255), (n * block_dim, i * block_dim, block_dim, block_dim))
      elif maze[level][i][n] == 2:
        pygame.draw.rect(screen, (0, 255, 0), (n * block_dim, i * block_dim, block_dim, block_dim))
      elif maze[level][i][n] == 3:
        pygame.draw.rect(screen, (0, 0, 255), (n * block_dim, i * block_dim, block_dim, block_dim))
  player = pygame.draw.rect(screen, ('#66729E'), (x, y, block_dim, block_dim))
  screen.blit(cover_surf, clip_rect)
  pygame.display.update()
  if maze[level][y//block_dim][x//block_dim] == 2 and level == 2:
    print("win")
    time.sleep(5)
    break
  elif maze[level][y//block_dim][x//block_dim] == 2 and level != 2:
    print('next level')
    level += 1
    x = 32
    y = 32
    x_mask = x+(block_dim/2)
    y_mask = y+(block_dim/2)
    time.sleep(5)
  key = pygame.key.get_pressed()
  if key[pygame.K_LEFT]:
     tempx = (x - block_dim)//block_dim
     tempy = (y)//block_dim
     if maze[level][tempy][tempx] in check:
       x -= block_dim
       x_mask -= block_dim
  if key[pygame.K_RIGHT]:
     tempx = (x + block_dim)//block_dim
     tempy = (y)//block_dim
     if maze[level][tempy][tempx] in check:
       x += block_dim
       x_mask += block_dim
  if key[pygame.K_UP]:
     tempx = (x)//block_dim
     tempy = (y - block_dim)//block_dim
     if maze[level][tempy][tempx] in check:
       y -= block_dim
       y_mask -= block_dim
  if key[pygame.K_DOWN]:
     tempx = (x)//block_dim
     tempy = (y + block_dim)//block_dim
     if maze[level][tempy][tempx] in check:
       y += block_dim
       y_mask += block_dim
  if key[pygame.K_x]:
    if maze[level][y//block_dim][x//block_dim] == 3:
      if 'gun' in inventory:
        no_dig.got_gun()
      else:
        print('dig')
        inventory_change = Diggin(inventory, level, cover_surf, screen)
        inventory = inventory_change.dig()
        print(inventory)
        maze[level][y//block_dim][x//block_dim] = 0
  for events in pygame.event.get():
    if events.type == QUIT:
     pygame.quit()
     sys.exit()
  clock.tick(fps)