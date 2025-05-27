## Lesson 2 – Inheritance: **Character → Player / Enemy**

### Lesson Overview

You’ll learn how inheritance keeps code **DRY** (Don’t Repeat Yourself) by creating an `Enemy` class that re-uses everything `Character` already knows. By the end, your game can spawn a foe with its own stats.

---

### Concept Explainer

| New Idea                          | Plain-English Why-It-Matters                                                                                                                             |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Inheritance**                   | Lets one class borrow attributes + methods from another. `Enemy` will *inherit* `name`, `level`, and `health` from `Character` so we don’t rewrite them. |
| **DRY Principle**                 | Copy-pasted code is hard to fix. Inheritance keeps shared stuff in one place—so a future change only happens once.                                       |
| **`field(default_factory=list)`** | Each enemy needs its *own* loot list, not a shared one. `default_factory` makes a fresh list every time.                                                 |

---

### Step-by-Step Instructions

1. **Create a new Git branch**

   ```bash
   git checkout -b lesson-2-enemy
   ```

2. **Edit `characters.py` – add the Enemy class**

   ```diff
   @@
    @dataclass
    class Player(Character):
        inventory: List[str] = field(default_factory=list)

   +@dataclass
   +class Enemy(Character):
   +    # Items the player can collect after defeating this foe
   +    loot: List[str] = field(default_factory=list)
   ```

3. **Update `engine.py` – import and demo an enemy**

   ```diff
   -from characters import Player
   +from characters import Player, Enemy
   @@
        hero = Player(name="Ada", level=1, health=5)
        hero.inventory.append("rusty sword")
        print(hero)
   +
   +     # Temporary: spawn a goblin to prove Enemy works
   +     goblin = Enemy(name="Goblin", level=1, health=3, loot=["gold coin"])
   +     print(goblin)
        print(hero)  # thanks to @dataclass, this is readable
   ```

4. **Run the game**

   ```bash
   python engine.py
   ```

   The terminal should show both the player and the goblin printed nicely.

5. **Commit and push**

   ```bash
   git add characters.py engine.py
   git commit -m "Lesson 2: add Enemy class via inheritance"
   git push origin lesson-2-enemy
   ```

---

### Check-Your-Work / Expected Output

```
Player(name='Ada', level=1, health=5, inventory=['rusty sword'])
Enemy(name='Goblin', level=1, health=3, loot=['gold coin'])
Player(name='Ada', level=1, health=5, inventory=['rusty sword'])
```

(Exact memory addresses may differ; the important part is that both objects print cleanly and `Enemy` shows a `loot` list.)

---

### Stretch Tasks (Optional)

* **Add another enemy**: e.g., `Orc` with `level=2`, `health=4`, `loot=["axe"]`.
* **Give each enemy a custom `__str__` method** to print cooler battle cards.
* **Refactor test prints into a quick-and-dirty `main()`** that loops over a list of enemies.

---

### Recap & What’s Next

Nice! You avoided copy-paste by letting `Enemy` inherit from `Character`, keeping your code DRY. Next lesson you’ll make these enemies *fight back* by wiring up a simple turn-based combat loop. 🚀
