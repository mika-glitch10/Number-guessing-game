#'''This is a number guessing game, A menu will be displayed and you have to choose any 1 option among them, 
#if you guess correctly your score increases by 1 and number of attempts is displayed'''

import random
score=0

def display_menu():
  print("---Main menu---")
  print("1. Play Game")
  print("2. View Score")
  print("3. Exit")

def play_game():
 global score
 computer_num=random.randint(1,100)
 attempts =0

 while True:
  try:
    user_input=int(input("Guess a number between 1 and 100: "))
    attempts+=1
    if user_input<computer_num:
     print("Too Low")
    elif user_input>computer_num:
     print("Too High")
    else:
     print(f"Congratulations! You guessed the number in {attempts} attempts.")
     score+=1
     break
  except ValueError:
   print("Please enter valid number")


while True:
    display_menu()
    try:
     choice= int(input("Enter your choice(1-3): "))
     if choice==1:
       play_game()
     elif choice==2:
       print("Your current score is", score)
     elif choice==3:
       print("Thanks for playing!")
       break
    except ValueError:
      print("Invalid choice")
    







     
   
    
