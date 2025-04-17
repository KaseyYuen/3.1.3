'''Iteration 3
Add the following features to your first iteration:

 Ask the user whether they would like french fries (yes, no).
 If they say yes, ask what size french fries they would like: 
    small $1.00
    medium $1.50
    large $2.00
 If they say “small,” ask the user whether they’d like to mega-size their fries (yes, no). 
 If the user inputs yes to mega-size, give them large fries at the large fries price instead of their small fries.
 Have the program output the user’s fries selection to verify that the program is working correctly.
 Adjust the program so the total cost only outputs to the user after their sandwich, drink, and fries selection.'''
sSelect = input("chicken $5.25, beef $6.25, tofu $5.75).")
print(sSelect)
string1 = "Would you like a beverage?"
print (string1)
(yesno)= input(str("Yes or No"))
print (yesno)
if (yesno)==str("Yes" or "yes"):
  (drinksize) = input("small $1.00, medium $1.75, large $2.25")
  print(drinksize) 
  string1 = "Would you like fries?"
  print(string1)
  (yesno2)= input(str("Yes or No"))
  print (yesno2)
  if (yesno2)==str("Yes" or "yes"):
    (fries) = input(str("small $1.00, medium $1.50, large $2.00"))
    print(fries)
    if (fries)==str("small"):
      string1 = "Would you like to mega size your fries?"
      print (string1)
      (yesno3)= input(str("Yes or No"))
      print (yesno3)
      if (yesno)==str("Yes" or "yes"):
        input("large $2.00")
if (yesno)==str("No" or "no"):
  string1 = "Would you like fries?"
  print(string1)
  (yesno2)= input(str("Yes or No"))
  print (yesno2)
  if (yesno2)==str("Yes" or "yes"):
    (fries) = input(str("small $1.00, medium $1.50, large $2.00"))
    print(fries)
    if (fries)==str("small"):
      string1 = "Would you like to mega size your fries?"
      print (string1)
      (yesno3)= input(str("Yes or No"))
      print (yesno3)
      if (yesno)==str("Yes" or "yes"):
        (string1) = "large"
        print (string1)
