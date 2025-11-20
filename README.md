# python-mini-projects

<p>
A collection of small Python projects built to strengthen programming logic and problem-solving skills.  
Currently includes:
<ul>
  <li>Password Generator</li>
  <li>Hangman</li>
  <li>Rock-Paper-Scissor</li>
  <li>Guess the Number</li>
  <li>Basic Calculator</li>
  <li>Mad Libs</li>
  <li>Email Slicer</li>
  <li>Word Replacer</li>
</ul>
</p>

<hr>

<h1>About</h1>
<p>
This repository is part of my foundational learning in <b>Python programming</b>, supporting my journey as an <b>IT Engineering student</b> focused on <b>Defensive Security</b> and <b>Full Stack Development</b>.<br>
Each mini project is designed to reinforce basic programming concepts like variables, conditionals, loops, and input handling.
</p>

<hr>

<h1>Projects</h1>

<h3>Password Generator</h3>
<p>
A customizable command-line password generator that creates secure passwords based on user-selected criteria. 
The program allows the user to choose the length of the password and specify whether to include numbers, 
lowercase letters, uppercase letters, and special symbols. It validates all inputs, constructs an allowed 
character set, and generates a random password of the desired length.
</p>

<b>Concepts used:</b>
<ul>
  <li>User input validation for security and correctness</li>
  <li>String module for character sets (digits, letters, punctuation)</li>
  <li>Random module for generating unpredictable passwords</li>
  <li>Conditional logic for building a customizable character pool</li>
  <li>Looping and string manipulation for assembling the final password</li>
</ul>

<p>Example Output</p>
<img width="500" alt="image" src="https://github.com/user-attachments/assets/91c41e45-01b5-4e56-9634-a553b654c542" />

<h2>Hangman</h2>
<p>
A console-based Hangman game where the computer selects a random word from a predefined list, 
and the player attempts to guess it one letter at a time. The program tracks correct guesses, 
incorrect guesses, and previously attempted letters. The game continues until the player either 
completes the word or exits manually.
</p>

<b>Concepts used:</b>
<ul>
  <li>Random module for selecting a hidden word</li>
  <li>List manipulation to track revealed and unrevealed letters</li>
  <li>Sets for storing previously guessed characters</li>
  <li>Loop control for repeated guessing</li>
  <li>Conditional branching for correct and incorrect guesses</li>
  <li>String and input handling for player interaction</li>
</ul>

<p>Example Output</p>
<img width="500" alt="image" src="https://github.com/user-attachments/assets/1ede3592-f181-4ace-a789-610bd9532978" />
<img width="500" alt="image" src="https://github.com/user-attachments/assets/f0531053-fcee-486d-bb9e-dd5df2822cf5" />

<h2>Rock-Paper-Scissor</h2>
<p>
A command-line version of the classic Rock-Paper-Scissor game where the user competes against the computer. 
The program randomly selects its choice and compares it with the user's input to determine the winner. 
It continues running until the user decides to exit.
</p>

<b>Concepts used:</b>
<ul>
  <li>Random module for generating computer choices</li>
  <li>Conditional logic for win/loss evaluation</li>
  <li>Loop control and user input handling</li>
  <li>Program termination using exit conditions</li>
</ul>
<p>Example Output</p>
<img width="500" alt="image" src="https://github.com/user-attachments/assets/e031a516-8b15-4912-b42d-4739604fa1b9" />

<h2>Guess the Number</h2>
<p>Includes two variations:</p>
<ul>
  <li><b>User Guess:</b> The user tries to guess a number randomly chosen by the computer.</li>
  <li><b>Computer Guess:</b> The computer attempts to guess the number the user is thinking of.</li>
</ul>

<b>Concepts used:</b>
<ul>
  <li>Loops</li>
  <li>Conditional statements</li>
  <li>Random number generation</li>
  <li>Logic design</li>
</ul>

