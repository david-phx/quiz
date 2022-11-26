# QUIZ.PY
#### Video Demo: https://youtu.be/8WbMsWI4OUE
#### Description:
This is my final project for *CS50’s Introduction to Programming with Python*.

It's an application that reads a quiz from a file in .json format, asks user the quesions in the quiz, and then calculates and prints the quiz result.

## Usage

To open a quiz, run the following command:

    python project.py quiz.json

where `quiz.json` is the filename of the actual quiz file. If you don't provide any arguments or provide too many, the app will show the instruction on how to use it.
If the file is not a .json file or is in incorrect format, the app will exit with an appropriate message.

To answer a question, enter the answer number. If the user enters a number that doesn't match one of the answers, or enters something else, or doesn't enter anythting at all, the app
will keep asking for an answer until it's provided with a valid one.

Once the user answers all the questions, the program will calculate the score and print it along with a comment.


## Json file format

The quiz is Python dictionary object, where the questions, answers, and possible scores are lists of dictionaries insde the root dictionary. The object is then converted to string using `json.dumps` and
saved to a file, and converted back to object using `json.loads`.

Here's a sample quiz:

    {
        "title": "Sample Quiz",
        "questions": [
            {
                "question": "Is this a question?",
                "answers": [
                    {
                        "answer": "Yes",
                        "points": 1
                    },
                    {
                        "answer": "No",
                        "points": 0
                    },
                    {
                        "answer": "Maybe",
                        "points": 0
                    }
                ]
            },
            {
                "question": "Choose the correct answer:",
                "answers": [
                    {
                        "answer": "Correct",
                        "points": 1
                    },
                    {
                        "answer": "Incorrect",
                        "points": 0
                    },
                    {
                        "answer": "Not sure",
                        "points": 0
                    }
                ]
            }
        ],
        "scores": [
            {
                "score": 0,
                "result": "How could you get both questions wrong?"
            },
            {
                "score": 1,
                "result": "Well, at least you got one question right..."
            },
            {
                "score": 2,
                "result": "Good job, you got 100% right!"
            }
        ]
    }


As you can see, in the sample test a correct answer yields one point, while incorrect answers yield zero, however it's not necessary - the number of points can be any integer. For example, it's possible to award
the user with more points for answers to harder questions, or susbstract points (by adding negative points) for incorrect answers.

## Determining the result

After getting all the answers and adding up points, the app determines the result. It's done by iterating through the list of scores sorted by lowest first, and comparing the user score to
the score values, until it finds one that's equal or higher than the user's score. For example, if the scores dictionary has score values of 3, 7, and 10, and the user got 5 points, the app
will skip 3, and print out the score with value 7. The highest possible value in the scores dictionary **has** to be equal to the maximum possible scores the user can get (so the 100% will
always be a separate result), however the app doesn't valdate it - it is assumed that the quiz meets all the requirements.

## Functions

Here's the list of functions in the project:

**get_filename(argv)**

Processes command line, exits with a message if there are not enough or too many arguments, and returns the filename if only one argument is provided.

**get_quiz(filename)**

Tries to open *filename* and convert it's contents into a quiz. If the file can't be opened or has incorrect format, exits the app with a message.

**run_quiz(quiz)**

Prints the quiz title, iterates through questions, and returns the total score.

**ask(index, total, question)**

Asks a question, and returns the amount of points. The order of answers is randomized. `Index` and `total` are used to be able to print "Question `index` of `total`:"

**show_result(score, scores)**

Prints the user's score.

**hr(symbol="─", times=120)**

returns a sting consisting of `symbol * times`. Used to print a horizontal line to visually separate questions from one another.

## Files

**project.py**

The main project file.

**test_project.py**

Tests of project functions. Usage:

    pytest test.project.py

**quiz.json**

Sample quiz.

**startrek.json**

Star Trek quiz.

## Thank you

That's pretty much it.

Thank you for the course, it was fun, and see you in the next one! CS50AI, here I come.












