from domain.character import Character
from domain.classes import Warrior, Mage,Cleric




if __name__=="__main__":
    print("QuestForge booting... (Level 0 skeleton)")

    hero = Character("Aria", 100, 15)
    goblin = Character("Goblin", 35, 5)
    spiderman = Character("Spider-Man", 80, 10)
    superman = Character("Superman", 150, 20)


    warrior = Warrior("Bram")
    mage = Mage("Sylla")
    sage = Cleric("Eldrin")


    mage.special_ability(goblin)
    print(f"Bram HP: {warrior.health}, Sylla HP: {mage.health}")
    sage.special_ability(goblin)
    print(f"Goblin HP: {goblin.health}, Eldrin HP: {sage.health}")