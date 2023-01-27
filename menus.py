"""
menu file

"""
import sys


class MainMenu:
    def __init__(self):
        self.options = {
            "1": self.option_1,
            "2": self.option_2,
            "3": self.option_3,
            "0": self.exit
        }

    def display(self):
        print("Main Menu:")
        print("1. Start Game")
        print("2. Character Select")
        print("3. Settings")
        print("4. Exit")

    def run(self):
        while True:
            self.display()
            choice = input("Enter an option: ")
            action = self.options.get(choice)
            if action:
                action()
            else:
                print(f"{choice} is not a valid option.")

    def option_1(self):
        print("Starting Game!")

    def option_2(self):
        print("Character select")

    def option_3(self):
        print("Settings")

    def exit(self):
        print("Exiting...")
        sys.exit()

def main():
    menu = MainMenu()
    menu.run()

if __name__ == "__main__":
    main()

    
    
# class CharacterSelectionMenu():
    
    