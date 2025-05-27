## Lesson 6 – Choices & Branching

### Lesson Overview

Time to make the story react to the player!
In this lesson you’ll replace the “Press Enter to continue” rail-track with a real menu, read the player’s answer, validate it, and jump to the correct next turn.

---

### Concept Explainer

| New Idea                 | Kid-sized Explanation                                                                                       |
| ------------------------ | ----------------------------------------------------------------------------------------------------------- |
| **`choices` dictionary** | Each turn will now list all the buttons the player can press ( `"l"`, `"r"` …) and where each button leads. |
| **Input validation**     | We keep asking until the player types one of the allowed keys. No sneaking in wrong letters!                |
| **Branching flow**       | Because different keys point to different `(scene, turn)` pairs, the story can finally split and loop.      |

---

### Step-by-Step Instructions

> **Open VS Code in your cloned repo and start a new branch:**
> `git checkout -b lesson-06-choices`

1. **Edit `data/intro.json` – turn the linear story into a menu**
   Replace the file contents with:

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
       },

       "wolf": {
         "prompt": "A hungry wolf snarls at you! (Nothing you can do yet…)",
         "next": ["intro", "start"]
       },

       "pond": {
         "prompt": "You find a quiet pond and feel refreshed.",
         "next": ["intro", "start"]
       }
     }
   }
   ```

   *Save* the file.

2. **Update `engine.py` – show the menu & branch**
   Find the **`while current_turn:`** loop and replace it with the diff below.

   ```diff
    while current_turn:
        turn = self.repo.get_turn(current_scene, current_turn)
   ```

* ```
    print(turn["prompt"])
  ```
* ```
    input("\nPress Enter to continue...\n")
  ```
* ```
    current_scene, current_turn = turn.get("next", (None, None))
  ```

- ```
    print("\n" + turn["prompt"])
  ```
-
- ```
    # ─── NEW: menu & branching ───
  ```
- ```
    if "choices" in turn:                 # interactive turn
  ```
- ```
        for key, choice in turn["choices"].items():
  ```
- ```
            print(f"[{key}] {choice['label']}")
  ```
-
- ```
        choice_key = input("> ").strip().lower()
  ```
- ```
        while choice_key not in turn["choices"]:
  ```
- ```
            print("Please pick one of the listed options.")
  ```
- ```
            choice_key = input("> ").strip().lower()
  ```
-
- ```
        current_scene, current_turn = turn["choices"][choice_key]["next"]
  ```
- ```
    else:                                 # non-interactive (old style)
  ```
- ```
        input("\nPress Enter to continue...\n")
  ```
- ```
        current_scene, current_turn = turn.get("next", (None, None))
  ```

  ```
  ```

3. **Run the game**
   In the terminal:

   ```bash
   python engine.py
   ```

   Try both `l` and `r` to prove the fork works, and see that wrong keys gently re-prompt.

4. **Stage & commit**

   ```bash
   git add data/intro.json engine.py
   git commit -m "Lesson 6: add choices menu and branching"
   git push origin lesson-06-choices
   ```

---

### Check-Your-Work / Expected Output

```text
[DEBUG] loading intro.json
You wake up in a dark forest. A narrow path splits.
[l] Go left
[r] Go right
> q
Please pick one of the listed options.
> r

You find a quiet pond and feel refreshed.

Press Enter to continue...
```

Picking `l` instead of `r` should print the wolf prompt, then loop back to the fork.

---

### Stretch Tasks (Optional)

* Add a `"b"` (back) option to the `pond` turn that returns straight to the wolf.
* Give the wolf turn its own `choices` menu (maybe **fight** vs **run**) even though combat isn’t coded yet.
* Let the player type **full words** (`"left"` / `"right"`) in addition to single letters—hint: store a list of aliases in each choice.

---

### Recap & What’s Next

Nice! Your game now *asks* and *listens*. Players can explore different paths, making the forest feel alive. In the next lesson you’ll bring danger to those paths by wiring up a super-simple combat loop—so sharpen that rusty sword!
