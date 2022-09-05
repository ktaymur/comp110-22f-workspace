"""One shot guess wordle!"""

__author__ = "730556906"

secret: str = "python"
guess: str = input(f"What is your {len(secret)}-letter guess? ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
while len(guess) != len(secret):
    guess = input(f"That was not {str(len(secret))} letters! Try again: ")

i: int = 0
s: str = ""
while i < len(secret):
    if secret[i] == guess[i]:
        s = s + GREEN_BOX
    else:
        index_match: int = 0
        character_present: bool = False
        while character_present is False and index_match < len(secret):
            if secret[index_match] == guess[i]:
                s = s + YELLOW_BOX
                character_present = True
            else:
                index_match += 1
        if character_present is False:
            s = s + WHITE_BOX
        
    i = i + 1
print(s)
if len(guess) == len(secret) and guess == secret:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
