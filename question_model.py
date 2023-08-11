class Question:
    # create a new instance of the question, it should hold the text,
    # which is the question retrieved from data.py, and it holds the
    # answer to that question (True/False)
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

