## Lesson 7 – Basic Combat Stub

### Lesson Overview

You’ll add a **placeholder combat system** so the player can “fight” an enemy and always win. This lays the groundwork for real turn-based battles later.

---

### Concept Explainer

| New Idea            | Friendly Description                                                                                      |
| ------------------- | --------------------------------------------------------------------------------------------------------- |
| **Stub Function**   | A quick, fake version of a real function that lets you wire pieces together before the hard logic exists. |
| **Separate Module** | Putting combat code in its own `combat.py` keeps the project tidy and makes future upgrades easier.       |
| **Engine Hook-up**  | Calling the stub from `engine.py` shows how different modules talk to each other.                         |

---

### Step-by-Step Instructions

1. **Create the combat module**
   In your project root, add a new file **`combat.py`**:

   ```py
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
   ```

2. **Wire the stub into the game engine**
   Open **`engine.py`** and import the new module at the top:

   ```diff
   -from characters import Player, Enemy
   +from characters import Player, Enemy
   +from combat import fight        # NEW
   ```

   Locate the spot where an enemy fight should occur (inside the game-loop after a player picks a choice). Replace the TODO or placeholder with a real call:

   ```diff
   if "enemy" in turn and choice_key == "f":
       enemy = Enemy(**turn["enemy"])
   -    # TODO: call combat function here
   +    if not fight(self.player, enemy):
   +        print("Game over.")   # In stub, this never runs
   +        break
   ```

3. **Add an “enemy block” to a scene**
   Open **`data/intro.json`** (or any active scene). Inside a turn node that should present combat, add an `enemy` key like this (keep existing keys):

   ```jsonc
   "wolf": {
     "prompt": "A hungry wolf snarls at you!",
     "enemy": { "name": "Wolf", "level": 1, "health": 2, "loot": [] },
     "choices": {
       "f": { "label": "Fight", "next": ["intro", "after_wolf"] },
       "x": { "label": "Flee back", "next": ["intro", "start"] }
     }
   }
   ```

4. **Run the game**

   ```bash
   python engine.py
   ```

   Choose the path that triggers the fight (`f`). You should see the stub messages and then continue the story.

5. **Commit & Push**

   ```bash
   git add combat.py engine.py data/intro.json
   git commit -m "Lesson 7: add combat stub and enemy wiring"
   git push
   ```

---

### Check-Your-Work / Expected Output

```
Your name, hero? Alex

=== STATUS ===
Health: 5   Level: 1   Inventory: Empty
================

You wake up in a dark forest. A narrow path splits.
[l] Go left
[r] Go right
> l

⚔️  You face Wolf…
…but the battle is strangely easy. You win!

The path is clear. The gem sparkles in your pack.
[c] Continue onward
>
```

*The wolf fight always reports victory, and the game continues without crashing.*

---

### Stretch Tasks (Optional)

* **Flavor Text:** Randomize the victory message for different enemies.
* **Lose Condition Stub:** Add a debug flag that makes `fight` sometimes return `False` to test the “Game over” branch.
* **Loot Drop:** Update the stub to append any `enemy.loot` items to `player.inventory`.

---

### Recap & What’s Next

Nice work! You created a separate **combat module**, integrated it with the engine, and proved the flow works with an always-win stub. In the upcoming lesson you’ll replace this stub with real turn-based logic and let the wolf actually bite back!
