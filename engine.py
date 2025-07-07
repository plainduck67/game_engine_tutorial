from characters import Player

class GameEngine:
    def __init__(self):
        # Hard-code some starter data for now
        hero = Player(name="Ada", level=1, health=5)
        hero.inventory.append("rusty sword")
        print(hero)          # thanks to @dataclass, this is readable


if __name__ == "__main__":
    GameEngine()