import pygame
import random
pygame.init()

def coods1(pNumber):
  if pNumber == 1:
    return [(285, 143)]
  if pNumber == 2:
    return [(266,143), (302,143)]
  if pNumber == 3:
    return [(251,143),(285, 143),(320, 143)]
def coods2(pNumber):
  if pNumber == 1:
    return [(285, 386)]
  if pNumber == 2:
    return [(266,386), (302,386)]
  if pNumber == 3:
    return [(251,386),(285, 386),(320, 386)]
def scale(img, scale):
  return pygame.transform.scale(img, scale)
def enemy(pList):
  x = random.randint(0, 20)
  y = random.randint(0, 20)
  if pList[y][x] == 0:
    pList[y][x] = 4
  else:
    enemy(pList)