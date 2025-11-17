"""Mad Libs are stories with words removed and replaced by blank spaces. 
One player acts as the “reader” and asks the other players, who haven’t seen the story, 
to fill in the blanks with adjectives, nouns, exclamations, colors, adjectives, and more. 
These words are inserted into the blanks and then the story is read aloud to hilarious results."""

adjective1 = input("Provide an adjective: ").lower()
adjective2 = input("Provide another adjective: ").lower()
verb1 = input("Provide a verb: ").lower()
verb2 = input("Provide another verb: ").lower()

paragraph = f"A {adjective1} option for complete beginners without any experience to {verb1}. \
If you're looking for a {adjective2} intro to this very deep language, I have to {verb2} this book."

print(paragraph)