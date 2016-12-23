while True:
    number = int(raw_input("Please enter a number between 1 and 100: "))

    if number < 1:
        print "Your number is smaller than 1!"

    elif number > 100:
        print "Your number is bigger than 100!"

    else:
        for i in range(1, number + 1):
            if i % 15 == 0:
                print "FizzBuzz"
            elif i % 3 == 0:
                print "Fizz"
            elif  i % 5 == 0:
                print "Buzz"
            else:
                print i
        break