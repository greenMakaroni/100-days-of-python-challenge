class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
        print(f"self.text: {self.text}, self.answer: {self.answer}")


question1 = Question("2 + 5 = 6", False)