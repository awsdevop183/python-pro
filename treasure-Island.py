print('''               __CS____________        |
 hp___________/ |  |  \       /        |
  \    |   |    |  |  |nm   ,'         /
  |    |   |    |  |  |  `./     _____|
  \    |   |_,--dam---'    \   _/ \  /
   |   |_,-|    |  |       wap=.   \/\
   \  /|   |    |__|        /   \_ /  `\
    `/ |  _|    \   \      /      wp    `\
     \ \_/  \_  kp--mp--rp'      /  \
     |  \_    \/____|__,-\     ,/    `\
      \   \_  /     \    _\   /        `\
       `\   \/___,--|---'  |_/           `
         `\  |      \  ___/
           \_lp-----wc/
''')
print("="*90)
print("************ Welcome to Treasure Island Game ************ ")
print("Your mission is to find the treaure.")

choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")










