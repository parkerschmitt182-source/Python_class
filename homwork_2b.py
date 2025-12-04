import random
play = "Y"
print("Hello! I'm your computer. What is your name? ")
user_name = input().title()
print(f"Well, {user_name}, I would like to play a number guessing game.")
while play == "Y":
    NumOfTry = 10
    LimitLow = 1
    LimitHigh = 100
    print(f"Please think of a whole number between {LimitLow} and {LimitHigh}. I am about to try to guess it in {NumOfTry} tries. ")
    randomGuess = random.randint(LimitLow,LimitHigh)
    while NumOfTry != 0:
        print(f"\n{NumOfTry} attempts left")
        print(f"I guess: {randomGuess}")
        print ("H = too high")
        print ("L = too low")
        print ("C = correct ")
        HumanAnswer = str(input ("\nSo did I guess right?").upper())
        
        if HumanAnswer == "C":
            print("\nWOO HOO! I won!")
            NumOfTry = 0
        elif HumanAnswer == "H":
    
            LimitHigh = randomGuess
            print(f"\nHmm, so your number is between {LimitLow} and {LimitHigh}")
            NumOfTry -= 1
            randomGuess = random.randint(LimitLow,LimitHigh)
        elif HumanAnswer == "L":
           
            LimitLow = randomGuess
            print(f"\nHmm, so your number is between {LimitLow} and {LimitHigh}")
            NumOfTry -= 1
            randomGuess = random.randint(LimitLow,LimitHigh)
        
        else:
            print("\n Please enter a valid answer. H, L and C are the valid choices.")
        if LimitLow == LimitHigh:
            print("It looks like you are cheating")
            import sys
            sys.exit()
    else:
        if HumanAnswer != "C":
            print("\nLooks like you win this time!")
        print("\nType Y if you want to play again. ")
        play = input ().upper
else:
    print(f"\nThank you for playing with me, {user_name}.")