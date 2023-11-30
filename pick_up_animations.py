import os
import pygame
from const import *

pygame.init()

class pick_up:
  def __init__(self, type, new_stat, old_stat):
    self.type = type
    self.new_stat = new_stat
    self.old_stat = old_stat
    self.pick_up_confirmation = [pygame.transform.scale(pygame.image.load(pass), (screen_size, screen_size))]