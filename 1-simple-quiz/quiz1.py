def quiz():
    questions = {
        "What is the name of the Kubernetes API object that represents a group of containers?": "Pod",
        "Which Kubernetes component is responsible for maintaining the desired state of the cluster?": "Controller",
        "What is the default package manager for Kubernetes?": "Helm",
        "What command is used to view the status of Kubernetes resources?": "kubectl get",
        "which kubernetes object is used to isolate resources?": "Namespace"
    }
    score = 0 

    for question, answer  in questions.items(): 
        user_answer = input(question + "\n")
        if user_answer.strip().lower() == answer.lower():
            print("Correct")
            score += 1 
        else:
            print(f"wrong. The correct anser is {answer}")


    print(f"\n Your final score is : {score}/{len(questions)}")
if __name__ == "__main__": 
    quiz()