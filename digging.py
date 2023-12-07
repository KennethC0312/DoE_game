import random
from pick_up_animations import *

class Diggin:
  def __init__(self, inventory, level):
    self.inventory = inventory
    self.level = level + 1

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
        sword = pick_up('weapon', attack, self.inventory['sword'], 0)
        check = sword.pick_up_animation()
        if check:
          self.inventory['sword'] = attack
      elif self.level == 2:
        attack *= 2
        sword = pick_up('weapon', attack, self.inventory['sword'], 0)
        check = sword.pick_up_animation()
        if check:
           self.inventory['sword'] = attack
      else:
        attack *= 3
        sword = pick_up('weapon', attack, self.inventory['sword'], 0)
        check = sword.pick_up_animation()
        if check:
          self.inventory['sword'] = attack
    elif num >= 7 and num <= 10:
      defence = random.randint(1, 1)
      #armour
      if self.level == 1:
        defence *= 1
        armour = pick_up('armour', defence, self.inventory['armour'], 0)
        check = armour.pick_up_animation()
        if check:
           self.inventory['armour'] = defence
      elif self.level == 2:
        defence *= 2
        armour = pick_up('armour', defence, self.inventory['armour'], 0)
        check = armour.pick_up_animation()
        if check:
           self.inventory['armour'] = defence
      else:
        defence *= 3
        armour = pick_up('armour', defence, self.inventory['armour'], 0)
        check = armour.pick_up_animation()
        if check:
           self.inventory['armour'] = defence
    else:
      #gun
      gun = pick_up('gun', 999, 1, 0)
      self.inventory['gun'] = 1
      self.inventory['sword'] = 0
      self.inventory['armour'] = 0
    return self.inventory
