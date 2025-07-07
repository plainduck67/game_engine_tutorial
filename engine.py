from characters import Player, Enemy, NPC

class GameEngine:
    def __init__(self):
        # Hard-code some starter data for now
        hero = Player(name="Ada", level=1, health=5)
        hero.inventory.append("rusty sword")
        goblin = Enemy(name = "Goblin", level = 1, health = 3)
        goblin.loot.append("gold coin")
        print(hero)          # thanks to @dataclass, this is readable
        print(goblin)

if __name__ == "__main__":
    GameEngine()