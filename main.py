secret_word = "Ing Zhen is handsome"
guess = "ok"
guess_count = 0
guess_limit = 3
not_out_of_guesses = True

while guess != secret_word and  not_out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        print(str(guess_limit - guess_count - 1) + " guess left")
        guess_count +=1
    else:
        not_out_of_guesses = False

if not_out_of_guesses == True:
    print("You Win!")
else:
    print("Out of Guesses, You Lose!")

