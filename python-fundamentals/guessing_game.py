import random

attempts = 0
number_to_guess = random.randint(1, 100)
print("Welcome to the Guessing Game!")
while True:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < number_to_guess:
        print("Too low! Try again.")
        attempts += 1
        #continue
    elif guess > number_to_guess:
        print("Too high! Try again.")
        attempts += 1
        #continue
    else:
        print("Congratulations! You've guessed the number.")
        break

print(f"It took you {attempts} attempts to guess the number.")