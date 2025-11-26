# python-fundamental-projects

<p>
A collection of small Python projects built to strengthen programming logic and problem-solving skills.  
Currently includes:
<ul>
  <li><a href="#password-manager">Password Manager</a></li>
  <li><a href="#password-generator">Password Generator</a></li>
  <li><a href="#hangman">Hangman</a></li>
  <li><a href="#rock-paper-scissor">Rock-Paper-Scissor</a></li>
  <li><a href="#guess-the-number">Guess the Number</a></li>
  <li><a href="#basic-calculator">Basic Calculator</a></li>
  <li><a href="#dice-simulator">Dice Simulator</a></li>
  <li><a href="#quiz">Quiz</a></li>
  <li><a href="#date-and-time-display">Date and Time Display</a></li>
  <li><a href="#countdown-timer">Countdown Timer</a></li>
  <li><a href="#mad-libs">Mad Libs</a></li>
  <li><a href="#email-slicer">Email Slicer</a></li>
  <li><a href="#word-replacer">Word Replacer</a></li>
</ul>
</p>

<hr>

<h1>About</h1>
<p>
This repository is part of my foundational learning in <b>Python programming</b>, supporting my journey as an <b>IT Engineering student</b> focused on <b>Full Stack Development</b> and <b>CyberSecurity</b>.<br>
Each mini project is designed to reinforce programming concepts like variables, conditionals, loops, and input handling.
</p>

<hr>

<h1>Projects</h1>

<h3>Password Manager</h3>
<p>
A command-line password manager that allows users to securely store, view, update, and remove account credentials. 
The application is structured into modular components for handling operations, validating user input, and managing password-related functionality. 
The program ensures controlled input flow, persistent looping for menu navigation, and organized function handling for each operation.
</p>

<b>Concepts used:</b>
<ul>
  <li>Modular project structure with multiple Python files</li>
  <li>Input validation using custom validation functions</li>
  <li>Loop-based menu system for continuous user interaction</li>
  <li>CRUD operations (Create, Read, Update, Delete) for managing entries</li>
  <li>Separation of concerns through dedicated modules</li>
  <li>Error handling using try/except blocks</li>
</ul>

<p>Example Output</p>
<img width="550" alt="Screenshot_20251126_102145" src="https://github.com/user-attachments/assets/1f6ad6b3-bbbb-4164-9f99-092d92c1e85f" />

<img width="550" alt="Screenshot_20251126_102243" src="https://github.com/user-attachments/assets/3ac9fa10-288f-4521-bb48-901941533807" />

<img width="550" alt="Screenshot_20251126_102318" src="https://github.com/user-attachments/assets/0a2b66fb-bc7b-45a1-a0c8-11270d62d064" />

<img width="550" alt="Screenshot_20251126_102402" src="https://github.com/user-attachments/assets/a90ed41f-142b-465f-a09d-93581cb79ff7" />


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

<h2>Dice Simulator</h2>
<p>
A program that simulates rolling two six-sided dice. Each roll randomly selects values from predefined ASCII art representations and displays the visual output of both dice to the user.
</p>

<b>Concepts used:</b>
<ul>
  <li>Random number generation</li>
  <li>Dictionaries for structured data storage</li>
  <li>Loops and conditional logic</li>
  <li>User input handling</li>
</ul>

<p>Example Output</p>
<img width="500" alt="image" src="https://github.com/user-attachments/assets/c0a655ce-6505-4558-a055-8bf074f365b8" />

<h2>Quiz</h2>
<p>
A basic terminal-based quiz that iterates through a predefined set of questions, accepts user input, compares answers, and tracks the total score.
</p>

<b>Concepts used:</b>
<ul>
  <li>Dictionaries for structured data storage</li>
  <li>Loops for sequential question processing</li>
  <li>User input handling</li>
  <li>String normalization using <code>.lower()</code></li>
  <li>Conditional checks for answer validation</li>
  <li>Basic scoring logic</li>
</ul>

<p>Example Output</p>
<img width="600" alt="image" src="https://github.com/user-attachments/assets/bb0d57b4-ea7c-4e4b-9fa8-8b9c361cd312" />

<h2>Date and Time Display</h2>
<p> A basic program that retrieves the system’s current date and time using Python’s <code>time</code> module and prints it in a human-readable format. It extracts day, month, and year values, as well as hour, minute, and second values, and outputs them separately. </p>

<b>Concepts used:</b>
<ul> 
  <li>Using the <code>time</code> module</li> 
  <li>Accessing system time structures</li> 
  <li>Formatted string output</li> 
</ul>
  
<p>Example Output</p>
<img width="600" alt="image" src="https://github.com/user-attachments/assets/3c5afe51-3525-4b07-8dd6-a450b02aeadf" />

<h2>Countdown Timer</h2> 
<p> A basic timer that accepts a number of seconds from the user and performs a countdown, printing each remaining second until it reaches zero. </p>

<b>Concepts used:</b>

<ul> 
  <li>User input handling</li> 
  <li>Loop control</li> 
  <li>Time delay using <code>time.sleep()</code></li>
</ul>
<p>Example Output</p>
<img width="400" alt="image" src="https://github.com/user-attachments/assets/8515a4ab-6839-4ece-a518-80e3962cfaf5" />

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
<p> This is a simple console-based program that parses an email address provided by the user. It uses string manipulation, specifically the <code>split()</code> method, to separate the email into its three core components: the username, the email provider, and the domain extension. </p>

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

<p> This program demonstrates the basic concept of string manipulation by allowing the user to dynamically replace a specific word within a predefined message. It uses the built-in Python <code>.replace()</code> method to perform the substitution and prints the modified string to the console. </p>

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
