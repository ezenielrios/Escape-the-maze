print('''
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa   a
8   8               8               8           8                   8   8
8   8   aaaaaaaaa   8   aaaaa   aaaa8aaaa   aaaa8   aaaaa   aaaaa   8   8
8               8       8   8           8           8   8   8       8   8
8aaaaaaaa   a   8aaaaaaa8   8aaaaaaaa   8aaaa   a   8   8   8aaaaaaa8   8
8       8   8               8           8   8   8   8   8           8   8
8   a   8aaa8aaaaaaaa   a   8   aaaaaaaa8   8aaa8   8   8aaaaaaaa   8   8
8   8               8   8   8       8           8           8       8   8
8   8aaaaaaaaaaaa   8aaa8   8aaaa   8   aaaaa   8aaaaaaaa   8   aaaa8   8
8           8       8   8       8   8       8           8   8           8
8   aaaaa   8aaaa   8   8aaaa   8   8aaaaaaa8   a   a   8   8aaaaaaaaaaa8
8       8       8   8   8       8       8       8   8   8       8       8
8aaaaaaa8aaaa   8   8   8   aaaa8aaaa   8   aaaa8   8   8aaaa   8aaaa   8
8           8   8           8       8   8       8   8       8           8
8   aaaaa   8   8aaaaaaaa   8aaaa   8   8aaaa   8aaa8   aaaa8aaaaaaaa   8
8   8       8           8           8       8   8   8               8   8
8   8   aaaa8aaaa   a   8aaaa   aaaa8aaaa   8   8   8aaaaaaaaaaaa   8   8
8   8           8   8   8   8   8           8               8   8       8
8   8aaaaaaaa   8   8   8   8aaa8   8aaaaaaa8   aaaaaaaaa   8   8aaaaaaa8
8   8       8   8   8           8           8   8       8               8
8   8   aaaa8   8aaa8   aaaaa   8aaaaaaaa   8aaa8   a   8aaaaaaaa   a   8
8   8                   8           8               8               8   8
8   8aaaaaaaaaaaaaaaaaaa8aaaaaaaaaaa8aaaaaaaaaaaaaaa8aaaaaaaaaaaaaaa8aaa8
''')
print("Welcome to the Maze.")
print("Your mission is to escape the Maze.")
choice1 = input('You\'re at a cross tunnel. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a sunken floor. you have to get across. Type "wait" to wait for help. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input("Help arrives and gets you across unharmed. your now at a deadend with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("Boom!. an explosion. Game Over.")
    elif choice3 == "yellow":
      print("You found the exit! You Win!")
    elif choice3 == "blue":
      print("You enter a corridor of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry snake. Game Over.")
else:
  print("You fell into a hole. Game Over.")