pink = "\033[95m"
purple = "\033[35m"
grey= "\033[37m"
reset= "\033[0m"
grey_background = "\033[100m"
pinkt_background = "\033[45m"
RESET = "\033[0m"
yellow= "\033[93m"
green= "\033[92m"
blue= "\033[34m"
red = '\33[91m'


def logbook():
    print(f"{pink}Welcome to Logbook\n")
    date= input("Enter the date of today(dd-mm-yyyy): \n")
    feelings = input("put your feelings down to relief: \n")
    f"logbook_{date}.txt"

    with open ('logbook.txt', 'a') as file:
           file.write(f"{date}: {feelings}\n")

    print("your feelings are saved\n"
          "you will return to the menu\n")

def read_logbook():
    while True:
        date = (input("type the date of the day you want to read in: "))
        filename = f"logbook_{date}.txt"

        try:
            with open(filename, 'r') as file:
                inhoud = file.readlines()
                if inhoud:
                    print(f"\nYour feelings from {date}:")
                    for line in inhoud:
                        print(line.strip())
                else:
                    print(f"There are no feelings recorded for {date}.")
        except FileNotFoundError:
            print(f"There are no feelings for the date {date}.")

        input("Do you want to try another date? (yes or no): ")
        if exit == "no":
            return None
        elif exit == "yes":
            print("let's write another entry!")

def menu_logbook():
    while True:
        logbook_menu = (
             "\nWelcome to the logbook\n"
              f"{pink} 1.Write your feelings{reset}\n"
              f" {purple}2.Read your feelings{reset}\n"
              f" {grey}3.exit.{reset}"
        )
        print(logbook_menu)

        keuzen = input("What do you want to do today? (chose between 1 and 3): ")

        if keuzen == "1":
             print("you chose for write your feelings\n")
             logbook()
        elif keuzen == "2":
            print("u chose for read your feelings\n")
            read_logbook()
        elif keuzen == "3":
            print("you chose to exit, I hope you enjoy your day\n")
            return
        else:
            print("That's not a valid option")

        return