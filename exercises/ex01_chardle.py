"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730556906"

five_character_word: str = input("Enter a 5-character word: ")
if len(five_character_word)!= 5:
    print("Error: Word must contain 5 characters ")
    exit()

character_guess: str = input("Enter a single character: ")
if len(character_guess)!=1:
    print("Error: Character must be a single character. ")
    exit()

print("Searching for " + character_guess + " in " + five_character_word)

letter_instances: int = 0

if five_character_word[0]==character_guess:
    print(character_guess + " found at index 0 ")
    letter_instances = letter_instances + 1
if five_character_word[1]==character_guess:
    print(character_guess + " found at index 1 ")
    letter_instances = letter_instances + 1
if five_character_word[2]==character_guess:
    print(character_guess + " found at index 2 ")
    letter_instances = letter_instances + 1
if five_character_word[3]==character_guess:
    print(character_guess + " found at index 3 ")
    letter_instances = letter_instances + 1
if five_character_word[4]==character_guess:
    print(character_guess + " found at index 4 ")
    letter_instances = letter_instances + 1

if letter_instances > 1:
    print(str(letter_instances) + " instances of " + character_guess + " found in " + five_character_word)
else:
    if letter_instances == 1:
        print("1 instance of " + character_guess + " found in " + five_character_word)
    else:
        print("No instances of " + character_guess + " found in " + five_character_word)
