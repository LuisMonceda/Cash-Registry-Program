# Menu
print("Welcome to the Rational Bookstore!")
print("""
a) Ballpen | P10
b) Pencil | P5
c) Highlighter | P15
d) Eraser | P10
e) Marker | P20
""")

#Item prices
ballpen_price = 10
pencil_price = 5
highlighter_price = 15
eraser_price = 10
marker_price = 20

running_1 = True

while running_1:
# Bought item
  item_bought = str(input("What would you like to buy? >> "))
# Quantity of the item
  quantity_item = int(input("How many would you like to buy? >> "))
# Your money
  money = float(input("How much money do you have? >> "))

  #If, elif, else statements
  # If user bought ballpen
  if item_bought == "a" or item_bought == "ballpen":
    print("You bought", quantity_item, "ballpen(s) for", ballpen_price * quantity_item, "pesos.")
    print("You have", money - ballpen_price * quantity_item, "pesos left.")
    print("Thank you for your purchase!")
  # If user bought a pencil
  elif item_bought == "b" or item_bought == "pencil":
    print("\n")
    print("You have bought", quantity_item, "pencil(s) for", pencil_price * quantity_item, "pesos.")
    print("You have", money - pencil_price * quantity_item, "pesos left.")
    print("Thank you for your purchase!")

# If user bought a highlighter
  elif item_bought == "c" or item_bought == "highlighter":
    print("\n")
    print("You have bought", quantity_item, "highlighter(s) for", highlighter_price * quantity_item, "pesos.")
    print("You have", money - highlighter_price * quantity_item, "pesos left.")
    print("Thank you for your purchase!")

# If user bought an eraser
  elif item_bought == "d" or item_bought == "eraser":
    print("\n")
    print("You have bought", quantity_item, "eraser(s) for", eraser_price * quantity_item, "pesos.")
    print("You have", money - eraser_price * quantity_item, "pesos left.")
    print("Thank you for your purchase!")

# If user bought a marker
  elif item_bought == "e" or item_bought == "marker":
    print("\n")
    print("You have bought", quantity_item, "marker(s) for", marker_price * quantity_item, "pesos.")
    print("You have", money - marker_price * quantity_item, "pesos left.")
    print("Thank you for your purchase!")

# Ask if the user would like to purchase again
  print("\n")
  purchase_again = input("Would you like to purchase again? (yes/no) >> ")
# If user would like to purchase again
  if "yes" in [purchase_again]:
    running_1 = True

  if "yes" not in [purchase_again]:
   print("Thank you for shopping at the Rational Bookstore!")
   break