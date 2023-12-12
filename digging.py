import random
from pick_up_animations import *

class Diggin:
  def __init__(self, inventory, level, screen):
    self.inventory = inventory
    self.level = level + 1
    self.screen = screen

  def dig(self):
    num = random.randint(0, 11)
    if num >= 0 and num <= 2:
      if self.inventory['torch'] == 0:
        self.inventory['torch'] += 1
      if self.inventory['torch'] == 1 and self.level >= 2:
        self.inventory['torch'] +=1
    elif num >= 3 and num <= 6:
      attack = random.randint(1, 1)
      #sword
      if self.level == 1:
        attack *= 1
        attack = str(attack)
        sword = pick_up('weapon', attack, self.inventory['sword'], 0, self.screen)
        check = sword.pick_up_animation()
        if check:
          self.inventory['sword'] = attack
      elif self.level == 2:
        attack *= 2
        attack = str(attack)
        sword = pick_up('weapon', attack, self.inventory['sword'], 0, self.screen)
        check = sword.pick_up_animation()
        if check:
           self.inventory['sword'] = attack
      else:
        attack *= 3
        attack = str(attack)
        sword = pick_up('weapon', attack, self.inventory['sword'], 0, self.screen)
        check = sword.pick_up_animation()
        if check:
          self.inventory['sword'] = attack
    elif num >= 7 and num <= 10:
      defence = random.randint(1, 1)
      #armour
      if self.level == 1:
        defence *= 1
        defence = str(defence)
        armour = pick_up('armour', defence, self.inventory['armour'], 0, self.screen)
        check = armour.pick_up_animation()
        if check:
           self.inventory['armour'] = defence
      elif self.level == 2:
        defence *= 2
        defence = str(defence)
        armour = pick_up('armour', defence, self.inventory['armour'], 0, self.screen)
        check = armour.pick_up_animation()
        if check:
           self.inventory['armour'] = defence
      else:
        defence *= 3
        armour = pick_up('armour', defence, self.inventory['armour'], 0, self.screen)
        check = armour.pick_up_animation()
        if check:
           self.inventory['armour'] = defence
    else:
      #gun
      gun = pick_up('gun', str(999), str(1), 0, self.screen)
      self.inventory['gun'] = 1
      self.inventory['sword'] = 0
      self.inventory['armour'] = 0
    return self.inventory
