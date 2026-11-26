# Online Python compiler (interpreter)
# Write and run Python online using this editor.

import random
def show_rule():
  print("==============================")
  print("Rock,Paper,Scissors Tournament")
  print("==============================\n")

def get_player_choice():
  while True:
    print("\nChoose your move:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Quit Game")
    choice = input("Enter 1, 2, 3, or 4: ")
    if choice == "1":
      return "rock"
    elif choice == "2":
      return "paper"
    elif choice == "3":
      return "scissors"
    elif choice == "4":
      return "quit"
    else:
      print("Invalid input! Please type 1, 2, 3, or 4")
def get_computer_choice():
  options = ["rock", "paper", "scissors"]
  return random.choice(options)

def check_winner(player,computer):
  if player == computer:
    return "tie"
  elif player == "rock" and computer == "scissors":
    return "player"
  elif player == "paper" and computer == "rock":
    return "player"
  elif player == "scissor" and computer == "paper":
    return "player"
  else:
    return "computer"

def show_scoreboard(player_score, computer_score, ties, streak):
  print(f"SCOREBOARD -> You: {player_score} | Computer: {computer_score}")
  if streak >=2:
    print(f" You are on a {streak}-win streak!")
def play_game():
  show_rule()

  player_score = 0
  computer_score = 0
  ties = 0
  win_streak = 0
  round_number = 1

  while player_score<5 and computer_score<5:
    print(f"\n---ROUND {round_number} ---")
    player_move = get_player_choice()

    if player_move == "quit":
      print("\nYou exited the tournament. Thanks for playing!")
      return
    computer_move = get_computer_choice()
    print(f"\nYou chose: {player_move.upper()}")
    print(f"\nComputer chose: {computer_move.upper()}")
    winner = check_winner(player_move,computer_move)
    if winner == "player":
      print("You win this round!")
      player_score +=1
      win_streak +=1
    elif winner == "computer":
      print("Computer win this round!")
      computer_score +=1
      win_streak = 0
    else:
      print("It's a Tie!")
      ties += 1

    show_scoreboard(player_score, computer_score, ties, win_streak)
    round_number += 1
  print("Game Over")
  if player_score == 5:
    print("You win!")
  else:
    print("Computer wins!")
  print(f"Final Score -> You: {player_score} | Computer: {computer_score}")
while True:
  play_game()
  play_again = input("\nDo you want to play again? y/n: ")
  if play_again == "n":
    print("Goodbye")
    break
