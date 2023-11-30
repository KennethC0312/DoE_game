import os
import pygame
from const import *

pygame.init()

class pick_up:
  def __init__(self, type, new_stat, old_stat, torch_level):
    self.type = type
    self.new_stat = []
    for i in new_stat:
      self.new_stat.append(i)
    self.old_stat = []
    for i in old_stat:
      self.old_stat.append(i)
    self.pick_up_confirmation = [pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/pick_up_confirmation', 'pick_up_1.png')), (screen_size, screen_size)),                                pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/pick_up_confirmation', 'pick_up_2.png')), (screen_size, screen_size)),
 pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/pick_up_confirmation', 'pick_up_3.png')), (screen_size, screen_size)),
pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/pick_up_confirmation', 'pick_up_4.png')), (screen_size, screen_size)),
pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/pick_up_confirmation', 'pick_up_5.png')), (screen_size, screen_size)),
pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/pick_up_confirmation', 'pick_up_6.png')), (screen_size, screen_size)),
pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/pick_up_confirmation', 'pick_up_7.png')), (screen_size, screen_size)),
pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/pick_up_confirmation', 'pick_up_8.png')), (screen_size, screen_size)),
pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/pick_up_confirmation', 'pick_up_9.png')), (screen_size, screen_size)),
pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/pick_up_confirmation', 'pick_up_10.png')), (screen_size, screen_size)),
pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/pick_up_confirmation', 'pick_up_11.png')), (screen_size, screen_size)),
pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/pick_up_confirmation', 'pick_up_12.png')), (screen_size, screen_size)),
pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/pick_up_confirmation', 'pick_up_13.png')), (screen_size, screen_size)),
 pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/pick_up_confirmation', 'pick_up_14.png')), (screen_size, screen_size)),
pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/pick_up_confirmation', 'pick_up_15.png')), (screen_size, screen_size)),                         pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/pick_up_confirmation', 'pick_up_16.png')), (screen_size, screen_size)),
pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/pick_up_confirmation', 'pick_up_17.png')), (screen_size, screen_size)),
pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/pick_up_confirmation', 'pick_up_18.png')), (screen_size, screen_size)),
pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/pick_up_confirmation', 'pick_up_19.png')), (screen_size, screen_size)),
pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/pick_up_confirmation', 'pick_up_20.png')), (screen_size, screen_size))]
    self.numbers = [pygame.image.load(os.path.join('assets/numbers', '0.png')),
                   pygame.image.load(os.path.join('assets/numbers', '1.png')),
                   pygame.image.load(os.path.join('assets/numbers', '2.png')),
                   pygame.image.load(os.path.join('assets/numbers', '3.png')),
                   pygame.image.load(os.path.join('assets/numbers', '4.png')),
                   pygame.image.load(os.path.join('assets/numbers', '5.png')),
                   pygame.image.load(os.path.join('assets/numbers', '6.png')),
                   pygame.image.load(os.path.join('assets/numbers', '7.png')),
                   pygame.image.load(os.path.join('assets/numbers', '8.png')),
                   pygame.image.load(os.path.join('assets/numbers', '9.png'))]
    self.torch_level = torch_level

  def pick_up_animation(self):
    if self.type == 'armour':
      pass
    elif self.type == 'weapon':
      pass
    elif self.type == 'torch':
      if self.torch_level == 1:
        pass
      else:
        pass
    else:  #gun
      pass