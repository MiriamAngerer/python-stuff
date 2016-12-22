menu_file = open("menu.txt", "w+")

menu = {}

while True:
    dish = raw_input("Please enter the name of the dish:")
    price = raw_input("Please enter the grade for %s: " % dish)
    menu[dish] = price # Ich scheitere daran dem Menü ein Gericht mit Key(Dish) und Value(Price) hinzuzufügen. Wie würde ich das machen?
    menu.append(menu)

    new = raw_input("Do you want to enter a new dish? (yes/no)")

    if new == "no":
        break

print "The daily menu is: %s" % menu
menu_file.write("The daily menu is: %s" % menu)

print "END"
menu_file.close()