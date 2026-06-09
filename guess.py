import random
comp_guess = random.randint(1,10)
count = 0
attempt = 20
print(comp_guess)
# while True:
#     if count<attempt:
#         user_guess = int(input(f'Input number between 1 and 20: '))
#         count += 1
#         print(f'you have {attempt- count} attempt left')

#         if comp_guess == user_guess:

#             print(comp_guess)
#             print("You guessed the correct number.")
#             print(f"you guessed the correct number in {count} attempts.")

#             break
#         else:
#             print(comp_guess)
#             if user_guess > comp_guess:
#                  print(f"Your guess is incorrect.The correct number is lower than {user_guess}, try again ")
#             else:
#                 print(f"Your guess is incorrect.The correct number is higher than {user_guess}, try again ")
#     else:
#         print(f"Max attempt reached, random number is {comp_guess}")
#         break
          
while True:
    if count<attempt:
        user_guess = int(input(f'Input number between 1 and 20: '))
        count += 1
        print(f'you have {attempt- count} attempt left')

        if comp_guess == user_guess:

            print(comp_guess)
            print("You guessed the correct number.")
            print(f"you guessed the correct number in {count} attempts.")

            break
        else:
            print(comp_guess)
            if user_guess > comp_guess:
                 print(f"Your guess is incorrect.The correct number is lower than {user_guess}, try again ")

            else:
                print(f"Your guess is incorrect.The correct number is higher than {user_guess}, try again ")
    else:
        print(f"Max attempt reached, random number is {comp_guess}")
        break
          

   
