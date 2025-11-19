questions_dict = {
    'question1' : {
        'Q' : 'What is the first letter of word "Shirt"',
        'answer' : 's'
    },
    'question2' : {
        'Q' : 'Where does a dog live?',
        'answer' : 'kennel'
    },
    'question3' : {
        'Q' : 'After how many years does a leap year come?',
        'answer' : '4'
    }
}

points = 0

print("\nWelcome To Quiz!\n")

for key_of_question_dict, value_of_question_dict in questions_dict.items():

    print(value_of_question_dict['Q'])
    user_input = input("Answer: ").lower()
    if user_input == value_of_question_dict['answer']:
        print("Correct!")
        points = points + 1
    else:
        print("Incorrect!")
    print()
    
print(f"You've earned {points} points.")
    