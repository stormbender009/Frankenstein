import time

from termcolor import colored

from rich.prompt import Prompt
from rich.console import Console

console = Console()

input = Prompt.ask #See user_choice

#Modules for the input. input q or press Ctrl + C and you leave
modules = """[Q] Exit (Ctrl + C)"""

def Main_Modules():
    print(modules)

    user_choice = input("Enter your choice ") #Asking you for input. See modules

    if user_choice == "q": #if the inputted module is q, it exits
        console.clear()
        exit()
    else: #if you dont use a module, it goes here.
        print(colored("Invalid choice", 'red'))
        time.sleep(1)
        Main_Modules()

if __name__ == "__main__":
    try:
        Main_Modules() #Tells you the modules every time you run the script
    except KeyboardInterrupt: #Clears the console and exits on interrupt(Ctrl + C)
        console.clear()
        print(colored("User Quit", 'red'))
        exit()
    except Exception as e: #I have no idea. I assume it depends on an unpresedented error.
        console.clear()
        print(colored("ERROR VALUE", 'red'))
        exit()