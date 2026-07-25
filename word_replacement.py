# Takes in a word from the sentence and replaces it with the word provided

message = "Hi Aarya, How are you?"
print(message)

word_to_replace = input("Please enter the word you want to replace: ")
word_replacement = input(
    f"Please enter the word you want to replace '{word_to_replace}' with: "
    )

print(message.replace(word_to_replace, word_replacement))