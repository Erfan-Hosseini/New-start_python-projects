🗝️ Password Manager (Python CLI)

A simple command-line password manager built in Python.
It allows you to add, view, and remove password entries, which are stored locally in a text file.

📁 Project Structure
password_manager/
│
├── main.py          # Main program loop and user menu
├── utils.py         # Helper functions (add, remove, show)
└── passwords.txt    # Data file where passwords are stored

⚙️ Features

📝 Add new password entries

❌ Remove existing entries

👀 View saved usernames and passwords

💾 Data persistence (entries are saved to a file)

🧩 Modular code design using separate utils.py

🧰 Requirements

Python 3.10+ (for the match statement)

No external libraries are required.

🚀 How to Run

Clone this repository

git clone https://github.com/YOUR_USERNAME/password-manager.git
cd password-manager


Run the program

python main.py


Follow the on-screen menu

1: Add a password
2: Remove a password
3: See your passwords
4: Save and quit

💾 Data Storage

All passwords are stored in a plain text file:

passwords.txt


Each entry is saved in the format:

Source: Username | Password


⚠️ Warning: This version does not encrypt stored passwords.
Do not use real credentials — this project is for learning purposes only.

🧠 How It Works

add_password() — prompts for a username, password, and source; appends it to the list.

remove_password() — searches and removes a specific entry by keyword.

show_passwords() — prints all saved credentials.

main.py handles the menu and saves the data to passwords.txt on exit.

🔒 Planned Improvements

Add simple encryption using the cryptography module

Mask password input

Auto-save after each change

Create a GUI version with Tkinter

👨‍💻 Author

📧 erfan.hosseini2001@gmail.com
💼 (https://github.com/Erfan-Hosseini)