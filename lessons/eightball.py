from random import randint

question: str = input("Ask a yes or no question...")
response: int = randint(0, 3)

if response == 0:
    print("Yes, definitely")
elif response == 1:
    print("Ask again later")
elif response == 2:
    print("YES")
else:
    print("My sources say no")
