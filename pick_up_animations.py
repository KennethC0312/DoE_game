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
    self.new_stat = [x for x in str(new_stat)]
    self.old_stat = [x for x in str(old_stat)]
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
    self.wow = [pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/wow', 'loop_1.png')), (screen_size, screen_size)),
       pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/wow', 'loop_2.png')), (screen_size, screen_size)),
       pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/wow', 'Wow_1.png')), (screen_size, screen_size)),
       pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/wow', 'Wow_2.png')), (screen_size, screen_size)),
       pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/wow', 'Wow_3.png')), (screen_size, screen_size)),
       pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/wow', 'Wow_4.png')), (screen_size, screen_size)),
       pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/wow', 'Wow_5.png')), (screen_size, screen_size)),
       pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/wow', 'Wow_6.png')), (screen_size, screen_size)),
       pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/wow', 'Wow_7.png')), (screen_size, screen_size))]
    self.got = [pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/you_got', 'loop_1.png')), (screen_size, screen_size)),
               pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/you_got', 'loop_2.png')), (screen_size, screen_size)),
               pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/you_got', 'You_got_1.png')), (screen_size, screen_size)),
               pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/you_got', 'You_got_2.png')), (screen_size, screen_size)),
               pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/you_got', 'You_got_3.png')), (screen_size, screen_size)),
               pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/you_got', 'You_got_4.png')), (screen_size, screen_size)),
               pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/you_got', 'You_got_5.png')), (screen_size, screen_size)),
               pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/you_got', 'You_got_6.png')), (screen_size, screen_size)),
               pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/you_got', 'You_got_7.png')), (screen_size, screen_size)),
               pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/you_got', 'You_got_8.png')), (screen_size, screen_size)),
               pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/you_got', 'You_got_9.png')), (screen_size, screen_size)),
               pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/you_got', 'You_got_10.png')), (screen_size, screen_size)),
               pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/you_got', 'You_got_11.png')), (screen_size, screen_size)),
               pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/you_got', 'You_got_12.png')), (screen_size, screen_size)),
               pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/you_got', 'You_got_13.png')), (screen_size, screen_size)),
               pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/you_got', 'You_got_14.png')), (screen_size, screen_size)),
               pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/you_got', 'You_got_15.png')), (screen_size, screen_size)),
               pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/you_got', 'You_got_16.png')), (screen_size, screen_size)),
               pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/you_got', 'You_got_17.png')), (screen_size, screen_size)),
               pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/you_got', 'You_got_18.png')), (screen_size, screen_size)),
               pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/you_got', 'You_got_19.png')), (screen_size, screen_size)),
               pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/you_got', 'You_got_20.png')), (screen_size, screen_size)),
               pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/you_got', 'You_got_21.png')), (screen_size, screen_size)),
               pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/you_got', 'You_got_22.png')), (screen_size, screen_size)),
               pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/you_got', 'You_got_23.png')), (screen_size, screen_size)),
               pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/you_got', 'You_got_24.png')), (screen_size, screen_size)),
               pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/you_got', 'You_got_25.png')), (screen_size, screen_size)),
               pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/you_got', 'You_got_26.png')), (screen_size, screen_size)),
               pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/you_got', 'You_got_27.png')), (screen_size, screen_size)),
               pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/you_got', 'You_got_28.png')), (screen_size, screen_size)),
               pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/you_got', 'You_got_29.png')), (screen_size, screen_size)),
               pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/you_got', 'You_got_30.png')), (screen_size, screen_size)),
               pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/you_got', 'You_got_31.png')), (screen_size, screen_size)),
               pygame.transform.scale(pygame.image.load(os.path.join('assets/pick_up_animation/you_got', 'You_got_32.png')), (screen_size, screen_size))]
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
    self.stat = [pygame.transform.scale(pygame.image.load(os.path.join('assets/stat', 'Armour_New.png')),((screen_size/2),213)),
                 pygame.transform.scale(pygame.image.load(os.path.join('assets/stat', 'Armour_old.png')),((screen_size/2),213)),
                 scale(pygame.image.load(os.path.join('assets/stat', 'weapon_new.png')),((screen_size/2),213)),
                scale(pygame.image.load(os.path.join('assets/stat', 'weapon_old.png')),((screen_size/2),213))]
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
    self.identify = [pygame.transform.scale(pygame.image.load(os.path.join('assets/others', 'armour.png')), (250, 250)),
                     pygame.transform.scale(pygame.image.load(os.path.join('assets/others', 'sword.png' )), (250, 250))]
    self.torch = [[pygame.transform.scale(pygame.image.load(os.path.join('assets/torch/pick_up_1', 'loop_1.png')), (screen_size, 150)),
                  pygame.transform.scale(pygame.image.load(os.path.join('assets/torch/pick_up_1', 'loop_2.png')), (screen_size, 150)),
                  pygame.transform.scale(pygame.image.load(os.path.join('assets/torch/pick_up_1', 'wow_1.png')), (screen_size, 150)),
                  pygame.transform.scale(pygame.image.load(os.path.join('assets/torch/pick_up_1', 'wow_2.png')), (screen_size, 150)),
                  pygame.transform.scale(pygame.image.load(os.path.join('assets/torch/pick_up_1', 'wow_3.png')), (screen_size, 150)),
                  pygame.transform.scale(pygame.image.load(os.path.join('assets/torch/pick_up_1', 'wow_4.png')), (screen_size, 150)),
                  pygame.transform.scale(pygame.image.load(os.path.join('assets/torch/pick_up_1', 'wow_5.png')), (screen_size, 150)),
                  pygame.transform.scale(pygame.image.load(os.path.join('assets/torch/pick_up_1', 'wow_6.png')), (screen_size, 150)),
                  pygame.transform.scale(pygame.image.load(os.path.join('assets/torch/pick_up_1', 'wow_7.png')), (screen_size, 150)),
                  pygame.transform.scale(pygame.image.load(os.path.join('assets/torch/pick_up_1', 'wow_8.png')), (screen_size, 150)),
                  pygame.transform.scale(pygame.image.load(os.path.join('assets/torch/pick_up_1', 'wow_9.png')), (screen_size, 150)),
                  pygame.transform.scale(pygame.image.load(os.path.join('assets/torch/pick_up_1', 'wow_10.png')), (screen_size, 150)),
                  pygame.transform.scale(pygame.image.load(os.path.join('assets/torch/pick_up_1', 'wow_11.png')), (screen_size, 150)),
                  pygame.transform.scale(pygame.image.load(os.path.join('assets/torch/pick_up_1', 'wow_12.png')), (screen_size, 150)),
                  pygame.transform.scale(pygame.image.load(os.path.join('assets/torch/pick_up_1', 'wow_13.png')), (screen_size, 150)),
                  pygame.transform.scale(pygame.image.load(os.path.join('assets/torch/pick_up_1', 'wow_14.png')), (screen_size, 150)),
                  pygame.transform.scale(pygame.image.load(os.path.join('assets/torch/pick_up_1', 'wow_15.png')), (screen_size, 150)),
                  pygame.transform.scale(pygame.image.load(os.path.join('assets/torch/pick_up_1', 'wow_16.png')), (screen_size, 150)),
                  pygame.transform.scale(pygame.image.load(os.path.join('assets/torch/pick_up_1', 'wow_17.png')), (screen_size, 150)),
                  pygame.transform.scale(pygame.image.load(os.path.join('assets/torch/pick_up_1', 'wow_18.png')), (screen_size, 150)),
                  pygame.transform.scale(pygame.image.load(os.path.join('assets/torch/pick_up_1', 'wow_19.png')), (screen_size, 150))],
                  []]
    self.jump = [180, 190, 200, 210, 220, 230, 230, 230, 220, 210, 200, 190, 180, 180]
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
    y = 0
    n = 1
    identify_x = 200
    identify_y = 150
    for i in range(len(self.wow)-2):
      self.sc.blit(self.wow[i+2], (0,0))
      self.screen.set_clip(self.clip)
      self.screen.blit(self.sc, self.clip)
      pygame.display.flip()
      time.sleep(0.2)
    while not self.clicked:
      n = 1 if n == 0 else 0
      self.sc.blit(self.wow[n], (0,0))
      self.screen.set_clip(self.clip)
      self.screen.blit(self.sc, self.clip)
      for events in pygame.event.get():
        pygame.display.flip()
        if events.type == pygame.MOUSEBUTTONDOWN:
          mouse_presses = pygame.mouse.get_pressed()
          if mouse_presses[0]:
            self.clicked = True
      pygame.display.flip()
      time.sleep(0.2)
    n = 1
    self.clicked = False
    if self.type == 'armour':
      for i in range(len(self.got)-2):
        self.sc.blit(self.got[i+2], (0,0))
        self.sc.blit(self.identify[0], (200, 150))
        self.screen.set_clip(self.clip)
        self.screen.blit(self.sc, self.clip)
        pygame.display.flip()
        time.sleep(0.2)
      while not self.clicked:
        n = 1 if n == 0 else 0
        self.sc.blit(self.got[n], (0,0))
        self.sc.blit(self.identify[0], (identify_x, identify_y))
        self.screen.set_clip(self.clip)
        self.screen.blit(self.sc, self.clip)
        for events in pygame.event.get():
          pygame.display.flip()
          if events.type == pygame.MOUSEBUTTONDOWN:
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0]:
              self.clicked = True
        pygame.display.flip()
        time.sleep(0.2)
      self.clicked = False
      for i in range(3):
        identify_x += 63
        identify_y += 10
        self.sc.blit(self.got[n], (0,0))
        self.sc.blit(self.identify[0], (identify_x, identify_y))
        self.screen.set_clip(self.clip)
        self.screen.blit(self.sc, self.clip)
        pygame.display.flip()
        time.sleep(0.2)
      for i in range(len(self.pick_up_confirmation)):
        y = (y+1) if y != len(self.jump) else 0
        self.sc.blit(self.pick_up_confirmation[i], (0,0))
        self.sc.blit(self.stat[1], (30, 30))
        self.sc.blit(self.stat[0], (30, 273))
        for i in range(len(self.old_stat)):
          self.sc.blit(self.numbers[int(self.old_stat[i])], self.coods1[i])
        for i in range(len(self.new_stat)):
          self.sc.blit(self.numbers[int(self.new_stat[i])], self.coods2[i])
        self.sc.blit(self.identify[0], (390, self.jump[y-1]))
        self.screen.set_clip(self.clip)
        self.screen.blit(self.sc, self.clip)
        pygame.display.flip()
        time.sleep(0.2)
      while not self.clicked:
        y = (y+1) if y != len(self.jump) else 0
        self.sc.blit(self.pick_up_confirmation[19], (0,0))
        self.sc.blit(self.stat[1], (30, 30))
        self.sc.blit(self.stat[0], (30, 273))
        for i in range(len(self.old_stat)):
          self.sc.blit(self.numbers[int(self.old_stat[i])], self.coods1[i])
        for i in range(len(self.new_stat)):
          self.sc.blit(self.numbers[int(self.new_stat[i])], self.coods2[i])
        self.sc.blit(self.identify[0], (390, self.jump[y-1]))
        self.screen.set_clip(self.clip)
        self.screen.blit(self.sc, self.clip)
        pygame.display.flip()
        for events in pygame.event.get():
          if events.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            print(mx, my)
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0] and ((mx >= 390 and mx<=664)and (my >= 533 and my<=593)):
              return True
            elif mouse_presses[0] and ((mx >= 390 and mx<=664)and (my >= 600 and my<=665)):
              return False
        self.screen.blit(self.sc, self.clip)
        pygame.display.flip()
    elif self.type == 'weapon':
      for i in range(len(self.got)-1):
        self.sc.blit(self.got[i+2], (0,0))
        self.sc.blit(self.identify[0], (200, 150))
        self.screen.set_clip(self.clip)
        self.screen.blit(self.sc, self.clip)
        pygame.display.flip()
        time.sleep(0.2)
      for i in range(len(self.pick_up_confirmation)):
        y = (y+1) if y != len(self.jump) else 0
        self.sc.blit(self.pick_up_confirmation[i], (0,0))
        self.sc.blit(self.stat[3], (30, 30))
        self.sc.blit(self.stat[2], (30, 273))
        for i in range(len(self.old_stat)):
          self.sc.blit(self.numbers[int(self.old_stat[i])], self.coods1[i])
        for i in range(len(self.new_stat)):
          self.sc.blit(self.numbers[int(self.new_stat[i])], self.coods2[i])
        self.sc.blit(self.identify[1], (390, self.jump[y-1]))
        self.screen.set_clip(self.clip)
        self.screen.blit(self.sc, self.clip)
        pygame.display.flip()
        time.sleep(0.2)
      for i in range(3):
        identify_x += 63
        identify_y += 10
        self.sc.blit(self.got[n], (0,0))
        self.sc.blit(self.identify[0], (identify_x, identify_y))
        self.screen.set_clip(self.clip)
        self.screen.blit(self.sc, self.clip)
        pygame.display.flip()
        time.sleep(0.2)
      while not self.clicked:
        y = (y+1) if y != len(self.jump) else 0
        self.sc.blit(self.pick_up_confirmation[19], (0,0))
        self.sc.blit(self.stat[3], (30, 30))
        self.sc.blit(self.stat[2], (30, 273))
        for i in range(len(self.old_stat)):
          self.sc.blit(self.numbers[int(self.old_stat[i])], self.coods1[i])
        for i in range(len(self.new_stat)):
          self.sc.blit(self.numbers[int(self.new_stat[i])], self.coods2[i])
        self.sc.blit(self.identify[1], (390, self.jump[y-1]))
        self.screen.set_clip(self.clip)
        self.screen.blit(self.sc, self.clip)
        pygame.display.flip()
        time.sleep(0.2)
        for events in pygame.event.get():
          if events.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            print(mx, my)
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0] and ((mx >= 390 and mx<=664)and (my >= 533 and my<=593)):
              return True
            elif mouse_presses[0] and ((mx >= 390 and mx<=664)and (my >= 600 and my<=665)):
              return False
        self.screen.blit(self.sc, self.clip)
        pygame.display.flip()
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
  def torch_animation(self):
    self.clock.tick(200)
    n = 1
    if self.torch_level == 1:
      for i in range(len(self.torch[0])-2):
        self.sc.blit(self.torch[0][i+2], (0, 522))
        self.screen.set_clip(self.clip)
        self.screen.blit(self.sc, self.clip)
        pygame.display.flip()
        if i == 4:
          time.sleep(0.5)
        else:
          time.sleep(0.2)
      while not self.clicked:
        n = 1 if n == 0 else 0
        self.sc.blit(self.torch[0][n], (0,522))
        self.screen.set_clip(self.clip)
        self.screen.blit(self.sc, self.clip)
        pygame.display.flip()
        for events in pygame.event.get():
          if events.type == pygame.MOUSEBUTTONDOWN:
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0]:
              self.clicked = True
        time.sleep(0.2)
    else:
      pass