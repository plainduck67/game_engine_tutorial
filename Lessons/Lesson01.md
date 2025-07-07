## Lesson 1 – Dataclasses 101: Building **Player**

---

### Lesson Overview

You’ll create your very first **dataclass** — a `Player` object that will eventually explore our text-adventure world. Along the way you’ll learn what the `@dataclass` decorator does, why some fields should stay mutable, and how to print your shiny new hero to the terminal.

---

### Concept Explainer

| New Idea                          | Quick Take                                                                                                                                                                                       |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **`@dataclass`**                  | A Python decorator that writes common class boilerplate (like `__init__`, `__repr__`, `__eq__`) for you.                                                                                         |
| **Immutable vs. Mutable Fields**  | Numbers/strings are *immutable* (can’t change in place). Lists/dicts are *mutable* (can change). Dataclasses need special handling for *mutable* defaults so every instance gets its *own* list. |
| **`field(default_factory=list)`** | The safe way to give every `Player` a fresh empty inventory list.                                                                                                                                |

---

### Step-by-Step Instructions

1. **Create a new file `characters.py` in the project root.**
   Add the following code:

   ```python
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
   ```

2. **Update `engine.py` to use `Player`.**
   Replace its contents with the small test harness below (we’ll rebuild the engine later):

   ```python
   from characters import Player

   class GameEngine:
       def __init__(self):
           # Hard-code some starter data for now
           hero = Player(name="Ada", level=1, health=5)
           print(hero)          # thanks to @dataclass, this is readable


   if __name__ == "__main__":
       GameEngine()
   ```

3. **Run the program** (`python engine.py`) and watch the pretty print-out of your dataclass object.

4. **Experiment with mutability.**
   Inside `engine.py`, right after you create `hero`, add:

   ```python
   hero.inventory.append("rusty sword")
   print(hero)
   ```

   Run again. Notice how the inventory list changes in place without recreating the whole object.

5. **Save ➜ Commit ➜ Push.**

   ```bash
   git add characters.py engine.py
   git commit -m "Lesson 1: add Player dataclass"
   git push
   ```

---

### Check-Your-Work / Expected Output

```text
Player(name='Ada', level=1, health=5, inventory=[])
Player(name='Ada', level=1, health=5, inventory=['rusty sword'])
```

---

### Stretch Tasks (Optional)

* Make two players in the same file and prove their inventories don’t overlap.
* Try setting `inventory: tuple = ()` and observe what changes.
* Add a `__post_init__` method that prints “Ready for adventure!” when a `Player` is created.

---

### Recap & What’s Next

Great job! You used `@dataclass` to slash boilerplate and learned why `field(default_factory=list)` keeps each player’s gear separate. In the next lesson you’ll expand the `characters.py` module with an `Enemy` class and wire up basic combat