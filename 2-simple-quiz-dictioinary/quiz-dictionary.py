def quiz():
    questions = {
        "question1": {
            "question": "What is the name of the Kubernetes API object that represents a group of containers?",
            "answer": "Pod"
        },
        "question2": {
            "question": "Which Kubernetes component is responsible for maintaining the desired state of the cluster?",
            "answer": "Controller"
        },
        "question3": {
            "question": "What is the default package manager for Kubernetes?",
            "answer": "Helm"
        },
        "question4": {
            "question": "What command is used to view the status of Kubernetes resources?",
            "answer": "kubectl get"
        },
        "question5": {
            "question": "Which Kubernetes object is used to isolate resources?",
            "answer": "Namespace"
        }
    }
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
