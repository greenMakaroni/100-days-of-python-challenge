class QuizBrain:
    def __init__(self, question_list):
            # q for question
        self.q_list = question_list
        self.q_number = 0
        self.score = 0

    def next_question(self):
        current_question = self.q_list[self.q_number]
        user_answer = input(f'Question number { self.q_number + 1 }. { current_question.text }?, True / False ')
        if user_answer.lower() == current_question.answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong")
        
        self.q_number += 1
        print(f"Correct answer: {current_question.answer}")
        print(f"Your current score is: {self.score}/{len(self.q_list)}")
        print("\n")
       
        

    def still_has_questions(self):
        return self.q_number < len(self.q_list)
    


          
    