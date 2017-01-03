import random

def main():
    print "Welcome to the Lottery numbers generator 3000!" + "\n"

    lottery_numbers = []
    amount = int(raw_input("Enter the amount of lottery numbers: "))

    for i in range(0, amount):
        number = random.randint(1,49)
        lottery_numbers.append(number)

    lottery_numbers.sort()
    print "Your lucky numbers are: %s" % str(lottery_numbers)[1:-1] + "\n"
    print "END"

if __name__ == "__main__":
    main()








