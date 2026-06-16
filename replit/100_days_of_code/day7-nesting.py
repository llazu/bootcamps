#fix my code
order = input("What would you like to order: pizza or hamburger? ")
if order == "hamburger":
  print("Thank you.")
  cheese = input("Do you want cheese?")
  if cheese == "yes":
    print("You got it.")
  else: 
    print("No cheese it is.")
elif order == "pizza":
  print("Pizza coming up.")
  toppings = input("Do you want pepperoni on that?")
  if toppings == "yes":
    print("We will add pepperoni.")
else:
  print("Your pizza will not have pepperoni.")

#Day 7 challenge

show = input("Are you a Dragon Ball Z fan? ")
if show == "yes":
  main_character = input("Who is the main character? ")
  if main_character == "goku":
    enemy =input("Against what enemy did Goku first turn Super Sayan? ")
    if enemy == "freeza":
      print("You know your stuff, kid!")
    else:
      print("no way, jose!")
  else:
      print("How could you get that one wrong, haha!")
else:
  print("You're a fake fan; go watch some re-runs, lol!")
    