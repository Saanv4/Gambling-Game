import random

print("Welcome to this Gambling Game!\n")
num_players = int(input("Enter the number of players\n"))
list_username = []
list_networth = []
list_choices = ["Heads" , "Tails"]
end_game = False
for i in range(0 , num_players):
  username = str(input("Enter username\n"))
  list_username.append(username)
  list_networth.append(500)
computer_guess = random.randint(0 , 1)
winner = 0
while end_game == False:
  for i in range(0 , num_players):
    bet = int(input(f"Enter your bet,{list_username[i]}\n"))
    guess = str(input("Enter guess: Heads or Tails\n"))
    if guess == list_choices[computer_guess]:
      list_networth[i] += bet
    elif guess != list_choices[computer_guess]:
      list_networth[i] -= bet
  end_game1 = str(input("Enter \'end\' to end the game or else \'countinue\' to continue this game\n")) 
  max_wealth = int(max(list_networth)) 
  if end_game1 == "end":
    print(f"The winner is {list_username[list_networth.index(max_wealth)]} with a wealth of {max_wealth}\n")
    end_game = True
  elif end_game1 == "continue":
    end_game == False
