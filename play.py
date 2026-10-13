from domain.character import Character
from domain.classes import Warrior, Mage,Cleric, Rogue
from domain.battle import run_special_round, total_party_damage



if __name__=="__main__":
    print("QuestForge booting... (Level 0 skeleton)")

    hero = Character("Aria", 100, 15)
    goblin = Character("Goblin", 35, 5)
    spiderman = Character("Spider-Man", 80, 10)
    superman = Character("Superman", 150, 20)


    warrior = Warrior("Bram")
    mage = Mage("Sylla")
    rogue = Rogue("Kade")
    sage = Cleric("Eldrin")


    party = [Warrior("Bram"), Mage("Sylla"), Rogue("Kade"), Cleric("Eldrin")]
    dummy = Warrior("Training Dummy")

    total_party_damage(party, dummy)
    print(f"Dummy HP: {dummy.health}\n")