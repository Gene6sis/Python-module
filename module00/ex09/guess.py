import random

print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!\n")

step = 0
rand = random.randint(1, 99)
while True :
    text = input("Your guess between 1 and 99 ?\n>> ").strip()
    if text == "exit" :
        print("Goodbye!")
        break
    try :
        number = int(text)
    except ValueError :
        print("That's not a number.")
        continue
    step += 1
    if number < rand :
        print("Too low!")
    elif number > rand :
        print("Too high!")
    elif number == rand and rand == 42 :
        print("The answer to the ultimate question of life, the universe and everything is 42.")
        print("Congratulations! You won in {step} try!")
        break
    else :
        print("Congratulations, you've got it!")
        print(f"You won in {step} attempts!")
        break