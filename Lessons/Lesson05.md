## Lesson 5 – SceneRepository: Data-Driven Thinking

### Lesson Overview

You’ll move the story data-load out of `engine.py` and into a reusable **SceneRepository** class that caches JSON files. Then you’ll update the engine so the player can jump between scenes using a two-element tuple like `["village", "start"]`.

---

### Concept Explainer

| New Idea                    | Why It Matters                                                                                   |
| --------------------------- | ------------------------------------------------------------------------------------------------ |
| **Repository pattern**      | Puts all “how do I fetch data?” logic in one place so the rest of the game just asks for turns.  |
| **Caching**                 | Loading a file once then re-using it is faster and keeps your code DRY.                          |
| **Scene / turn addressing** | Represent “where am I?” with `(scene_id, turn_id)` so you can hop to completely different files. |

---

### Step-by-Step Instructions

1. **Create `scenes.py`**
   In the project root:

   ```py
   # scenes.py
   import json, pathlib
   from typing import Dict, Any

   DATA_DIR = pathlib.Path(__file__).parent / "data"

   class SceneRepository:
       """Loads scene JSON on demand and caches it."""
       def __init__(self):
           self._cache: Dict[str, Dict[str, Any]] = {}

       def get_turn(self, scene: str, turn: str) -> Dict[str, Any]:
           if scene not in self._cache:
               file_path = DATA_DIR / f"{scene}.json"
               print(f"[DEBUG] loading {file_path.name}")
               with open(file_path, encoding="utf-8") as f:
                   self._cache[scene] = json.load(f)["turns"]
           return self._cache[scene][turn]
   ```

2. **Upgrade `engine.py` to use the repository**
   Open `engine.py` and replace the *Lesson 4* block with:

   ```py
   # ─── Lesson 5: repository-driven story ───
   from scenes import SceneRepository

   self.repo = SceneRepository()
   current_scene, current_turn = "intro", "start"

   print("\nStory begins:")
   while current_turn:
       turn = self.repo.get_turn(current_scene, current_turn)
       print(turn["prompt"])
       input("\nPress Enter to continue...\n")
       current_scene, current_turn = turn.get("next", (None, None))
   # ─── end Lesson 5 block ───
   ```

   *Delete the old `data_path`, `json.load`, and `turns` code.*

3. **Prove caching works**
   Run `python engine.py`. You should see `[DEBUG] loading intro.json` only **once** even though you loop through several turns.

4. **Add a second scene to demonstrate switching**

   1. **Create `data/village.json`:**

      ```json
      {
        "scene": "village",
        "turns": {
          "start": {
            "prompt": "You arrive at a sleepy village. A cat stares suspiciously.",
            "next": [null, null]
          }
        }
      }
      ```
   2. **Edit `data/intro.json`** – in the `after_wolf` turn change its choice:

      ```json
      "c": { "label": "Continue onward", "next": ["village", "start"] }
      ```
   3. **Re-run** the game and choose the path that defeats the wolf → press **c**.
      You should see `[DEBUG] loading village.json` the first time you enter.

5. **Commit your work**

   ```bash
   git add scenes.py engine.py data/village.json data/intro.json
   git commit -m "Lesson 5: add SceneRepository and scene switching"
   git push origin main
   ```

---

### Check-Your-Work / Expected Output

```
Ada(level=1, health=5, inventory=['rusty sword'])
Goblin(level=1, health=3, loot=['gold coin'])

[DEBUG] loading intro.json

Story begins:
You wake up in a dark forest. A narrow path splits.

Press Enter to continue...

...   # (player progresses)

[DEBUG] loading village.json
You arrive at a sleepy village. A cat stares suspiciously.
```

*(Notice each `[DEBUG] loading …` line appears only once per file.)*

---

### Stretch Tasks (Optional)

* 💾  Add a tiny `data/cave.json` and let the pond route lead there.
* 🔄  Print the player’s current scene and turn each loop for easy debugging.
* 🚫  Raise a custom `SceneNotFoundError` if `get_turn` can’t locate a file or key.

---

### Recap & What’s Next

Nice work! Your engine now pulls story content from **any** JSON scene file exactly when it’s needed, keeping memory low and code tidy. Up next you’ll add **choices** so the player can decide actions instead of just pressing Enter, bringing real interactivity to your adventure.
