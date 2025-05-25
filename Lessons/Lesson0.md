## Lesson 0 – Project Setup & “Hello, Python”

### Lesson Overview

Today you’ll create a brand-new GitHub repo, clone it into VS Code, add your very first Python file, and see “hello world” appear in the terminal. This sets the foundation for the multi-file adventure game you’ll build over the next lessons.

---

### Concept Explainer

| New Idea              | Why It Matters                                                                         |
| --------------------- | -------------------------------------------------------------------------------------- |
| **Repository (repo)** | A cloud folder on GitHub that stores every version of your code.                       |
| **Clone**             | Copies the repo to your computer so you can edit files locally.                        |
| **`__init__` method** | Runs automatically when you make an object; today it will simply print a message.      |
| **Commit & Push**     | Save a snapshot of your work and send it back up to GitHub so it’s safe and shareable. |

---

### Step-by-Step Instructions

1. **Create the GitHub repo**

   1. Sign in at [github.com](https://github.com).
   2. Click **➕ New repository** → name it `text-adventure`.
   3. Leave it **Public**, **Add a README** ✔️, then **Create repository**.

2. **Clone into VS Code**

   1. Copy the repo’s **HTTPS** URL (green **Code** button).
   2. In VS Code, press **⌘⇧P / Ctrl Shift P** → “Git: Clone” → paste the URL.
   3. Pick a local folder; VS Code will offer to open it—accept.

3. **Add your first Python file**

   1. In the Explorer sidebar, click **New File** → `engine.py`.
   2. Type the starter code:

      ```python
      # engine.py
      class GameEngine:
          def __init__(self):
              print("hello world")

      if __name__ == "__main__":
          GameEngine()
      ```
   3. Press **⌘S / Ctrl S** to save.

4. **Run the program**

   1. Open a terminal in VS Code (**Terminal → New Terminal**).
   2. Run:

      ```bash
      python engine.py
      ```
   3. You should see `hello world`.

5. **Commit & Push**

   1. In the Source Control tab (left sidebar), click **+** next to `engine.py`.
   2. In the message box, type `Add engine.py with hello world` → press **✓ Commit**.
   3. Click **…** menu → **Push** (or the cloud-arrow icon).
   4. Refresh GitHub in your browser—`engine.py` should now be there.

---

### Check-Your-Work / Expected Output

```text
$ python engine.py
hello world
```

GitHub repo shows one commit with `engine.py`.

---

### Stretch Tasks (Optional)

* Change the message to `"Hello, <your-name>!"` and push the update.
* Create a `README.md` section titled **“Project Journal”** and jot one sentence about what you learned today.
* Explore the **Source Control** panel: view commit history and diff your change.

---

### Recap & What’s Next

Great job! You set up the entire workflow—GitHub ➜ VS Code ➜ Python ➜ Commit—in one session. Next lesson you’ll turn this tiny engine into something interactive, reading player input and printing simple story text. Keep your repo handy; every lesson will build on today’s work.
