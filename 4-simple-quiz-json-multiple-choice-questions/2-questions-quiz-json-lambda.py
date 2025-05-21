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

    for key, questionOptionsAnswer in questions.items():
        question = questionOptionsAnswer["question"]
        if "choices" in questionOptionsAnswer:
            choices = questionOptionsAnswer["choices"]
            # Display question and choices with labels
            print(question)
            for label, choice in choices.items():
                print(f"{label}. {choice}")
            if isinstance(questionOptionsAnswer["answer"], list):
                user_answer = input("Enter all correct choices separated by commas (e.g., A,C): ").strip().upper()
                user_answers = [ans.strip() for ans in user_answer.split(",") if ans.strip() in choices]
                correct_answers = questionOptionsAnswer["answer"]
                if set(user_answers) == set(correct_answers):
                    print("Correct")
                    score += 1
                else:
                    correct_choices = ", ".join([f"{label}. {choices[label]}" for label in correct_answers])
                    print(f"Wrong. The correct answers are: {correct_choices}")
            else:
                user_answer = input("Enter your choice (e.g., A): ").strip().upper()
                # Validate user input
                if user_answer in choices:
                    if user_answer == questionOptionsAnswer["answer"]:
                        print("Correct")
                        score += 1
                    else:
                        correct_label = questionOptionsAnswer["answer"]
                        correct_choice = choices[correct_label]
                        print(f"Wrong. The correct answer is {correct_label}. {correct_choice}")
                else:
                    print("Invalid choice. Question skipped.")
        else:
            # Simple Q&A question
            user_answer = input(question + "\n")
            if user_answer.strip().lower() == questionOptionsAnswer["answer"].lower():
                print("Correct")
                score += 1
            else:
                print(f"Wrong. The correct answer is {questionOptionsAnswer['answer']}")

    print(f"\nYour final score is: {score}/{len(questions)}")

if __name__ == "__main__":
    quiz()
