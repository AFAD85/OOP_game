from abc import ABC, abstractmethod



class Fighter(ABC):
    
    def __init__(self, name: str, health: int, controler: str):
        self.name = name
        self.health = health
        self.controler = controler
    
    @abstractmethod
    def attack() -> None:
        pass
    
    @abstractmethod
    def display_stats() -> None:



class Pokemon(Fighter):
    
    def __init__(self, name: str, health: int, controler: str):
        super().__init__(name, health, controler)
        self.name = name
        self.health = health
        self.attack_power = int()
        self.knocked_out = False
        self.controler = controler
        
    def attack(self, opponent):
        opponent.health -= self.attack_power  

    def set_attack_power(self, attack_power):
        """
        Sets the attack power of the pokemon
        """
        self.attack_power = attack_power
        
    def display_stats(self):
        print(f"{self.name} has {self.health} left.")
        
        
class Charmander(Pokemon):
    
    def __init__(self, name, health, controler, type: str):
        super().__init__(name, health, controler)
        self.name = name
        self.health = health
        self.controler = controler
        self.type = type
        self.attack_power = int()


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
    
    
    
    