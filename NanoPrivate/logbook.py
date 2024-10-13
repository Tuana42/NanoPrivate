
#kleuren die ik kan gebruiken.
pink = "\033[95m"
purple = "\033[35m"
grey= "\033[37m"
reset= "\033[0m"
yellow= "\033[93m"
green= "\033[92m"
blue= "\033[34m"
red = '\33[91m'
grey_background = "\033[100m"
pinkt_background = "\033[45m"
RESET = "\033[0m"

"""Dit is het logbook, de lezer typte hier zijn/haar/hen gevoelens uit"""
def logbook():
    date= input("Enter the date of today(dd-mm-yyyy): \n")
    feelings = input("put your feelings down to relief: \n")

    # f"logbook_{date}.txt"

    with open ('logbook.txt', 'a') as file:
           file.write(f"{date}: {feelings}\n")

    print(f"\n{pink}your feelings are saved"
          f"\n{purple}you will return to the menu\n")
    return menu_logbook()


"""De lezer kan hier zijn/haar/hen gevoelens terug lezen"""
def read_logbook():

    while True:
        date = (input(f"{purple}type the date of the day you want to read in dd-mm-yyyy: "))
        print(f"\n{purple}Your feelings from {date}:")

        with open('logbook.txt', 'r') as file:
            inhoud = file.readlines()

            if inhoud:
                date_exist = False

                for line in inhoud:
                    if line[0:10] == date:
                        print(line.strip())
                        date_exist = True
                        break

                if not date_exist:
                    print(f"{purple}There are no feelings for the date {date}")
                    continue
            else:
                print("please enter a valid date")
                continue

        retry = input("Do you want to try another date? (yes or no): \n")
        if retry == "no":
            print("you will return to the menu\n")
            menu_logbook()
        elif retry == "yes":
            print("let's write another entry!\n")
        return read_logbook()

"""Dit is het menu van het logbook. """
def menu_logbook():
    print(f"{pink}Welcome to the logbook\n")

    while True:
        logbook_menu = (f"{pink}1.Write your feelings{reset}\n"
                        f"{purple}2.Read your feelings{reset}\n"
                        f"3.exit\n")

        print(logbook_menu)

        keuzen = input(f"{pink}What do you want to do today? (chose between 1 and 3): ")

        if keuzen == "1":
             print("You chose for write your feelings\n")
             logbook()
        elif keuzen == "2":
            print("u chose for read your feelings\n")
            read_logbook()
        elif keuzen == "3":
            print("you chose to exit, I hope you enjoy your day\n")
            from main import menu
            menu()

        else:
            print("That's not a valid option")
        return menu_logbook()
