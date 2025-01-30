# function to manaage tickets and attendees
def ticket_attendee():
    price_one = 100
    price_three = 250
    price_vip = 450
    attendees = []
    while True:
        choice = input("""1. see ticket prices
2. adjust ticket prices
3. add attendee information
4. see attendee information
5. End
Enter the number of the thing you would like to do: """)
        if choice == "1":
            print("the price for a 1-day pass is $", price_one, ", the price for a 3-day pass is $", price_three, ", the price for a VIP pass is $", price_vip)
        elif choice == "2":
            price_one = float(input("what should the 1-day pass cost: "))
            price_three = float(input("what should the 3-day pass cost: "))
            price_vip = float(input("what should the VIP pass cost: "))
        elif choice == "3":
            name = input("enter the name of the attendee: ")
            age = input("enter the age of the attendee: ")
            ticket_type = input("""1. 1-day pass
2. 3-day pass
3. VIP pass
Enter the number of the type of ticket the attendee bought: """)
            if ticket_type == "1":
                ticket_type = "1-day pass"
            elif ticket_type == "2":
                ticket_type = "3-day pass"
            elif ticket_type == "3":
                ticket_type = "VIP pass"
            else:
                print("That is not an option.")
                continue
            attendee = (name, age, ticket_type)
            attendees.append(attendee)
        elif choice == "4":
            for p in range(len(attendees)):
                print(attendees[p])
        elif choice == "5":
            break
        else:
            print("That is not an option.")
            continue

ticket_attendee()