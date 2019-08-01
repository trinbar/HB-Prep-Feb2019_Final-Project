###########################
## ROCK, PAPER, SCISSORS ##
###########################
#Originally created in February 2019#


#Ask user to make a choice between Rock, Paper, or Scissors
def player_move(play):
  """
  Ask player to choose Rock, Paper, or Scissors
  """
  print("Choose one: Rock, Paper, Scissors")
  play = input("> ")
  play = play.title()

  return(play)

# Computer runs random play against Player
def computer_move(play):
  """
  Assign random play for computer
  """
  #Import random module
  import random

  #Create list of plays: Rock, Paper, or Scissors
  possible_plays = ["Rock","Paper","Scissors"]

  #Assign random choice from list to play variable
  play = random.choice(possible_plays)

  return(play)

#Determine winner of the game
def determine_winner(player, computer):
  """
  Determine winner of the game
  """

  #Define winning rules
  if player == computer:
    print("It's a tie.")
  elif player == "Paper" and computer == "Rock":
    print("{} covers {}.".format(player,computer))
    print("Player wins!")
  elif player == "Scissors" and computer == "Rock":
    print("{} smashes {}.".format(computer,player))
    print("Computer wins!")
  elif player == "Rock" and computer == "Paper":
    print("{} covers {}.".format(computer,player))
    print("Computer wins!")
  elif player == "Scissors" and computer == "Paper":
    print("{} cuts {}.".format(player,computer))
    print("Player wins!")
  elif player == "Rock" and computer == "Scissors":
    print("{} smashes {}.".format(player,computer))
    print("Player wins!")
  elif player == "Paper" and computer == "Scissors":
    print("{} cuts {}.".format(computer,player))
    print("Computer wins!")
  else:
    print("Error.")

  return(play)

# Play game
def play_game(play):
  """
  Main function to play Rock, Paper, Scissors
  """
  #Introduction
  print()
  print("This is a classic game of ROCK, PAPER, SCISSORS")
  print()

  #Outline of rules
  print("Rules")
  print("1. Rock smashes scissors")
  print("2. Paper covers rock")
  print("3. Scissors cut paper")
  print("4. Paper vs. Paper is a tie; Rock vs. Rock is a tie; Scissors vs. Scissors is a tie.")
  print()

  print("Ready? Let's play!")
  print("____________________________________")
  print()


  # Ask user to make a choice between Rock, Paper, or Scissors
  player = player_move(play)
  print("You chose {}.".format(player))
  print()

  # Computer runs random play against Player
  computer = computer_move(play)
  print("Computer chose {}.".format(computer))
  print()

  # Determine winner of the game
  print(determine_winner(player, computer))
  # I think the problem was that the function was
  # called too many times inadvertently so I stored 
  # the results in separate variables and made them
  # parameters for determine_winner()



play = " "
play_game(play)

  
# # For embellishment: (Loop 5 times for 5 reps)?, Assign points for each around, count points to determine winner