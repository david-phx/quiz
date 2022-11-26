import json
from random import shuffle
import sys


def main():
    filename = get_filename(sys.argv)
    quiz = get_quiz(filename)
    score = run_quiz(quiz)
    show_result(score, quiz["scores"])


def get_filename(argv):
    if len(argv) < 2:
        sys.exit("Usage: python project.py \x1B[3m" + "quiz.json" + "\x1B[0m")
    elif len(argv) > 2:
        sys.exit("Usage: python project.py \x1B[3m" + "quiz.json" + "\x1B[0m")
    else:
        return argv[1]


def get_quiz(filename):
    if filename[filename.rfind(".") + 1 :] != "json":
        sys.exit(filename + " is not a .json file")
    try:
        file = open(filename, "r")
    except FileNotFoundError:
        sys.exit(filename + " does not exist")
    try:
        quiz = json.loads(file.read())
    except json.JSONDecodeError:
        file.close()
        sys.exit("Incorrect file format")
    else:
        file.close()
        return quiz


def run_quiz(quiz):
    print(hr())
    print(f"QUIZ: {quiz['title']}")

    score = 0
    total = len(quiz["questions"])

    for index, question in enumerate(quiz["questions"], 1):
        score += ask(index, total, question)
    return score


def ask(index, total, question):
    # os.system('clear')
    print(hr())
    print(f"Question {index} of {total}: {question['question']}\n")

    shuffle(question["answers"])
    for i, answer in enumerate(question["answers"], 1):
        print(f"({i})", answer["answer"])

    print()
    while True:
        try:
            choice = int(input("Your answer? "))
        except ValueError:
            pass
        try:
            if 1 <= choice <= len(question["answers"]):
                break
        except UnboundLocalError:
            pass

    return int(question["answers"][choice - 1]["points"])


def show_result(score, scores):
    scores = sorted(scores, key=lambda s: s["score"])
    max_score = max(result["score"] for result in scores)

    print(hr())
    print(f"Your score: {score}/{max_score}\n")

    for result in scores:
        if score <= result["score"]:
            print(result["result"])
            break
    print(hr())


def hr(symbol="─", times=120):
    return symbol * times


# TODO: Take input from user and save quiz to file
def create_quiz():
    quiz = {}

    quiz["title"] = input("Title: ")

    questions = []
    while True:
        question = {}
        question["question"] = input("Question: ")
        if question["question"] != "":
            answers = []
            while True:
                answer = input("Answer: ")
                if answer != "":
                    points = input("Points: ")
                    answers.append({"answer": answer, "points": int(points)})
                else:
                    break
            question["answers"] = answers
            questions.append(question)
        else:
            break
    quiz["questions"] = questions

    scores = []
    while True:
        result = input("Result: ")
        if result != "":
            points = int(input("Score: "))
            scores.append({"score": points, "result": result})
        else:
            break
    quiz["scores"] = scores

    # TODO: Save to file instead
    print(json.dumps(quiz, indent=4))


if __name__ == "__main__":
    main()
