# combat.py  – stub version
from characters import Player, Enemy

def fight(player: Player, enemy: Enemy) -> bool:
    """
    Temporary combat: the player always wins.
    Returns True for victory so the story can continue.
    """
    print(f"\n⚔️  You face {enemy.name}…")
    print("…but the battle is strangely easy. You win!")
    return True
