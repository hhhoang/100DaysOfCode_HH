#https://replit.com/@hhhoang/coffee-machine-start#main.py
#CREATE A COFFEE MACHINE WITHIN THE COURSE 100 days of Python from Angela Yu


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

money = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def checkResources(drink):
  """
  When user chooses a drink, it should check if there are enough resources to make that drink.
  """
  #print(resources["water"])
  isSufficient = []
  for k, v in MENU.items():
    if drink == k: 
      for k, v in v['ingredients'].items():
        #print(k, "needs ", v, "and current is ", resources[k])
        if v <= resources[k]:
          isSufficient.append(True)
        else:
          print("Sorry there is not enough ",k)
          isSufficient.append(False)
  return min(isSufficient) 



def processCoins(drink):
  """
  allow user to insert coins and return the total value
  """
  print("Please insert coins.")
  quarters = input("how many quarters?")
  dimes = input("how many dimes?")
  nickles = input("how many nickles?")
  pennies = input("how many pennies?")
  value = int(quarters)*0.25 + int(dimes)*0.10 + int(nickles)*0.05 + int(pennies)*0.01
  #print(value)
  return value
  

def checkTransaction(coins_inserted, drink):
  """
  check if the payment is enough for the chosen drink
  """
  if coins_inserted < MENU[drink]["cost"]:
    print("Sorry that is not enough money. Money refunded.")
    return False
  elif coins_inserted == MENU[drink]["cost"]:
    global money
    money += MENU[drink]["cost"]
    return True
  elif coins_inserted > MENU[drink]["cost"]:
    print("Here is ", round(coins_inserted - MENU[drink]["cost"],2), " dollars in change.")
    money += MENU[drink]["cost"]
    return True

def makeCoffee(drink):
  """
  deduct the resources and give user the drink of his choice
  """
  for k, v in MENU[drink]["ingredients"].items():
    resources[k] -= v
  print("Here is your ", drink, "☕  Enjoy!")

isOn = True

while isOn:
  promt_message = input("What would you like? (espresso $1.5/latte $2.5/cappuccino $3.0)")

  # Secret word "off" to clear off the screen
  if promt_message == "off":
    print("Powering off")
    print("...")
    print("...")
    isOn = False

  # Secret word "report" to print the report for resources
 
  elif promt_message == "report":
    for k, v in resources.items():
      print (k, ": ", v)
    print("profit: ", money)
  
  elif promt_message in MENU:
    drink = promt_message
    if checkResources(drink):
      coins_inserted = processCoins(drink)
      if checkTransaction(coins_inserted, drink):
        makeCoffee(drink)
  else:
    print("please enter correct command")

  # 

  
