# Andrea Mejias
# 11/19/2024
# P5HW
# Create a text based game using functions

import random
import time
from typing import Dict, Tuple

class Character:
    # Call the attributes needed for the battles to simulate
    def __init__(self, name: str, health: int):
        self.name = name
        self.max_health = health
        self.health = health
        self.meme_energy = 250
        self.defense = 250
        self.emotions = 50
        self.max_emotions = 300

    # Set the code that will end the simulation when a character dies
    def is_alive(self) -> bool:
        return self.health > 0

    def get_emotion_increase_range(self, condition: str) -> tuple:
        # Do If Else statements for SMGs to have higher emotion increases
        if self.name.startswith('SMG'):
            increase_ranges = {
                'low_meme': (20, 30),
                'low_health': (30, 45)
            }
        else:
            increase_ranges = {
                'low_meme': (15, 25),
                'low_health': (25, 40)
            }
        return increase_ranges[condition]

    # Use If Else Statements to determine an increase in emotions by low values
    def update_emotions(self) -> str:
        emotion_message = ""
        original_emotions = self.emotions
        
        if self.meme_energy < 100:
            min_increase, max_increase = self.get_emotion_increase_range('low_meme')
            increase = random.randint(min_increase, max_increase)
            self.emotions = min(self.max_emotions, self.emotions + increase)
            if self.emotions != original_emotions:
                emotion_message += f"\n{self.name}'s low meme energy causes emotions to rise by {increase}!"
        
        if self.health < 100:
            min_increase, max_increase = self.get_emotion_increase_range('low_health')
            increase = random.randint(min_increase, max_increase)
            self.emotions = min(self.max_emotions, self.emotions + increase)
            if self.emotions != original_emotions:
                emotion_message += f"\n{self.name}'s low health intensifies their emotions by {increase}!"
        
        return emotion_message

    # Determine damage given by characters
    def take_damage(self, damage: int) -> None:
        actual_damage = max(0, damage - (self.defense // 10))
        self.health = max(0, self.health - actual_damage)
        self.defense = max(0, self.defense - (damage // 4))

    # State the damage ranges for specific characters using if statements
    def get_damage_range(self, attack_type: str) -> tuple:
        # Damage ranges for SMG characters
        if self.name.startswith('SMG'):
            damage_ranges = {
                'combined': (40, 60),
                'emotion': (30, 45),
                'bland': (25, 40),
                'basic': (15, 25)
            }
        # Damage ranges for SD characters
        elif self.name.startswith('SD') and self.name not in ['SDV', 'Niles']:
            damage_ranges = {
                'combined': (50, 70),
                'emotion': (40, 55),
                'bland': (35, 50),
                'basic': (25, 35)
            }
        # Damage ranges for SDV and Niles
        else:  # SDV and Niles
            damage_ranges = {
                'combined': (60, 80),
                'emotion': (50, 65),
                'bland': (45, 60),
                'basic': (35, 45)
            }
        return damage_ranges[attack_type]
    
    # Set the types of attacks depending on attributes
    def attack(self, target: 'Character') -> Tuple[str, int]:
        if self.meme_energy >= 100 and self.emotions >= 100:
            # Strong attack
            min_damage, max_damage = self.get_damage_range('combined')
            damage = random.randint(min_damage, max_damage)
            self.meme_energy -= 30
            self.emotions -= 20
            return f"{self.name} unleashes a powerful combined attack!", damage
        elif self.emotions >= 100 and self.meme_energy < 100:
            # Emotion Attack
            min_damage, max_damage = self.get_damage_range('emotion')
            damage = random.randint(min_damage, max_damage)
            self.emotions -= 25
            return f"{self.name} channels their emotions into an attack!", damage
        elif self.meme_energy >= 100 and self.emotions < 100:
            # Bland Attack
            min_damage, max_damage = self.get_damage_range('bland')
            damage = random.randint(min_damage, max_damage)
            self.meme_energy -= 35
            return f"{self.name} performs a bland but effective attack!", damage
        else:
            # Basic attack
            min_damage, max_damage = self.get_damage_range('basic')
            damage = random.randint(min_damage, max_damage)
            return f"{self.name} performs a basic attack!", damage

# Display the character list for the user to choose their two characters
def create_characters() -> Dict[str, Character]:
    characters = {}
    
    # SMG characters (200 health)
    for i in [0, 1, 2, 3, 4]:
        characters[f'SMG{i}'] = Character(f'SMG{i}', 200)
    
    # SD characters (250 health)
    for c in ['A', 'K', 'J', 'M']:
        characters[f'SD{c}'] = Character(f'SD{c}', 250)
    
    # Special characters (300 health)
    characters['SDV'] = Character('SDV', 300)
    characters['Niles'] = Character('Niles', 300)
    
    return characters

def display_stats(char1: Character, char2: Character) -> None:
    print("\nCurrent Stats:")
    print(f"{char1.name}: Health: {char1.health}/{char1.max_health} | Meme Energy: {char1.meme_energy}/250 | Emotions: {char1.emotions}/300 | Defense: {char1.defense}/250")
    print(f"{char2.name}: Health: {char2.health}/{char2.max_health} | Meme Energy: {char2.meme_energy}/250 | Emotions: {char2.emotions}/300 | Defense: {char2.defense}/250")

# Set the timer for when each turn ends
def countdown_timer():
    print("\nNext turn starting in:")
    for i in range(5, 0, -1):
        print(f"{i}...")
        time.sleep(1)
    print("Fight!")

# Simulate the battle
def battle(char1: Character, char2: Character) -> None:
    round_num = 1
    
    while char1.is_alive() and char2.is_alive():
        print(f"\nTurn {round_num}")
        display_stats(char1, char2)
        
        emotion_updates = char1.update_emotions() + char2.update_emotions()
        if emotion_updates:
            print(emotion_updates)
        
        # First character attacks
        message, damage = char1.attack(char2)
        print(f"\n{message}")
        char2.take_damage(damage)
        print(f"{char2.name} takes {damage} damage!")

        # Set the if statement to determine who wins if one dies
        if not char2.is_alive():
            print(f"\n{char1.name} wins!")
            break
            
        # Second character attacks
        message, damage = char2.attack(char1)
        print(f"\n{message}")
        char1.take_damage(damage)
        print(f"{char1.name} takes {damage} damage!")

        # Set the if statement to determine who wins if one dies
        if not char1.is_alive():
            print(f"\n{char2.name} wins this battle!")
            break
            
        # Regenerate some energy each round to maintain battle stats
        for char in [char1, char2]:
            char.meme_energy = min(250, char.meme_energy + random.randint(10, 20))
            char.defense = min(250, char.defense + random.randint(5, 15))
        
        round_num += 1
        countdown_timer()

# Use while loops with all classes defined to set the game up
def main():
    while True:
        characters = create_characters()
        print("Welcome to Cosmology Guardians, where you can watch the tiers of the multiverse test their own powers!!")
        print("\nAvailable characters:", ", ".join(characters.keys()))

        while True:
            char1_name = input("\nEnter the name of the first character: ").strip()
            if char1_name in characters:
                break
            # Print out invalid message if a name outside the character list is entered
            print("Invalid character name! Please try again!")
            
        while True:
            char2_name = input("Enter the name of the second character: ").strip()
            if char2_name in characters and char2_name != char1_name:
                break
            # Print out invalid message if a name outside the character list is entered
            print("Invalid character name or same as first character! Please try again!")
        
        battle(characters[char1_name], characters[char2_name])
        
        play_again = input("\nWould you like to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing Cosmology Guardians!")
            break

# Call the main
if __name__ == "__main__":
    main()
