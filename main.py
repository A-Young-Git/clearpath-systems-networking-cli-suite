import subprocess
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# colorama color palette
class Palette:
    TITLE = Fore.LIGHTGREEN_EX
    PROMPT = Fore.CYAN
    HIGHLIGHT = Style.RESET_ALL + Fore.YELLOW + Style.DIM
    DIM = Fore.WHITE + Style.DIM
    ERROR = Fore.RED
    RESET_DIM = Style.RESET_ALL + DIM

def main():
    print(f"{Palette.TITLE}\n***** ClearPath Systems Networking Suite *****")

    while True:
        print(f"{Palette.PROMPT}\nPlease choose a numeric option below:\n")
        print(f"{Palette.DIM}1. Test the reachability of a host")
        print(f"{Palette.DIM}2. Perform a domain name lookup")
        print(f"{Palette.DIM}3. Run all tests")
        print(f"{Palette.DIM}4. Quit the program")

        choice = input(f"{Palette.PROMPT}\nEnter your choice: ")

        try:
            choice = int(choice)
        except ValueError:
            print(f"{Palette.ERROR}\nInvalid choice: please enter a number")
            continue

        actions = {
            1: lambda: subprocess.run(["ping", "-c", "5", hostname]),
            2: lambda: subprocess.run(["nslookup", hostname]),
            3: lambda: (actions.get(1)(), actions.get(2)()),
            4: lambda: quit(),
        }

        action = actions.get(choice)
        if action:
            if choice in (1, 2, 3):
                hostname = input(f"{Palette.PROMPT}\nPlease enter the hostname or IP address you wish to run the test(s) on: ")
            action()
        else:
            print(f"{Palette.ERROR}\nInvalid choice")

if __name__ == "__main__":
    main()
