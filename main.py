import random
from logbook import menu_logbook
from NumberGame import menu_numbergame

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

def menu():
    print(f"{purple} WELCOME TO THE NANO PRIVET APP{reset}")
    name = input("\nHi, what is your name?: \n")

    while True:
        keuzen = input(f"hi {name}, what do you want to do today?\n1.numbergame\n2.logbook\n")
        print(keuzen.lower())
        if keuzen.lower == "numbergame" or keuzen == "1":
            menu_numbergame()
        elif keuzen.lower == "logbook" or keuzen == "2":
            menu_logbook()
        elif keuzen == "exit":
            print('you chose exit')

        else:
            print('you chose wrong option')
menu()
#