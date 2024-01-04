import os
import pygame
import time
from const import *
from non_const import *
from functions import *

pygame.init()

class pick_up:
  def __init__(self, type, new_stat, old_stat, torch_level, screen_cov, screen):
    self.clicked = False
    self.type = type
    self.new_stat = []
    for i in str(new_stat):
      self.new_stat.append(i)
    self.old_stat = []
    for i in str(old_stat):
      self.old_stat.append(i)
    self.coods1 = coods1(len(str(old_stat)))
    self.coods2 = coods2(len(str(new_stat)))
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
    self.numbers = [scale(pygame.image.load(os.path.join('assets/number', '0.png')),(34,48)),
                   scale(pygame.image.load(os.path.join('assets/number', '1.png')),(34,48)),
                   scale(pygame.image.load(os.path.join('assets/number', '2.png')),(34,48)),
                   scale(pygame.image.load(os.path.join('assets/number', '3.png')),(34,48)),
                   scale(pygame.image.load(os.path.join('assets/number', '4.png')),(34,48)),
                   scale(pygame.image.load(os.path.join('assets/number', '5.png')),(34,48)),
                   scale(pygame.image.load(os.path.join('assets/number', '6.png')),(34,48)),
                   scale(pygame.image.load(os.path.join('assets/number', '7.png')),(34,48)),
                   scale(pygame.image.load(os.path.join('assets/number', '8.png')),(34,48)),
                   scale(pygame.image.load(os.path.join('assets/number', '9.png')),(34,48)),
                   scale(pygame.image.load(os.path.join('assets/number', 'period.png')),(34,48))]
    self.stat = [pygame.transform.scale(pygame.image.load(os.path.join('assets/stat', 'Armour_stat.png')),((screen_size/2),213)),
                 scale(pygame.image.load(os.path.join('assets/stat', 'weapon_stat.png')),((screen_size/2),213))]
    self.gun_bro = [pygame.transform.scale(pygame.image.load(os.path.join('assets/got_gun/Bro', 'loop_1.png')), (screen_size, 150)),
                    pygame.transform.scale(pygame.image.load(os.path.join('assets/got_gun/Bro', 'loop_2.png')), (screen_size, 150)),
                    pygame.transform.scale(pygame.image.load(os.path.join('assets/got_gun/Bro', 'bro_1.png')), (screen_size, 150)),
                    pygame.transform.scale(pygame.image.load(os.path.join('assets/got_gun/Bro', 'bro_2.png')), (screen_size, 150)),
                    pygame.transform.scale(pygame.image.load(os.path.join('assets/got_gun/Bro', 'bro_3.png')), (screen_size, 150)),
                    pygame.transform.scale(pygame.image.load(os.path.join('assets/got_gun/Bro', 'bro_4.png')), (screen_size, 150)),
                    pygame.transform.scale(pygame.image.load(os.path.join('assets/got_gun/Bro', 'bro_5.png')), (screen_size, 150)),
                    pygame.transform.scale(pygame.image.load(os.path.join('assets/got_gun/Bro', 'bro_6.png')), (screen_size, 150)),
                    pygame.transform.scale(pygame.image.load(os.path.join('assets/got_gun/Bro', 'bro_7.png')), (screen_size, 150)),
                    pygame.transform.scale(pygame.image.load(os.path.join('assets/got_gun/Bro', 'bro_8.png')), (screen_size, 150)),
                    pygame.transform.scale(pygame.image.load(os.path.join('assets/got_gun/Bro', 'bro_9.png')), (screen_size, 150)),
                    pygame.transform.scale(pygame.image.load(os.path.join('assets/got_gun/Bro', 'bro_10.png')), (screen_size, 150)),
                    pygame.transform.scale(pygame.image.load(os.path.join('assets/got_gun/Bro', 'bro_11.png')), (screen_size, 150)),
                    pygame.transform.scale(pygame.image.load(os.path.join('assets/got_gun/Bro', 'bro_12.png')), (screen_size, 150)),
                    pygame.transform.scale(pygame.image.load(os.path.join('assets/got_gun/Bro', 'bro_13.png')), (screen_size, 150)),
                    pygame.transform.scale(pygame.image.load(os.path.join('assets/got_gun/Bro', 'bro_14.png')), (screen_size, 150)),
                    pygame.transform.scale(pygame.image.load(os.path.join('assets/got_gun/Bro', 'bro_15.png')), (screen_size, 150)),
                    pygame.transform.scale(pygame.image.load(os.path.join('assets/got_gun/Bro', 'bro_16.png')), (screen_size, 150))]
    self.no_dig = [pygame.transform.scale(pygame.image.load(os.path.join('assets/got_gun/no more dig for you', 'loop_1.png')), (screen_size, 150)),
                   pygame.transform.scale(pygame.image.load(os.path.join('assets/got_gun/no more dig for you', 'loop_2.png')), (screen_size, 150)),
                   pygame.transform.scale(pygame.image.load(os.path.join('assets/got_gun/no more dig for you', 'no_more_dig_1.png')), (screen_size, 150)),
                   pygame.transform.scale(pygame.image.load(os.path.join('assets/got_gun/no more dig for you', 'no_more_dig_2.png')), (screen_size, 150)),
                   pygame.transform.scale(pygame.image.load(os.path.join('assets/got_gun/no more dig for you', 'no_more_dig_3.png')), (screen_size, 150)),
                   pygame.transform.scale(pygame.image.load(os.path.join('assets/got_gun/no more dig for you', 'no_more_dig_4.png')), (screen_size, 150)),
                   pygame.transform.scale(pygame.image.load(os.path.join('assets/got_gun/no more dig for you', 'no_more_dig_5.png')), (screen_size, 150)),
                   pygame.transform.scale(pygame.image.load(os.path.join('assets/got_gun/no more dig for you', 'no_more_dig_6.png')), (screen_size, 150)),
                   pygame.transform.scale(pygame.image.load(os.path.join('assets/got_gun/no more dig for you', 'no_more_dig_7.png')), (screen_size, 150)),
                   pygame.transform.scale(pygame.image.load(os.path.join('assets/got_gun/no more dig for you', 'no_more_dig_8.png')), (screen_size, 150)),
                   pygame.transform.scale(pygame.image.load(os.path.join('assets/got_gun/no more dig for you', 'no_more_dig_9.png')), (screen_size, 150)),
                   pygame.transform.scale(pygame.image.load(os.path.join('assets/got_gun/no more dig for you', 'no_more_dig_10.png')), (screen_size, 150)),
                   pygame.transform.scale(pygame.image.load(os.path.join('assets/got_gun/no more dig for you', 'no_more_dig_11.png')), (screen_size, 150)),
                   pygame.transform.scale(pygame.image.load(os.path.join('assets/got_gun/no more dig for you', 'no_more_dig_12.png')), (screen_size, 150)),
                   pygame.transform.scale(pygame.image.load(os.path.join('assets/got_gun/no more dig for you', 'no_more_dig_13.png')), (screen_size, 150)),
                   pygame.transform.scale(pygame.image.load(os.path.join('assets/got_gun/no more dig for you', 'no_more_dig_14.png')), (screen_size, 150)),
                   pygame.transform.scale(pygame.image.load(os.path.join('assets/got_gun/no more dig for you', 'no_more_dig_15.png')), (screen_size, 150)),
                   pygame.transform.scale(pygame.image.load(os.path.join('assets/got_gun/no more dig for you', 'no_more_dig_16.png')), (screen_size, 150)),
                   pygame.transform.scale(pygame.image.load(os.path.join('assets/got_gun/no more dig for you', 'no_more_dig_17.png')), (screen_size, 150)),
                   pygame.transform.scale(pygame.image.load(os.path.join('assets/got_gun/no more dig for you', 'no_more_dig_18.png')), (screen_size, 150)),
                   pygame.transform.scale(pygame.image.load(os.path.join('assets/got_gun/no more dig for you', 'no_more_dig_19.png')), (screen_size, 150)),]
    self.torch_level = torch_level
    self.clock = pygame.time.Clock()
    self.sc = screen_cov
    self.sc.fill((0, 0, 0))
    self.sc.set_colorkey((0,1,255))
    pygame.draw.circle(self.sc,(0, 1, 255), (x_mask, y_mask), radius)
    self.clip = pygame.Rect(0, 0, screen_size, screen_size)
    self.screen = screen


  def pick_up_animation(self):
    self.clock.tick(200)
    if self.type == 'armour':
      for i in range(len(self.pick_up_confirmation)):
        self.sc.blit(self.pick_up_confirmation[i], (0,0))
        self.sc.blit(self.stat[0], (30, 30))
        self.sc.blit(self.stat[0], (30, 273))
        for i in range(len(self.old_stat)):
          self.sc.blit(self.numbers[int(self.old_stat[i])], self.coods1[i])
        for i in range(len(self.new_stat)):
          self.sc.blit(self.numbers[int(self.new_stat[i])], self.coods2[i])
        self.screen.set_clip(self.clip)
        self.screen.blit(self.sc, self.clip)
        pygame.display.flip()
        time.sleep(0.2)
      time.sleep(1000)
      '''
      while not self.clicked:
        for events in pygame.event.get():
          if events.type == pygame.MOUSEBUTTONDOWN:
            if events.button == 0 and 
            '''
    elif self.type == 'weapon':
      for i in range(len(self.pick_up_confirmation)):
        self.sc.blit(self.pick_up_confirmation[i], (0,0))
        self.sc.blit(self.stat[1], (30, 30))
        self.sc.blit(self.stat[1], (30, 273))
        for i in range(len(self.old_stat)):
          self.sc.blit(self.numbers[int(self.old_stat[i])], self.coods1[i])
        for i in range(len(self.new_stat)):
          self.sc.blit(self.numbers[int(self.new_stat[i])], self.coods2[i])
        self.screen.set_clip(self.clip)
        self.screen.blit(self.sc, self.clip)
        pygame.display.flip()
        time.sleep(0.2)
      time.sleep(1000)
    elif self.type == 'torch':
      if self.torch_level == 1:
        pass
      else:
        pass
    else:  #gun
      pass

  def got_gun(self):
    self.clock.tick(200)
    for i in range(len(self.gun_bro)-2):
      self.sc.blit(self.gun_bro[i+2], (0, 522))
      self.screen.set_clip(self.clip)
      self.screen.blit(self.sc, self.clip)
      pygame.display.flip()
      if i == 4:
        time.sleep(0.5)
      time.sleep(0.2)
    while not self.clicked:
      for events in pygame.event.get():
        if events.type == pygame.MOUSEBUTTONDOWN:
          mouse_presses = pygame.mouse.get_pressed()
          if mouse_presses[0]:
            self.clicked = True
      for i in range(2):
        self.sc.blit(self.gun_bro[i], (0, 522))
        self.screen.set_clip(self.clip)
        self.screen.blit(self.sc, self.clip)
        pygame.display.flip()
        time.sleep(0.2)
    self.clicked = False
    for i in range(len(self.no_dig)-2):
      self.sc.blit(self.no_dig[i+2], (0, 522))
      self.screen.set_clip(self.clip)
      self.screen.blit(self.sc, self.clip)
      pygame.display.flip()
      time.sleep(0.2)
    while not self.clicked:
      for events in pygame.event.get():
        if events.type == pygame.MOUSEBUTTONDOWN:
          mouse_presses = pygame.mouse.get_pressed()
          if mouse_presses[0]:
            self.clicked = True
      for i in range(2):
        self.sc.blit(self.no_dig[i], (0, 522))
        self.screen.set_clip(self.clip)
        self.screen.blit(self.sc, self.clip)
        pygame.display.update()
        time.sleep(0.2)