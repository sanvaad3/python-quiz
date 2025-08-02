import random
import os

# A dictionary of US states and their capitals
capitals = {
    'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
    'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
    'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
    'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines',
    'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston',
    'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln',
    'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
    'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville',
    'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier',
    'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
    'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'
}

# Create a directory to store the quiz and answer files
os.makedirs("quizzes", exist_ok=True)

# Generate 5 quiz files (change to 35 if needed)
for quiz_num in range(5):
    # Open files for quiz and answer key
    quiz_file = open(f'quizzes/capitals_quiz_{quiz_num + 1}.txt', 'w')
    answer_file = open(f'quizzes/capitals_answers_{quiz_num + 1}.txt', 'w')

    # Write headers
    quiz_file.write((' ' * 20) + f'State Capitals Quiz (Form {quiz_num + 1})\n')
    quiz_file.write('\nName:\n\nDate:\n\nPeriod:\n\n')
    quiz_file.write(('-' * 60) + '\n\n')

    # Randomize the order of states
    states = list(capitals.keys())
    random.shuffle(states)

    # Create 50 questions
    for question_num in range(50):
        correct_answer = capitals[states[question_num]]
        wrong_answers = list(capitals.values())
        wrong_answers.remove(correct_answer)
        wrong_options = random.sample(wrong_answers, 3)
        answer_options = wrong_options + [correct_answer]
        random.shuffle(answer_options)

        # Write question and options to quiz file
        quiz_file.write(f'{question_num + 1}. What is the capital of {states[question_num]}?\n')
        for i in range(4):
            quiz_file.write(f"    {'ABCD'[i]}. {answer_options[i]}\n")
        quiz_file.write('\n')

        # Write the correct answer to the answer file
        correct_letter = 'ABCD'[answer_options.index(correct_answer)]
        answer_file.write(f'{question_num + 1}. {correct_letter}\n')

    # Close the files
    quiz_file.close()
    answer_file.close()
