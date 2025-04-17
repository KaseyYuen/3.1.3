'''Iteration 4
 Ask the user how many ketchup packets they would like (enter a positive integer; cost is $0.25 per packet).

After ordering the sandwich, drink, fries, and ketchup packets:
 If the user selected a sandwich, french fries, and a beverage, reduce the total cost of the order by $1.00.
 The program informs the user of their menu selections, for only the items they ordered. 
 The program should print the total cost of the order. Remove any other totals before this point.'''
order = ["order"]
numbers = [0]
total = sum(numbers)
print(total)
sSelect = input("chicken $5.25, beef $6.25, tofu $5.75).")
print(sSelect)
if (sSelect)==str("chicken" or "Chicken"):
  total = [total] + [5.25]
  order = ["order"] + ["chicken"]
if (sSelect)==str("beef" or "Beef"):
  total = [total] + [6.25]
  order = ["order"] + ["beef"]
if (sSelect)==str("tofu" or "Tofu"):
  total = [total] + [5.75]
  order = ["order"] + ["tofu"]
string1 = "Would you like a beverage?"
print (string1)
(yesno)= input(str("Yes or No"))
print (yesno)
if (yesno)==str("Yes" or "yes"):
  (drinksize) = input("small $1.00, medium $1.75, large $2.25")
  print(drinksize) 
  if (drinksize)==str("small" or "Small"):
  total = [total] + [1.00]
  order = ["order"] + ["small drink"]
  if (drinksize)==str("medium" or "Medium"):
  total = [total] + [1.75]
  order = ["order"] + ["medium drink"]
  if (drinksize)==str("large" or "Large"):
  total = [total] + [2.25]
  order = ["order"] + ["large drink"]
  string1 = "Would you like fries?"
  print(string1)
  (yesno2)= input(str("Yes or No"))
  print (yesno2)
  if (yesno2)==str("Yes" or "yes"):
    (fries) = input(str("small $1.00, medium $1.50, large $2.00"))
    print(fries)
    if (sSelect)==str("small" or "Small"):
      total = [total] + [1.00]
      order = ["order"] + ["small fries"]
    if (sSelect)==str("medium" or "Medium"):
      total = [total] + [1.50]
      order = ["order"] + ["medium fries"]
    if (sSelect)==str("large" or "Large"):
      total = [total] + [2.00]
      order = ["order"] + ["large fries"]
    if (fries)==str("small"):
      string1 = "Would you like to mega size your fries?"
      print (string1)
      (yesno3)= input(str("Yes or No"))
      print (yesno3)
      if (yesno)==str("Yes" or "yes"):
        total = [total] + [2.00]
        order = ["order"] + ["large fries"]
      if (yesno)==str("No" or "no"):
        total = [total] + [1.00]
        order = ["order"] + ["small fries"]
        (ketchup) = input(str("How many ketchup packets do you want? $.25 each"))
        print (ketchup)
        if (sSelect)==str("chicken" or "beef" or "tofu") and (drinksize)==str("small" or "medium" or "large") and (fries)==str("small" or "medium" or "large"):
          (total) = (total) - (1.00)
