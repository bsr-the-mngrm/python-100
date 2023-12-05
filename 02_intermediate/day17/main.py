from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

if __name__ == '__main__':
    question_bank = []

    for question in question_data:
        question_bank.append(Question(question['text'], question['answer']))

    quiz = QuizBrain(question_bank)

    while quiz.still_has_questions():
        quiz.next_question()

    print("\nYou've completed the quiz")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")
