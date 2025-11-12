import random # Choose a word randomly
import os # Clean the screen
import getpass # Request to write a word without it being displayed
from colorama import Fore, Style, init # Add color in the game
import time # Animation

# Initialisation of colorama
init(autoreset=True)

# Hanged
HANGED = [
	"""






    =========
    """,
	"""





           |
    =========
    """,
    """




           |
           |
    =========
    """,
	"""


           
           |
           |
           |
    =========
    """,
	"""


           |
           |
           |
           |
    =========
    """,
	"""

           |
           |
           |
           |
           |
    =========
    """,
    """
       +---+
           |
           |
           |
           |
           |
    =========
    """,   
    """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

def	load_words(file="words.txt"):
	if not os.path.exists(file):
		print(Fore.RED, "Error when opening file " + file + "\n")
		exit(1)
	with open(file, "r", encoding="utf-8") as f: # Open the file in "reading" mode. The file is now 'f'
		return [word.strip().lower() for word in f if word.strip()] # Create a list. At each line of the file. Word will be "cat\n" until there are no more words in the file. .strip() remove the spaces at the beginning and the end of each line. The list will look like this : ["cat", "dog", "apple"]... 

def intro():
	welcome = "​🕹️​ WELCOME TO THE HANGMAN GAME ​🕹️​"
	for letter in welcome:
		print(Fore.MAGENTA + letter, end="", flush=True)
		time.sleep(0.05)
	print("\n")

def play(secret_word):
	guessing_word = ["_"] * len(secret_word) # word to guess * the length of it so "cat" will be ["_", "_", "_"]
	attempt = set() # all the letters tried. Set has never duplicates
	errors = 0
	max_errors = len(HANGED) - 1

	print(f"\n{Fore.CYAN}​🕹️​ The word has {len(secret_word)} letters.\n")

	while errors < max_errors and "_" in guessing_word:

		print(Fore.BLUE + HANGED[errors]) # Current hanged
		print(f"{Fore.CYAN}Word = {Fore.WHITE}{' '.join(guessing_word)}\n") # Current word when guessing him.
		print(f"{Fore.RED}• Letters tried : {', '.join(sorted(attempt)) if attempt else '(none remaining)'}") # .join() transforms the sorted list into a space- or comma-separated or  string.
		print(f"{Fore.RED}• Remaining trials : {max_errors - errors}\n")

		letter = input(Fore.CYAN + "Choose a letter : ").lower().strip()

		if len(letter) != 1 or not letter.isalpha():
			print(Fore.RED + "​⛔​ Enter a single valid letter\n")
			continue

		if letter in attempt:
			print(Fore.RED + "​⛔​ You already try this letter\n")
			errors+= 1
			continue
		attempt.add(letter) # Add each letter to the list with set()

		if letter in secret_word:
			for i, j in enumerate(secret_word): # enumerate() scans the word letter by letter while having the clue for each letter.
				if j == letter:
					guessing_word[i] = letter # if it's good, replace the "_" by the good letter
			os.system("cls" if os.name == "nt" else "clear")
			print(Fore.GREEN + "​🟢 Well done !\n")
			continue
		else:
			errors += 1
			os.system("cls" if os.name == "nt" else "clear")
			print(Fore.RED + "🔴 Wrong Choice !\n")
			continue

		os.system("cls" if os.name == "nt" else "clear")

	print(Fore.MAGENTA + HANGED[errors])
	if "_" not in guessing_word:
		print(f"{Fore.GREEN}🎉 Congrats, you found the word : {Fore.WHITE}{secret_word}")
	else:
		print(f"{Fore.RED}❌​ Looser ! The word was : {Fore.WHITE}{secret_word}")
	print(Style.RESET_ALL)

def	main():

	os.system("cls" if os.name == "nt" else "clear") # If we are on windows, clear the terminal is "cls", otherwise if we are on Linux/Mac, it's "clear"

	intro()
	while True:
		print(f"{Fore.MAGENTA}=== ​🎮​ HANGMAN GAME ==={Style.RESET_ALL}")
		print(f"{Fore.YELLOW}1 : Single player mode (random word)")
		print(f"{Fore.YELLOW}2 : Two player mode")
		print(f"{Fore.YELLOW}3 : Leave the game{Style.RESET_ALL}")
		choice = input(Fore.CYAN + "Choose an option 👉​ " + Style.RESET_ALL).strip() # input() wait for the player to type their choice and press Enter

		if choice == "1":
			words = load_words() # All the words are loaded in words
			secret_word = random.choice(words) # It choose one word randomly
			play(secret_word)

		elif choice == "2":
			print(f"\n{Fore.CYAN}👥​ Two player mode selected !")

			while True:
				print(f"{Fore.YELLOW}Player 1, Choose a word 👉 ")
				secret_word = getpass.getpass(Fore.CYAN + "Secret word : " + Style.RESET_ALL).lower().strip() # getpass.getpass retrieves input from the terminal without displaying it.

				print(f"\n{Fore.CYAN}You entered this word : {Fore.WHITE}{secret_word}{Fore.CYAN}. Is it good ?")
				confirm = input(f"{Fore.YELLOW}Confirm ? (Y/N) : {Style.RESET_ALL}").strip().lower()

				if confirm == "Y" or confirm == "y" or confirm == "yes" or confirm == "YES":
					break
				else:
					print(Fore.RED + "Rewrite it.\n")

			os.system("cls" if os.name == "nt" else "clear")
			print("\n" * 40)
			print(f"{Fore.YELLOW}Player 2, It's up to you ! Good luck !")
			play(secret_word)

		elif choice == "3":
			print(Fore.CYAN + "🫶 Thanks for playing ! See you later ! 🫶​")
			break

		else:
			print(Fore.RED + "❌ Invalid choice. Try again between 1-3.\n")

if __name__ == "__main__":
	main()