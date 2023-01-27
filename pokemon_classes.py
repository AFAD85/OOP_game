"""
this file contains all pokemon classes, and super classes
super classes placed here for the time being, will be moved later

"""
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
        pass



class Pokemon(Fighter, ABC):
    
    def __init__(self, name: str, health: int, controler: str):
        super().__init__(name, health, controler)
        self.name = name
        self.health = health
        self.attack_power = int()
        self.knocked_out = False
        self.controler = controler
    
    @abstractmethod
    def attack(self):
        pass
  
    @abstractmethod
    def set_attack_power(self):
        pass
    
    @abstractmethod  
    def special_attack(self):
        pass    
    
    def display_stats(self):
        print(f"{self.name} has {self.health} left.")
    

        
        
class Charmander(Pokemon):
    
    def __init__(self, name, health, controler):
        super().__init__(name, health, controler)
        self.name = name
        self.health = health
        self.controler = controler
        self.type = "Fire"
        self.attack_power = int()
        
    def special_attack(self):
        self.special_attack_name = "Fire breath"
        self.special_attack_type = "Fire"
        self.special_attack_damage = int()
        
    def set_attack_power(self, attack_power):
        """
        Sets the attack power of the pokemon
        """
        self.attack_power = attack_power
        
class Pikachu(Pokemon):
    
    def __init__(self, name, health, controler):
        super().__init__(name, health, controler)
        self.name = name
        self.health = health
        self.controler = controler
        self.type = "Lightning"
        self.attack_power = int()
        

        
class Squirtle(Pokemon):
    
    def __init__(self, name, health, controler):
        super().__init__(name, health, controler)
        self.name = name
        self.health = health
        self.controler = controler
        self.type = "Water"
        self.attack_power = int()
        
class Bulbasaur(Pokemon):
    
    def __init__(self, name, health, controler):
        super().__init__(name, health, controler)
        self.name = name
        self.health = health
        self.controler = controler
        self.type = "Plant"
        self.attack_power = int()

class MisterMime(Pokemon):
    
    def __init__(self, name, health, controler):
        super().__init__(name, health, controler)
        self.name = name
        self.health = health
        self.controler = controler
        self.type = "Nightmare"
        self.attack_power = int()
        
