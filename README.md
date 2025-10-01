
# 💌 Mail Merge Magic

Tired of typing the same letter over and over?
This project takes a **template letter** + a **list of names** and automatically creates personalized letters for everyone. 🪄

---

## 📂 Project Structure

```
Mail Merge Project Start/
├── Input/
│   ├── Letters/
│   │   └── starting_letter.txt      # Your template
│   └── Names/
│       └── invited_names.txt        # List of names
├── Output/
│   └── ReadyToSend/                 # Personalized letters land here
│       └── letter_for_<name>.txt
└── main.py                          # The script that does the magic
```

* **`starting_letter.txt`** → Your template. Use `[name]` wherever the person’s name should go.
* **`invited_names.txt`** → A list of names (one per line).
* **`ReadyToSend/`** → All generated letters will appear here.

---

## 🚀 How It Works

1. Read the names list ✏️
2. Find the `[name]` placeholder in the template 📄
3. Replace it with each real name 👤
4. Save each personalized letter into `ReadyToSend/` ✉️

---

## ▶️ Usage

1. Clone this repo or download the project.
2. Add your names to:

   ```
   Input/Names/invited_names.txt
   ```
3. Customize your letter in:

   ```
   Input/Letters/starting_letter.txt
   ```

   👉 Use `[name]` wherever you want the recipient’s name to appear.
4. Run the script:

   ```bash
   python3 main.py
   ```
5. Open `Output/ReadyToSend/` and collect your letters. 🎉

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

**Generated Files:**

* `letter_for_Alice.txt`
* `letter_for_Bob.txt`
* `letter_for_Charlie.txt`

---

## 🛠️ Requirements

* Python 3.x
* No extra libraries — pure Python 🐍

---

## 🎯 Why Use This?

Because life’s too short to copy-paste letters.
With Mail Merge Magic, you can:

* Send invitations ✉️
* Share reminders 📢
* Even automate fun messages 🤭

All with one simple script. 🚀
