# Dictionaries
# https://automatetheboringstuff.com/chapter5/


stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        # FILL IN THE CODE HERE
        print(k, ": ", v)
        item_total += v
    print("Total number of items: " + str(item_total))

#displayInventory(stuff)

def addToInventory(inventory, addedItems):
    # your code goes here
    print("before: ", inventory)
    for i in addedItems:
        if i in inventory:
            inventory[i] = inventory[i] + 1
        else:
            inventory.setdefault(i, 1)
    print("after: ", inventory)
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
