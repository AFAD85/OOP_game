from abc import ABC, abstractmethod


class Fighter(ABC):
    @abstractmethod
    def attack() -> None:
        pass



class Pokemon(Fighter):
    
    def __init__(self, name, controler):
        self.name = name
        self.health = 10
        self.attack_power = 2
        self.knocked_out = False
        self.controler = controler
        
    def attack(self, opponent):
        opponent.health -= self.attack_power  

    def set_attack_power(self, attack_power):
        """
        Sets the attack power of the pokemon
        """
        self.attack_power = attack_power
        



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
    
    
    
    