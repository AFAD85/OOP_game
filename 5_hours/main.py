def main():
    
    
    # displays main menu

    
    while True:
        print(f"-------------------------------------\n",
        "Welcome to Pokemon fighting!\n",
        "Main Menu\n",
        "1. Start Game\n",
        "2. Select fighters\n",
        "0. Exit\n"
        )
        
        
        # asks user for input
        selection = get_user_input_main_menu()
        
        # checks user input and proceeds with corresponding function
        if selection == "1":
            print("starting game!")
            # game loop initilized here
            break
        
        if selection == "2":
            print("Select fighters")
            # selection menu initialized here
            break

        if selection == "0":
            print("exiting game")
            break

        else:
            print("Invalid input, please select 1, 2 or 0 and press enter")


def get_user_input_main_menu():
    selection = input("type 1, 2 or 0 and press enter - "
                    )
    return selection
    
    
    
    
    








if __name__ == "__main__":
    main()

