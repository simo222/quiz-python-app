cd ./4-simple-quiz-json-multiple-choice-questions
python3 quiz-python-app1-question-quiz-no-lambda-functions.py


## run this command unittest  
cd ./4-simple-quiz-json-multiple-choice-questions
python3 test_quiz.py


## to use podman 
cd ./4-simple-quiz-json-multiple-choice-questions
podman build -t quiz-app .
podman run -it --rm quiz-app
