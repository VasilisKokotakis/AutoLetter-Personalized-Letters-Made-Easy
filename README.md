

````markdown
# 💌 Mail Merge Magic

Ever wanted to send **personalized letters** without typing the same thing 100 times?  
This little project takes a template letter and a list of names, then magically spits out ready-to-send letters for each person. 🪄

---

## 📂 Project Structure

<pre>
```text
Mail Merge Project Start/
├── Input/
│   ├── Letters/
│   │   └── starting_letter.txt
│   └── Names/
│       └── invited_names.txt
├── Output/
│   └── ReadyToSend/
│       └── letter_for_<name>.txt
└── main.py
````

</pre>

* **`starting_letter.txt`** → your template letter. Use `[name]` wherever you want the recipient’s name to appear.
* **`invited_names.txt`** → a simple list of names (one per line).
* **`ReadyToSend/`** → where the magic happens! Personalized letters land here.

---

## 🚀 How It Works

1. Python reads your list of names ✏️
2. Finds the placeholder `[name]` in your template 📄
3. Replaces it with each real name 👤
4. Saves brand-new letters in the `ReadyToSend/` folder ✉️

---

## ▶️ Usage

1. Clone this repo or download the project
2. Put your names in:

   ```
   Mail Merge Project Start/Input/Names/invited_names.txt
   ```
3. Edit your template letter:

   ```
   Mail Merge Project Start/Input/Letters/starting_letter.txt
   ```

   Use `[name]` wherever you want the person’s name to appear.
4. Run the script:

   ```bash
   python3 main.py
   ```
5. Check the `Output/ReadyToSend/` folder for your custom letters. 🎉

---

## 💡 Example

**Template (`starting_letter.txt`):**

```
Dear [name],

You are invited to my party this Saturday!
```

**Names (`invited_names.txt`):**

```
Alice
Bob
Charlie
```

**Result:**

* `letter_for_Alice.txt`
* `letter_for_Bob.txt`
* `letter_for_Charlie.txt`

---

## 🛠️ Requirements

* Python 3.x
  (No fancy dependencies — just pure Python 🐍)

---

## 🎯 Why?

Because life’s too short to copy-paste letters.
This way, you can send out invites, reminders, or even prank notes faster than ever. 🚀

```

