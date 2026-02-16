
# Basic Rock Paper Scissors Game
# Name: Kallan Fuchs
# Date: 2/13/2026

import random
import pygame

"""
main.py
---------
Rock Paper Scissors game for CS101 Fall 2025 Lab 02.
This script allows a user to play a 3-round game of Rock, Paper, Scissors against the computer.
It uses the 'rich' library for colorful output.
"""

import random
from rich.console import Console
from rich.text import Text

# Create a Console object for rich output
console = Console()
"""
main.py (Starter Template)
-------------------------
Rock Paper Scissors game for CS101 Fall 2025 Lab 02.

Complete the TO-DOs to finish the game!
"""

import random
from rich.console import Console

console = Console()

choices = ['rock', 'paper', 'scissors', 'end']
num_to_choice = {'1': 'rock', '2': 'paper', '3': 'scissors', '4':'end'}

# Implements this function to get and validate the user's choice.
def get_user_choice():
	"""Prompt the user for their choice and return 'rock', 'paper', or 'scissors'."""
	# uses console.input and validate input (accept 1/2/3 or words)
	user_input = console.input("[bold]Choose rock (1), paper (2), scissors (3), end(4): [/bold]".strip().lower())
	if user_input in num_to_choice:
			user_choice = num_to_choice[user_input]
	else:
		user_choice = user_input
	if user_choice in choices:
		pass
	else:
		console.print("[red]Invalid choice. Please try again.[/red]")
	return user_choice

# Implements this function to randomly select the computer's choice.
def get_computer_choice():
	"""Randomly return 'rock', 'paper', or 'scissors'."""
	computer_coice = random.choice(choices)
	return computer_coice

# Implements this function to determine the winner of a round.
def determine_winner(user_choice, computer_choice,user_score, computer_score):
	"""Return 'user', 'computer', or 'tie' based on the choices."""
	if user_choice == computer_choice:
		# It's a tie, scores unchanged
		return user_score, computer_score
	elif (
		(user_choice == 'rock' and computer_choice == 'scissors') or
		(user_choice == 'paper' and computer_choice == 'rock') or
		(user_choice == 'scissors' and computer_choice == 'paper')
	):
		user_score += 1
	else:
		computer_score += 1
	return user_score, computer_score

# Implements this function to print the round result with color.
def print_round_result(user_choice, computer_choice):
	"""Print the choices and the winner of the round using rich colors."""
	if user_choice == computer_choice:
		console.print("[blue]It's a tie![/blue]")
	elif (
		(user_choice == 'rock' and computer_choice == 'scissors') or
		(user_choice == 'paper' and computer_choice == 'rock') or
		(user_choice == 'scissors' and computer_choice == 'paper')
	):
		console.print("[bold green]You win this round![/bold green]")
	else:
		console.print("[bold red]Computer wins this round![/bold red]")

# Implements the main game loop.
def main():
	"""Main function to run the game for 3 rounds and print the final result."""
	pygame.mixer.init()
	user_score = 0
	computer_score = 0
	rounds = 3
	# for round_num in range(1, rounds + 1):
	while True:
		user_choice = get_user_choice()
		if user_choice == 'end':
			break
		computer_choice = get_computer_choice()
		print_round_result(user_choice, computer_choice)
		user_score, computer_score = determine_winner(user_choice, computer_choice, user_score, computer_score)
		pass
	console.print(f"Computer final score: {computer_score}")
	console.print(f"User final score: {user_score}")
	if user_score > computer_score:
		console.print("[bold green]Congratulations, you win the game![/bold green]")
		my_sound = pygame.mixer.Sound(r"C:\Users\kalla\2025-2026\cs101\labs\lab04-fuchs02\Sounds\cheering.mp3")
		play_obj = my_sound.play()
		while play_obj.get_busy():
			pygame.time.wait(100)
	else:
		console.print("[bold red]Computer wins, you lost the game![/bold red]")
		my_sound = pygame.mixer.Sound(r"C:\Users\kalla\2025-2026\cs101\labs\lab04-fuchs02\Sounds\downer_noise.mp3")
		play_obj = my_sound.play()
		while play_obj.get_busy():
			pygame.time.wait(100)
	

if __name__ == "__main__":
	main()
	
