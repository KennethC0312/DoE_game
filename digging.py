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
      #sword
      if self.level == 1:
        pass
      elif self.level == 2:
        pass
      else:
        pass
    elif num >= 7 and num <= 10:
      #armour
      if self.level == 1:
        pass
      elif self.level == 2:
        pass
      else:
        pass
    else:
      #gun
      gun = pick_up('gun', 999, 1, 0)
      self.inventory['gun'] = 1
      self.inventory['sword'] = 0
      self.inventory['armour'] = 0
    return self.inventory
