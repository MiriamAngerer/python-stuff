import random

def main():
    country_capital_dict = {"Slovenia": "Ljubljana", "Croatia": "Zagreb", "Austria": "Vienna"}

    while True:
        random_num = random.randint(0, 2)
        country = country_capital_dict.keys()[random_num]

        guess = raw_input("What is the capital of %s? " % country)

        check_guess(guess, country, country_capital_dict)

        again = raw_input("Would you like to continue this game? (yes/no) ")
        if again == "no":
            break

    print "END"
    print "_________________________"


def check_guess(guess, country, country_capitial_dict):
    capital = country_capitial_dict[country]

    if  guess == capital:
        print "Correct! The capital of %s is indeed %s." % (country, capital)
        return True
    else:
        print "Sorry, you are wrong. The capital of %s is %s." % (country, capital)
        return False

if __name__ == "__main__":
    main()

