import json

def quiz():
    try:
        with open("questions.json", "r") as f:
            questions = json.load(f)
    except FileNotFoundError:
        print("Questions file not found.")
        return
    except json.JSONDecodeError:
        print("Error decoding the questions file.")
        return

    score = 0

    for key, qa in questions.items():
        user_answer = input(qa["question"] + "\n")
        if user_answer.strip().lower() == qa["answer"].lower():
            print("Correct")
            score += 1
        else:
            print(f"Wrong. The correct answer is {qa['answer']}")

    print(f"\nYour final score is: {score}/{len(questions)}")

if __name__ == "__main__":
    quiz()
