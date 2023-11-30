import random

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
      pass
    elif num >= 7 and num <= 10:
      #armour
      pass
    else:
      #gun
      print('you got gun')
      self.inventory['gun'] = 1
      self.inventory['sword'] = 0
      self.inventory['armour'] = 0
    return self.inventory
