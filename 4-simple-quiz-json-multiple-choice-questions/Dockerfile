# Use official lightweight Python image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy only the Python script and JSON file
COPY 2-questions-quiz-json-lambda.py .
COPY questions.json .

# Default command to run the Python script
CMD ["python", "2-questions-quiz-json-lambda.py"]
