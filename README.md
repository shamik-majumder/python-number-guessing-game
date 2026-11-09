# 🎯 Python Number Guessing Game

An interactive command-line number guessing game built in Python. This project challenges players to guess a randomly generated secret number between 1 and 100, providing helpful high/low hints and tracking the total number of attempts.

---

## 🚀 Features

* **Random Number Generation:** Utilizes Python's built-in `random` module to pick a fresh, unpredictable target number every game.
* **Input Validation:** Checks if user guesses fall outside the valid 1–100 range and prompts them accordingly.
* **Dynamic Feedback:** Guides the player with *"Higher number please"* or *"Lower number please"* hints until they find the target.
* **Attempt Tracking:** Keeps a running count of guesses and congratulates the player with their final score upon winning.
* **Beginner-Friendly Code:** Written with clear inline comments, making it an ideal reference project for learning loops, conditionals, and standard library imports.

---

## 📋 Prerequisites

Make sure you have **Python 3.x** installed on your machine. No external packages or libraries are required since this project relies entirely on Python's built-in standard library.

🎮 How to Run
Clone the repository:

Bash
git clone [https://github.com/YOUR_USERNAME/python-number-guessing-game.git](https://github.com/YOUR_USERNAME/python-number-guessing-game.git)
Navigate to the project directory:

Bash
cd python-number-guessing-game
Run the script:

Bash
python guessing_game.py

🕹️ How to Play
When you run the script, the game will prompt you to enter a number between 1 and 100.

Pay attention to the feedback:

If your guess is too low, it will say: "Higher number please."

If your guess is too high, it will say: "Lower number please."

If you enter a number outside 1–100, it will warn you with an invalid choice message without penalizing your guess count.

Keep guessing until you hit the correct number and check out how many attempts it took you!

📜 License
This project is open source and available under the MIT License.
