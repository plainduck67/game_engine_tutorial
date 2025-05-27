## Lesson 3 – Reading Your First JSON File

### Lesson Overview

You’ll teach the game to read its very first scene file (`intro.json`) and print the opening prompt on-screen. This shows how games load content from data files instead of hard-coding everything.

---

### Concept Explainer

| New Idea            | Kid-friendly What & Why                                                                                 |
| ------------------- | ------------------------------------------------------------------------------------------------------- |
| **`json` module**   | A built-in tool that turns a text file full of `{ }` and `[` ]\` into Python dictionaries and lists.    |
| **Pathlib**         | Lets you build file paths (`/folder/file.txt`) that work on Windows, Mac, or Linux.                     |
| **Nested look-ups** | Accessing `scene["turns"]["start"]["prompt"]` digs three levels deep to find exactly the line you want. |

---

### Step-by-Step Instructions

1. **Create the data folder and scene file**
   *In VS Code explorer:*

   * Right-click the project root → **New Folder** → name it **`data`**.
   * Inside **`data`** create **`intro.json`** and paste:

     ```json
     {
       "scene": "intro",
       "turns": {
         "start": {
           "prompt": "You wake up in a dark forest. A narrow path splits.",
           "choices": {
             "l": { "label": "Go left",  "next": ["intro", "wolf"] },
             "r": { "label": "Go right", "next": ["intro", "pond"] }
           }
         }
       }
     }
     ```

2. **Import the helpers**
   Open **`engine.py`** and add these imports right under the existing ones:

   ```diff
    from characters import Player, Enemy
   +import json
   +import pathlib
   ```

3. **Point Python at the JSON file** – still in **`engine.py`**, inside `GameEngine.__init__` (just under the goblin printout is fine), paste:

   ```diff
        print(goblin)
   ```

* ```
    # ───── Lesson 3 code starts here ─────
  ```
* ```
    data_path = pathlib.Path(__file__).parent / "data" / "intro.json"
  ```
* ```
    with open(data_path, encoding="utf-8") as f:
  ```
* ```
        scene_data = json.load(f)
  ```
*
* ```
    first_turn = scene_data["turns"]["start"]
  ```
* ```
    print("\nStory begins:")
  ```
* ```
    print(first_turn["prompt"])
  ```
* ```
    # ───── Lesson 3 code ends here ─────
  ```

  ```
  ```

4. **Run it!**
   In the VS Code terminal:

   ```bash
   python engine.py
   ```

5. **Commit your progress**

   ```bash
   git add .
   git commit -m "Lesson 3: load intro.json and print starting prompt"
   git push
   ```

---

### Check-Your-Work / Expected Output

```text
Player(name='Ada', level=1, health=5, inventory=['rusty sword'])
Enemy(name='Goblin', level=1, health=3, loot=['gold coin'])
Player(name='Ada', level=1, health=5, inventory=['rusty sword'])

Story begins:
You wake up in a dark forest. A narrow path splits.
```

(The exact order of the first three lines may vary—no worries.)

---

### Stretch Tasks (Optional)

* **Print the two choice labels** (`Go left`, `Go right`) under the prompt.
* Add a safety check: if `intro.json` is missing, print a friendly error instead of crashing.
* Experiment: change the prompt text in the JSON file and re-run to see instant story edits.

---

### Recap & What’s Next

Awesome—your game just read a file all by itself! Today you met the `json` module, pathlib, and nested dictionary look-ups. Next time you’ll organise this loading code into a neat `SceneRepository` class and let the player actually choose **left** or **right**.
