secret = 7
guess = int(raw_input("secret: "))
wrong = "Nice try! Maybe next time!"
right = "Congratulations!"

if guess == secret:
    print right
else:
    print wrong
