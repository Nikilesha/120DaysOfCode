class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score= 0
    

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer =input(f"Q.{self.question_number}: {current_question.text} (True/False): ")

        self.correct(user_answer,current_question.answer)

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
        
    def correct(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right")
            self.score += 1
        else:
            print("You got it wrong")
        print("the answer is : ",correct_answer)
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")    