"""
File containing character selection logic, will be called by main on user input
will itself look either directly at specified classes file or use character selection interface (still working out the logic)


Preliminary design sketch:
1 main file is used to call for character selection
2 character selection is initialized based on whos team (player or computer) is being defined
3 character classes are loaded and displayed
4 user selects a character and sets required values (name etc.)
5 repeated untill team is full
6 team object is returned to main which picks it up and allows for it to be used in the game loop



"""



class PlayerCharacterSelection:
    
    def __init__(self):
        self.team_list = []
        self.character_1 = self.team_list[0]
        self.character_2 = self.team_list[1]
        self.character_3 = self.team_list[2]

    

# class ComputerCharacterSelection:
    
    




class PlayerCharacterSelection:
    
    def __init__(self):
        self.selection = []
        self.character_1 = None
        self.character_2 = None
        self.character_3 = None
        

        self.selection.append(Pokemon("Bulbasaur", "player"))
        self.selection.append(Pokemon("Charmander", "player"))
        self.selection.append(Pokemon("Pikachu", "player"))
    
    
    
    
    
# class ComputerCharacterSelection:
    
    
    
    