import random

print "Welcome to Secret Number 1.2. Guess the secret number between 1 and 10!" + "\n"

def main():
    secret = random.randint(1, 10)
    guess = 0

    while guess != secret:
        guess = int(raw_input("Take a guess: "))

        if guess == secret:
            print "You did it - Congratulations! It's number %s!" % str(secret)

        elif guess > 10 or guess < 1:
            print "Your number is needs to be between 1 and 10!"

        else:
            print "Sorry, %s is not correct." % str(guess)
            if guess > secret:
                print "Too high!"
            else:
                print "Too low!"


if __name__ == "__main__":
    main()