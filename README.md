# Bulls-and-Cows-game-using-python

## Description
The **Bulls and Cows** game is a number-guessing logic game built using **Python** and **Tkinter**. The goal of the game is to guess a randomly generated **4-digit number** where all digits are unique. After each guess, the player receives feedback in the form of **Bulls** and **Cows**:  
- **Bulls**: Number of digits that are correct and in the correct position.  
- **Cows**: Number of digits that are correct but in the wrong position.  

The player continues guessing until they get **4 Bulls**, meaning they have correctly guessed the number. The game then displays a success message and resets with a new randomly generated number.  

The program ensures that the player enters a valid **4-digit number** with **no repeated digits**. If an invalid input is detected (e.g., non-numeric characters, duplicate digits, or incorrect length), an error message is displayed. The interface consists of a simple text entry field, a submit button, and a result display.  

This implementation demonstrates **event-driven programming** using Tkinter. It handles user input, processes game logic, and updates the UI accordingly. The game runs entirely in a **GUI window** and does not require a command-line interface.  

## How It Works
- A **random 4-digit number** is generated at the start, ensuring all digits are unique.  
- The player enters a **4-digit guess** and clicks the **Submit** button.  
- The program checks the guess and provides feedback:  
  - A **Bull** is awarded for each correctly placed digit.  
  - A **Cow** is awarded for each correct digit in the wrong position.  
- The feedback is displayed on the screen.  
- The game continues until the player gets **4 Bulls**.  
- When the player wins, a success message is shown, and the game resets.  

## Code Overview
The code consists of two main classes:  

### **Packages Used**
- **tkinter**: Used to create the graphical interface.  
- **random**: Used to generate the secret number.  

### **Key Components**
- **Game Class (`Game`)**:  
  - `gen_code()`: Generates a random 4-digit number with unique digits.  
  - `eval_guess(guess)`: Checks how many Bulls and Cows the guess contains.  
  - `reset()`: Resets the game by generating a new random number.  

- **App Class (`App`)**:  
  - Manages the **Tkinter GUI**.  
  - Includes an **Entry** widget for user input.  
  - Displays feedback using a **Label**.  
  - Contains a **Button** to submit the guess.  
  - Implements `check_guess()`, which processes the player's input and updates the result.  

- **Game Logic**:  
  - Uses `random.sample()` to generate a **random** 4-digit number with **unique digits**.  
  - Ensures the player’s guess is exactly **4 digits long** and **contains no duplicate digits**.  
  - Provides feedback in terms of **Bulls and Cows**.  
  - Displays error messages if the input is invalid.  

## Installation & Running
1. Ensure **Python** is installed on your system.  
2. Run the following command in your terminal or command prompt:  

   ```sh
   python main.py
   ```

## Screenshots
Starting window:<br>
![image](https://github.com/user-attachments/assets/07b34671-f161-41fe-83a1-10b7dc92869a) <br><br>
After getting 4 bulls:<br>
![image](https://github.com/user-attachments/assets/e2d7b94b-c163-42b4-b1a0-06fbb22f13be)
