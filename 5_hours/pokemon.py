# pokemon module

class PokemonFighter():
    
    def __init__(self):
        self.health = 0
        self.attack_power = 0
        self.speed = 0
        
    def attack(self, computer):
        attack = self.attack_power - computer.attack_power
        return attack

    
    




