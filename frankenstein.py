import time

from termcolor import colored

from rich.prompt import Prompt
from rich.console import Console

console = Console()

input = Prompt.ask

modules = """[Q] :door: Exit (Ctrl + C)"""

def Main_Modules():
    print(modules)

    user_choice = input("Enter your choice ")

    if user_choice == "q":
        console.clear()
        exit()
    else:
        print(colored("Invalid choice", 'red'))
        time.sleep(1)
        Main_Modules()

if __name__ == "__main__":
    try:
        #----------------------
        Main_Modules()
    except KeyboardInterrupt:
        console.clear()
        print(colored("User Quit", 'red'))
        exit()
    except Exception as e:
        console.clear()
        print(colored("ERROR VALUE", 'red'))
        exit()