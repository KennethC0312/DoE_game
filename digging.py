import random
from pick_up_animations import *

class Diggin:
  def __init__(self, inventory, level, screen_cov, screen):
    self.inventory = inventory
    self.level = level + 1
    self.screen_cov = screen_cov
    self.screen = screen

  def __dig(self, choice):
    from non_const import radius
    if choice >= 0 and choice <= 2:
      if self.inventory['torch'] == 0 or (self.inventory['torch'] == 1 and self.level >= 2):
        self.inventory['torch'] += 1
        torch = pick_up('torch', 0, self.inventory['sword'], self.inventory['torch'], self.screen_cov, self.screen)
        torch.torch_animation()
      else:
        return True
    elif choice >= 3 and choice <= 6:
      attack = random.randint(10, 50)
      #sword
      if self.level == 1:
        attack *= 1
        attack = str(attack)
        sword = pick_up('weapon', attack, self.inventory['sword'], 0, self.screen_cov, self.screen)
        check = sword.pick_up_animation()
        if check:
          self.inventory['sword'] = attack
      elif self.level == 2:
        attack *= 1.2
        attack = str(int(attack))
        sword = sword = pick_up('weapon', attack, self.inventory['sword'], 0, self.screen_cov, self.screen)
        check = sword.pick_up_animation()
        if check:
           self.inventory['sword'] = attack
      else:
        attack *= 1.8
        attack = str(int(attack))
        sword = sword = pick_up('weapon', attack, self.inventory['sword'], 0, self.screen_cov, self.screen)
        check = sword.pick_up_animation()
        if check:
          self.inventory['sword'] = attack
    elif choice >= 7 and choice <= 10:
      defence = random.randint(10, 50)
      #armour
      if self.level == 1:
        defence *= 1
        defence = str(defence)
        armour = pick_up('armour', defence, self.inventory['armour'], 0, self.screen_cov, self.screen)
        check = armour.pick_up_animation()
        if check:
           self.inventory['armour'] = defence
      elif self.level == 2:
        defence *= 1.2
        defence = str(int(defence))
        armour = pick_up('armour', defence, self.inventory['armour'], 0, self.screen_cov, self.screen)
        check = armour.pick_up_animation()
        if check:
           self.inventory['armour'] = defence
      else:
        defence *= 1.8
        defence = str(int(defence))
        armour = pick_up('armour', defence, self.inventory['armour'], 0, self.screen_cov, self.screen)
        check = armour.pick_up_animation()
        if check:
           self.inventory['armour'] = defence
    else:
      #gun
      gun = pick_up('gun', str(999), str(1), 0, self.screen_cov, self.screen)
      gun.pick_up_animation()
      self.inventory['gun'] = 1
      self.inventory['sword'] = 0
      self.inventory['armour'] = 0
    return self.inventory
  def dig(self):
    choice = random.randint(0, 11)
    list = self.__dig(choice)
    while list == True:
      list = self.__dig(choice)
    return list