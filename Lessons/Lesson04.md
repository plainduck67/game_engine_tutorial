a## Lesson 4 – Turn Manager v0: Linear Story

### Lesson Overview

Today you’ll turn last lesson’s single‐prompt demo into a **mini text-adventure loop**.
After the lesson your game will:

* keep showing the current turn’s text
* wait for the player to press **Enter**
* jump to the next hard-coded turn until the story ends

---

### Concept Explainer

| Concept             | Kid-sized Description                                                                                                           |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `while` loop        | Repeats code while a condition is *True*. Great for “keep the game running”.                                                    |
| *Sentinel* variable | A variable that holds “where we are”. We update it each lap through the loop.                                                   |
| `input()` pause     | `input()` stops the program and waits for the user. Even if you ignore what they type, it’s a handy “Press Enter to continue…”. |
| JSON lookup         | Your `scene_data["turns"][turn_id]` grabs the right chunk of story text each time.                                              |

---

### Step-by-Step Instructions

1. **Add a `next` key to every turn in `data/intro.json`**
   This creates a single-path story.

   ```jsonc
   "start": {
       "prompt": "You wake up in a dark forest. A narrow path splits.",
       "next": "wolf"
   },
   "wolf": {
       "prompt": "A hungry wolf snarls at you!",
       "next": "pond"
   },
   "pond": {
       "prompt": "You find a quiet pond and feel refreshed.",
       "next": null          // null marks “the end”
   }
   ```

2. **Open `engine.py` and locate the Lesson 3 block.**
   Replace everything from `# ───── Lesson 3 code starts here ─────`
   down to `# ───── Lesson 3 code ends here ─────` with the code below.

   ```python
   # ───── Lesson 4 code starts here ─────
   data_path = pathlib.Path(__file__).parent / "data" / "intro.json"
   with open(data_path, encoding="utf-8") as f:
       scene_data = json.load(f)

   turns = scene_data["turns"]
   current_turn = "start"

   print("\nStory begins:")
   while current_turn:                       # stop when we hit None
       turn = turns[current_turn]
       print(turn["prompt"])

       input("\nPress Enter to continue...\n")  # tiny pause

       current_turn = turn.get("next")       # move to the next id
   # ───── Lesson 4 code ends here ─────
   ```

3. **Run the game** (`python engine.py`).
   Watch it walk through **start → wolf → pond** and then exit.

4. **Commit & push**

   ```bash
   git add engine.py data/intro.json
   git commit -m "Lesson 4: basic turn manager loop"
   git push
   ```

---

### Check-Your-Work / Expected Output

```text
Player(name='Ada', level=1, health=5, inventory=['rusty sword'])
Enemy(name='Goblin', level=1, health=3, loot=['gold coin'])

Story begins:
You wake up in a dark forest. A narrow path splits.

Press Enter to continue...

A hungry wolf snarls at you!

Press Enter to continue...

You find a quiet pond and feel refreshed.

Press Enter to continue...

```

*(Program ends – back at the command prompt.)*

---

### Stretch Tasks (Optional)

* Add a `"title"` key at the top of the JSON and print it once at game start.
* Allow the player to type **q** at any time to quit the loop early.
* Give each turn a `"delay": 2` value and experiment with `time.sleep()` for dramatic pauses.

---

### Recap & What’s Next

Great job! You now have a *turn manager* that drives the story forward one scene at a time. Next lesson we’ll replace the hard-wired `next` with **branching choices**, so the player’s input decides where the adventure goes.
