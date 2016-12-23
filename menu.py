menu_file = open("menu.txt", "w+")

menu = {}

while True:
    dish = raw_input("Please enter the name of the dish:")
    price = raw_input("Please enter the price for %s: " % dish)
    menu[dish] = price

    new = raw_input("Do you want to enter a new dish? (yes/no)")

    if new == "no":
        break

print "The daily menu is: %s" % menu
menu_file.write("The daily menu is: %s" % menu)

print "END"
menu_file.close()