# Python Quiz Generator

A Python script that generates randomized US state capitals quizzes with answer keys.

## Features

- Generates 5 different quiz forms with randomized questions
- Each quiz contains 50 multiple-choice questions about US state capitals
- Automatically creates answer keys for each quiz
- Questions are shuffled to prevent cheating between forms
- Answer choices are randomized for each question

## Usage

Run the script to generate quiz files:

```bash
python generate_state_capitals_quiz.py
```

This will create a `quizzes` directory containing:
- `capitals_quiz_1.txt` through `capitals_quiz_5.txt` - The quiz forms
- `capitals_answers_1.txt` through `capitals_answers_5.txt` - The corresponding answer keys

## Quiz Format

Each quiz includes:
- Header with form number, name, date, and period fields
- 50 multiple-choice questions (A, B, C, D format)
- Questions ask "What is the capital of [State]?"

## Requirements

- Python 3.x
- No external dependencies required (uses only built-in modules)

## Data

Includes all 50 US states and their capitals in the quiz pool.