actual_number = 55
attempts = 0

while True:
    attempts +=1
    guess = (int(input("Guess the number 1 to 100:/n")))
    score = (51 - attempts)
    if guess<actual_number:
        print("Your guess was too low")

    elif guess>actual_number:
            print("Your guess was too high")

    else:
        print(f"You guessed the number in {attempts} attempts", score)
        break
        print("Thank You")