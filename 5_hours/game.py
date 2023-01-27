from character_creation import Pokemon
from typing import Protocol

class GameLoop():
    
    def __init__(self, player_char, computer_char):
        self.player_char = player_char
        self.computer_char = computer_char



    def fight_turn_based(self):
        self.turn_count = 0
        
        print("Fight!")
        
        
        while True:
            

            self.turn_count += 1
            
            self.display_turn_report()
            
            
            player_turn_input = self.request_player_action()
                

            
            
            if player_turn_input == "1":
                self.execute_fight_turn()
                


            if self.player_char.knocked_out:
                
                print(f"{self.player_char.name} has been knocked out! {self.computer_char.name} wins!")
                break
            
            
            if self.computer_char.knocked_out:
                
                print(f"{self.computer_char.name} has been knocked out! {self.player_char.name} wins!")
                break
            
            
            if player_turn_input == "2":
                # add player_character_select function/class
                pass
            
            if player_turn_input == "0":
                break
            

            
    def execute_fight_turn(self):
        
        self.player_char.health -= self.computer_char.attack_power
        self.check_fighter_knocked_out()
        
        
        
        self.computer_char.health -= self.player_char.attack_power
        self.check_fighter_knocked_out()

    def check_fighter_knocked_out(self):
        
        if self.player_char.health <= 0:
            self.player_char.knocked_out = True
            return self.player_char.knocked_out
        
        elif self.computer_char.health <= 0:
            self.computer_char.kocked_out = True
            return self.computer_char.knocked_out
        
        else:
            return False



    def display_turn_report(self):
        
        print(f"""
            Turn {self.turn_count} has started!
            Your {self.player_char.name} has {self.player_char.health} health left
            The computer' {self.computer_char.name} has {self.computer_char.health} health left
            """
            )


    
            
    def request_player_action(self):
        
        print("please input action\n1. Attack\n2. Change fighter\n0. Exit Game\n")
        player_input = input("type 1, 2 or 0 and press enter")
        return player_input
        
# class Fighter(Protocol):
        
#     def attack(self, character:Attack):
#         ...
        
# class StreetFighter():
#     def attack(self, opponent):
#         opponent.health -= self.attack_power
        
player = Pokemon("Charmander", "player")
player.set_attack_power(5)
computer = Pokemon("Pikachu", "computer")

game = GameLoop(player, computer)
game.fight_turn_based()