<p>Example Output</p>
<h4>User tries to guess the number:</h4>
<img width="500" alt="image" src="https://github.com/user-attachments/assets/0292f445-ec32-4e38-8446-514e657f95ea" />
<h4>Computer tries to guess the number:</h4>
<img width="500" alt="image" src="https://github.com/user-attachments/assets/b25128f5-169d-4a8d-bef3-c4e86e88593c" />

<h2>Basic Calculator</h2>
<p> A simple, command-line calculator that performs basic arithmetic operations (addition, subtraction, multiplication, and division) on two user-provided numbers.
  It includes basic input validation to handle non-numeric input and invalid operation choices. </p>

<b>Concepts used:</b>
<ul>     
  <li>Functions for modularizing arithmetic operations</li>     
  <li>Loop control (<code>while True</code>) for continuous operation</li>     
  <li>Conditional branching (<code>if/elif/else</code>) to execute the chosen operation</li>     
  <li>Error handling (<code>try...except ValueError</code>) for invalid number input</li>     
  <li>Input handling (<code>input()</code>) for numbers and operation choice</li>     
</ul>
<p>Example Output</p>
<img width="500" alt="image" src="https://github.com/user-attachments/assets/a7df13ef-23b6-4895-baaa-562f70bc30c2" />

<h2>Mad Libs</h2>
<p>
A simple word game where the program takes user inputs (nouns, verbs, adjectives, etc.) and inserts them into a story template to create a fun or random narrative.
</p>

<b>Concepts used:</b>
<ul>
  <li>Input/output handling</li>
  <li>String concatenation and formatting</li>
</ul>

<p>Example Output</p>
<img width="500" alt="image" src="https://github.com/user-attachments/assets/08f35a8c-1458-409b-946e-09901c8db059" />

<h2>Email Slicer</h2>
<p> This is a simple console-based program that parses an email address provided by the user. It uses string manipulation, specifically the <code>split()</code> method, to separate the email into its three core components: the username, the email provider, and the domain extension. The program then neatly displays these individual components to the user. </p>

<b>Concepts used:</b>
<ul>     
  <li>String manipulation using the <code>split()</code> method to break the string at specified delimiters (<code>@</code> and <code>.</code>)</li>     
  <li>Tuple unpacking <code>(a, b) = value</code> for concise assignment of the split components</li>     
  <li>Input handling (<code>input()</code>) for taking the email address from the user</li>     
  <li>String formatting (f-strings) for displaying the results</li> 
</ul>

<p>Example Output</p>
<img width="500" alt="image" src="https://github.com/user-attachments/assets/928257c0-3606-4944-9b69-dce9ceedd810" />

<h2>Word Replacer</h2>

<p> This program demonstrates the basic concept of string manipulation by allowing the user to dynamically replace a specific word within a predefined message. It first displays the original message. Then, it prompts the user to input the word they wish to target and the new word to substitute it with. Finally, it uses the built-in Python <code>.replace()</code> method to perform the substitution and prints the modified string to the console. </p>

<ul>     
  <li>String declaration and basic output (<code>print()</code>)</li>     
  <li>Input handling (<code>input()</code>) to accept words from the user</li>     
  <li>String formatting (f-strings) for interactive prompting</li>     
  <li>The core String Method <code>.replace(old, new)</code> for substitution</li> 
</ul>
<p>Example Output</p>
<img width="600" alt="image" src="https://github.com/user-attachments/assets/a6184a4e-313f-4d2c-a8a6-cd39955e349b" />

<hr>

<h2>Learning Goals</h2>
<ul>
  <li>Strengthen understanding of Python basics</li>
  <li>Practice problem decomposition and logic flow</li>
  <li>Build a foundation for scripting and automation in Python</li>
</ul>

<hr>

<h2>Requirements</h2>
<ul>
  <li>Python 3.x</li>
</ul>

<hr>

<h2>Author</h2>
<p>
<b>Aarya</b><br>
IT Engineering student | Learning Defensive Security and Development
</p>

<hr>

<p>Projects inspired by Kylie Ying and Code with Tomi’s tutorial on YouTube.</p>
