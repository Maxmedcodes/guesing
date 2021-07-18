import random
guess =random.randint(1,100)

print("hello this is a guessing game")
print("If a player's guess is less than 1 or greater than 100, it will say 'OUT OF BOUNDS'")
print("if your guess is within 10 in the First guess it will say 'WARM' \n if your guess is further than 10 it will return cold")
print("""on all subsequent goes if your guess is closer than the previous guess it will return closer \n if is further than previous guess
 it will return colder""")



list_1 = [0]
guess =random.randint(1,100)

# My first try by myself 
while True:
  think = int(input("pick a number: "))
  if think < 1 or think >100 :
    print("Your out of bounds please choose a number between 1 and 100")
  else:
    print(guess)
    print(list_1)
  
  if think == guess:
    print("Well done ")
    break
  list_1.append(think)

  print(list_1[-2])

  # if list_1[-2]:  
  #   if abs(guess-think) < abs(guess-list_1[-2]):
  #       print('WARMER!')
  #   else:
  #     print('COLDER!')
   
  # else:
  #   if abs(guess-think) <= 10:
  #     print('WARM!')
  #   else:
  #     print('COLD!')

# Second try cheat + modify
# while True:
#     print(guess)
#     think = int(input("pick a number: "))
#     if think <1 or think >100 :
#         print("Your out of bounds please choose a number between 1 and 100")
#     list_1.append(think)
#     if list_1[-2]: 
#         if abs(guess-think) < abs(guess-list_1[-2]):
#             print('WARMER!')
#         else:
#             print('COLDER!')
   
#     else:
#         if abs(guess-think) <= 10:
#             print('WARM!')
#         else:
#             print('COLD!') 
            
        #     if think == guess:
#         print("well done you only did it in {}".format(len(think)))
#     elif think == "quit":
#         break
#     elif think != int():
#         continue
#     else:
#         list_1 += think
#         print("you're last guess was ",list_1)
#         continue
