secret = 7
guess = int(raw_input("secret: "))
wrong = "Try again!"
right = "Congratulations!"

if guess == secret:
    print right
else:
    print wrong
