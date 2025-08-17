#Inventory will be a dictionary where the keys are string values describing the item in the inventory and the value is an integer value detailing how many of that item the player has Write a function named displayInventory() that would take any possible “inventory” and display it 

def displayInventory(inv):
    print('Players Inventory:')
    itemTotal = 0

    for item in inv:
        print(f"{inv[item]} {item}")
        itemTotal += inv[item]
    print(f"Total items the player has {itemTotal}")
    print("====================================")
    print("\n")




# Write a function named addToInventory(inventory, addedItems), where the inventory parameter is a dictionary representing the player’s inventory (like in the previous project) and the addedItems parameter is a list like dragonLoot. The addToInventory() function should return a dictionary that represents the updated inventory. Note that the addedItems list can contain multiples of the same item.

def addToInventory(inv, loot):
    for item in loot:
        if item in inv:
            inv[item] += 1
        else:
            inv[item] = 1




# main function 
if __name__ == "__main__":
    #initial inventory
    inventory={'rope': 1, 'torch': 1, 'gold coin': 1, 'dagger': 1, 'arrow': 1}
    displayInventory(inventory)

    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby'] #loot
    #afterloot
    print("After loot:")
    addToInventory(inventory, dragonLoot)
    displayInventory(inventory)
