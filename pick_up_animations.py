import os
import pygame
import time
from const import *
from non_const import *
from images import *
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
    #the files
    self.pick_up_confirmation = pick_up_confirmation
    self.wow = wow
    self.got = got
    self.numbers = numbers
    self.stat = stat
    self.gun_bro = gun_bro
    self.no_dig = no_dig
    self.identify = identify
    self.torch = torch
    self.view = view
    self.gun_got = gun_got
    self.gun_shock = gun_shock
    self.no_dig_2 = no_dig_2
    
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
      for i in range(len(self.gun_got)-2):
        self.sc.blit(self.gun_got[i+2], (0,0))
        self.screen.set_clip(self.clip)
        self.screen.blit(self.sc, self.clip)
        pygame.display.flip()
        time.sleep(0.2)
      while not self.clicked:
        n = 1 if n == 0 else 0
        self.sc.blit(self.gun_got[n], (0,0))
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
      for i in range(len(self.gun_shock)-2):
        n = 1 if n == 0 else 0
        self.sc.blit(self.gun_shock[i+2], (0,0))
        self.sc.blit(self.identify[2], (-55, -130 + n*10))
        self.screen.set_clip(self.clip)
        self.screen.blit(self.sc, self.clip)
        pygame.display.flip()
        time.sleep(0.2)
      n = 1
      while not self.clicked:
        n = 1 if n == 0 else 0
        self.sc.blit(self.gun_shock[n], (0,0))
        self.sc.blit(self.identify[2], (-55, -130 + n*10))
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
      for i in range(len(self.no_dig_2)-2):
        n = 1 if n == 0 else 0
        self.sc.blit(self.no_dig_2[i+2], (0,0))
        self.sc.blit(self.identify[2], (-55, -130 + n*10))
        self.screen.set_clip(self.clip)
        self.screen.blit(self.sc, self.clip)
        pygame.display.flip()
        time.sleep(0.2)
      n = 1
      while not self.clicked:
        n = 1 if n == 0 else 0
        self.sc.blit(self.no_dig_2[n], (0,0))
        self.sc.blit(self.identify[2], (-55, -130 + n*10))
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
      for i in range(len(self.torch[1])-2):
        self.sc.blit(self.torch[1][i+2], (0, 522))
        self.screen.set_clip(self.clip)
        self.screen.blit(self.sc, self.clip)
        pygame.display.flip()
        if i == 4:
          time.sleep(0.5)
        else:
          time.sleep(0.2)
      while not self.clicked:
        n = 1 if n == 0 else 0
        self.sc.blit(self.torch[1][n], (0,522))
        self.screen.set_clip(self.clip)
        self.screen.blit(self.sc, self.clip)
        pygame.display.flip()
        for events in pygame.event.get():
          if events.type == pygame.MOUSEBUTTONDOWN:
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0]:
              self.clicked = True
        time.sleep(0.2)
    self.clicked = False
    for i in range(len(self.view)-2):
      self.sc.blit(self.view[i+2], (0, 522))
      self.screen.set_clip(self.clip)
      self.screen.blit(self.sc, self.clip)
      pygame.display.flip()
      time.sleep(0.2)
    while not self.clicked:
      n = 1 if n == 0 else 0
      self.sc.blit(self.view[n], (0,522))
      self.screen.set_clip(self.clip)
      self.screen.blit(self.sc, self.clip)
      pygame.display.flip()
      for events in pygame.event.get():
        if events.type == pygame.MOUSEBUTTONDOWN:
          mouse_presses = pygame.mouse.get_pressed()
          if mouse_presses[0]:
            self.clicked = True
      time.sleep(0.2)