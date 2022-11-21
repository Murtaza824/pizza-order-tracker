import time, os

customer = []
pizza = []
list = ["Name", "Quantity", "Size", "Cost"]

def prettyPrint():
  time.sleep(1)
  os.system("clear")
  print("Murtaza Bangin Pizza")
  print("--------------------")
  print()
  for item in list:
    print(f"{item:^10}", end = " ")
  print()
  print("------------------------------------------")
    
  for row in customer:
    for i in row:
      print(f"{i:^10}", end = " ")
    print()

s = 5.99
m = 12.99
l = 15.99

try:
  f = open("pizza.txt", "r")
  customer = eval(f.read())
  f.close
except:
  print()

while True:
  print("Murtaza Bangin Pizza")
  print("--------------------")
  print()
  order = input("1. Place an order\n2. View orders\n\n> ")
  print()
  if order == "1":
    name = input("What's your name?: ")
    size = input("What size do you want? s/m/l: ")
    try:
      quant = int(input("How many pizza's do you want?: "))
    except:
      quant = int(input("You must input a numerical character, try again > "))

    if size == "s":
      cost = quant * s
    elif size == "m":
      cost = quant * m
    elif size == "l":
      cost = quant * l

    pizza = [name, quant, size, cost]
    customer.append(pizza)
  
  elif order == "2":
    prettyPrint()
    time.sleep(3)
  f = open("pizza.txt", "w")
  file = f.write(str(customer))
  f.close()

  time.sleep(1)
  os.system("clear")
