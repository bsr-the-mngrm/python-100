from data import question_data
from question_model import Question

if __name__ == '__main__':
    question_bank = []

    for question in question_data:
        question_bank.append(Question(question['text'], question['answer']))


