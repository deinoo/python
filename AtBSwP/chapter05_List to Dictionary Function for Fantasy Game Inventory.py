"""Imagine that a vanquished dragon’s loot is represented as a list of strings like this:

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

Write a function named addToInventory(inventory, addedItems), where the inventory parameter is a dictionary
representing the player’s inventory (like in the previous project) and the addedItems parameter is a list like
dragonLoot. The addToInventory() function should return a dictionary that represents the updated inventory. Note that
the addedItems list can contain multiples of the same item.
Put into inventory some stuff from different one backpack
"""

import random

example = ['gold coin', 'dagger', 'gold coin', 'ruby']
secondBackPack = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = random.choices(example, k=20)
#print(dragonLoot)
inventory = {}


def addToInventory(inventory, addedItems, oldInventory):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    for item in inventory:
        inventory[item] += oldInventory.get(item,0)
    return inventory


print (addToInventory(inventory, dragonLoot, secondBackPack))