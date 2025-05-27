# characters.py
from dataclasses import dataclass, field
from typing import List

@dataclass
class Character:
    name: str
    level: int
    health: int

@dataclass
class Player(Character):
    # Use default_factory so each player gets a new list
    inventory: List[str] = field(default_factory=list)

@dataclass
class Enemy(Character):
    # Items the player can collect after defeating this foe
    loot: List[str] = field(default_factory=list)