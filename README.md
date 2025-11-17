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
<img width="644" height="488" alt="image" src="https://github.com/user-attachments/assets/2a2e6a7e-8405-4b56-ab55-fe6fc419547c" />

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
<img width="558" height="540" alt="image" src="https://github.com/user-attachments/assets/0300b49f-1c1f-4d78-b5f3-0f2a18852c23" width=300/>
<img width="653" height="559" alt="image" src="https://github.com/user-attachments/assets/816905f5-59d2-406d-9376-8b84e9760a25" width=300/>

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
<img width="560" height="492" alt="image" src="https://github.com/user-attachments/assets/36bc199c-eeb2-41ce-af82-d7e3a50c888c" />

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
<img width="625" height="460" alt="image" src="https://github.com/user-attachments/assets/109303cc-1032-4c17-8973-eb4220ebb348" />
<h4>Computer tries to guess the number:</h4>
<img width="732" height="779" alt="image" src="https://github.com/user-attachments/assets/419e7cf1-6deb-4562-bc0e-10e0ddeee883" />

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
<img width="704" height="426" alt="image" src="https://github.com/user-attachments/assets/102877ff-2129-4cb4-b534-25260512e834" />

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
<img width="569" height="315" alt="image" src="https://github.com/user-attachments/assets/5cd30991-16ac-4978-b440-af9571b5ab57" />

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
<img width="700" height="295" alt="image" src="https://github.com/user-attachments/assets/115b2563-ffb7-4122-adee-4af2a029ac0b" />

<h2>Word Replacer</h2>

<p> This program demonstrates the basic concept of string manipulation by allowing the user to dynamically replace a specific word within a predefined message. It first displays the original message. Then, it prompts the user to input the word they wish to target and the new word to substitute it with. Finally, it uses the built-in Python <code>.replace()</code> method to perform the substitution and prints the modified string to the console. </p>

<ul>     
  <li>String declaration and basic output (<code>print()</code>)</li>     
  <li>Input handling (<code>input()</code>) to accept words from the user</li>     
  <li>String formatting (f-strings) for interactive prompting</li>     
  <li>The core String Method <code>.replace(old, new)</code> for substitution</li> 
</ul>
<p>Example Output</p>
<img width="823" height="291" alt="image" src="https://github.com/user-attachments/assets/6f9f8620-475a-477e-bcaa-c08c6a1b6deb" />

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

<p>Projects inspired by Kylie Ying’s tutorial on YouTube.</p>
