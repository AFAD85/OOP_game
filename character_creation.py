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
    
    def __init__(self, name, health, controler):
        super().__init__(name, health)
        self.name = name
        self.health = health
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
        
    def display_stats():
        
        
class Charmander(Pokemon):
    
    def __init__(self, name, controler)


class PlayerCharacterSelection:
    
    def __init__(self):
        self.character_1 = None
        self.character_2 = None
        self.character_3 = None

    

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
    
    
    
    