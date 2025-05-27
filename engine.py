# engine.py
from characters import Player, Enemy
from combat import fight        # NEW
from scenes import SceneRepository

class GameEngine:
    def __init__(self):
       # Hard-code some starter data for now
        self.player = Player(name="Ada", level=1, health=5)
        self.player.inventory.append("rusty sword")
        print(self.player)  # thanks to @dataclass, this is readable

        # Temporary: spawn a goblin to prove Enemy works
        goblin = Enemy(name="Goblin", level=1, health=3, loot=["gold coin"])
        print(goblin)
        # ─── Lesson 5: repository-driven story ───
        self.repo = SceneRepository()
        current_scene, current_turn = "intro", "start"

        print("\nStory begins:")
        while current_turn:
            turn = self.repo.get_turn(current_scene, current_turn)
            # Show prompt
            print("\n" + turn["prompt"])

            # ─── NEW: menu & branching ───
            if "choices" in turn:                 # interactive turn
                for key, choice in turn["choices"].items():
                    print(f"[{key}] {choice['label']}")
                choice_key = input("> ").strip().lower()
                while choice_key not in turn["choices"]:
                    print("Please pick one of the listed options.")
                    choice_key = input("> ").strip().lower()
                # Combat stub: fight enemy if present and 'f' selected
                if "enemy" in turn and choice_key == "f":
                    enemy = Enemy(**turn["enemy"])
                    if not fight(self.player, enemy):
                        print("Game over.")   # stub always wins
                        break
                current_scene, current_turn = turn["choices"][choice_key]["next"]
            else:                                 # non-interactive (old style)
                input("\nPress Enter to continue...\n")
                current_scene, current_turn = turn.get("next", (None, None))
        # ─── end Lesson 5 block ───

if __name__ == "__main__":
    GameEngine()