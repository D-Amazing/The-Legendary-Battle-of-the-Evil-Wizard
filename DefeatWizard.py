
#Main Menu Function:
def main_menu():
    while True:
        print("Welcome to Legend of the Wizard!") 
        print("1. New Game") 
        print("2. Quit") 
        
        choice = input("Enter your choice: ") 
        
        if choice == '1':
            return True #Start a new game 
        elif choice == '2':
            print("Exiting the game. Goodbye!") 
            return False #Quit the game 
        else:
            print("Invalid choice. Please enter 1 or 2.") 

#Character Base Class 
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  

    def attack(self, opponent):
        damage = self.attack_power
        if isinstance(opponent, Mage) and opponent.shield_active:
            if damage <= opponent.shield_strength:
                opponent.shield_strength -= damage
                print(f"{opponent.name}'s shield absorbs the damage!")
                damage = 0
            else:
                damage -= opponent.shield_strength
                opponent.shield_strength = 0
                opponent.deactivate_shield()
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    def special_ability(self, opponent):
        self.attack_power -= opponent.health 

    def heal(self):
        heal_amount = 20  # Arbitrary heal amount, adjust as needed
        self.health = min(self.max_health, self.health + heal_amount)
        print(f"{self.name} heals for {heal_amount} health. Current health: {self.health}")

#Character Subclasses: 

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=160)

    def special_ability(self, opponent):
        total_damage = self.attack_power + 66  # Arbitrary special ability damage, adjust as needed
        opponent.health -= total_damage
        print(f"\n{self.name} uses Midnight Luna on {opponent.name} causing {total_damage} damage!")

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=116,)
        self.shield_active = False
        self.shield_strength = 50  # Set the strength of the shield 

    def special_ability(self, opponent):
        inferno_blaze_damage = 145  # Set the damage for Inferno Blaze ability
        opponent.health -= inferno_blaze_damage
        print(f"\n{self.name} uses Inferno Blaze on {opponent.name} causing {inferno_blaze_damage} damage!")

    def use_shield(self):
        self.shield_active = True
        print(f"{self.name} activates their magical shield, absorbing up to {self.shield_strength} damage for one turn.")

    def deactivate_shield(self):
        self.shield_active = False
        print(f"{self.name}'s shield has been deactivated.")

class SuperSayian(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=420)

    def special_ability(self, opponent):
        damage = 600
        opponent.health -= damage
        self.health -= 42  # Decrease the player's health as a drawback
        self.attack_power -= 30  # Optionally, decrease the player's attack power as well
        print(f"\n{self.name} uses Super Blast on {opponent.name} causing {damage} damage!")
        print(f"\n{self.name} is weakened by using Super Blast: -30 health, -30 attack power.")
        print(f"\n{self.name}'s current health: {self.health}, current attack power: {self.attack_power}")

class Dwarf(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=110)

    def special_ability(self, opponent):
        damage = self.attack_power * 2  # Berserk deals double damage
        opponent.health -= damage
        print(f"\n{self.name} uses Berserk on {opponent.name} causing {damage} damage!")


#Villian Class 

class Villain:
    def __init__(self, name, health, attack_power, use_special_ability, dark_void_buff=150):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.use_special_ability = use_special_ability
        self.dark_void_buff = dark_void_buff

    def attack(self, opponent):
        damage = self.attack_power
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def special_ability(self, opponent):
        print(f"\n{self.name} uses {self.special_ability} on {opponent.name}! Health is depleted {self.health}")

    def use_dark_void_buff(self):
        self.attack_power += 20
        self.dark_void_buff -= 20
        print(f"{self.name} activates Dark Void Buff! Attack power increased to {self.attack_power}. Remaining buff: {self.dark_void_buff}")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}, Attack Power: {self.attack_power}, Special Ability: {self.special_ability}, Dark Void Buff: {self.dark_void_buff}")

    def regenerate(self):
        heal_amount = 5
        self.health += heal_amount
        print(f"{self.name} regenerates {heal_amount} health! Current health: {self.health}")

#Villian Subclass 

class EvilWizard(Villain):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=220, use_special_ability="Dark Magic", dark_void_buff=150)

    def special_ability(self, opponent):
        if self.dark_void_buff >= 150:
            damage = self.attack_power + self.dark_void_buff
            opponent.health -= damage
            print(f"{self.name} uses Dark Magic on {opponent.name} causing {damage} damage!")
        else:
            print(f"{self.name}'s Dark Magic buff is not ready yet!")
 
#Wizard Action Choice Function: 
def wizard_action_choice():
    import random
    actions = ['regenerate', 'attack', 'use_buff']
    return random.choice(actions)
 
#Create Character Function: 

def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. SuperSayian") 
    print("4. Dwarf")  

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return SuperSayian(name) 
    elif class_choice == '4':
        return Dwarf(name) 
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)


#Battle Function: 
def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. Use Shield")  # If the player is a Mage
        print("5. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            player.special_ability(wizard)
        elif choice == '3':
            player.heal()
        elif choice == '4':
            if isinstance(player, Mage):
                player.use_shield()
            else:
                print(f"{player.name} cannot use a shield.")
        elif choice == '5':
            player.display_stats()
        else:
            print("Invalid choice. Try again.")

        if wizard.health > 0:
            wizard_action = wizard_action_choice()  # Decide wizard's action
            if wizard_action == 'regenerate':
                wizard.regenerate()
            elif wizard_action == 'attack':
                wizard.attack(player)
            elif wizard_action == 'use_buff':
                wizard.use_dark_void_buff()

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            break

    if wizard.health <= 0:
        print(f"The wizard {wizard.name} has been defeated by {player.name}!")

    # Add prompt for restarting or quitting the game
    while True:
        print("\nGame Over!")
        print("1. Restart Game")
        print("2. Quit Game")
        restart_choice = input("Enter your choice: ")

        if restart_choice == '1':
            main()  # Restart the game
            break
        elif restart_choice == '2':
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")


#Main Function: 

def main():
    if main_menu():
        player = create_character()
        wizard = EvilWizard("The Dark Wizard") 
        battle(player, wizard) 
    else:
        #Quit the game 
        pass 

if __name__ == "__main__":
    main()
