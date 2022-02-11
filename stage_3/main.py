import random


class ArithmeticExamApplication:
    def __init__(self):
        self.operators = ['+', '-', '*']
        self.numbers = [_ for _ in range(2, 10)]
        self.operator = None
        self.num_1 = None
        self.num_2 = None
        self.answer = None
        self.right_message = "Right!"
        self.wrong_message = "Wrong!"
        self.incorrect_message = "Incorrect format."
        self.question = None
        self.right_answer = None
        self.correct_answer = 0
        self.mark_message = ''

    def checker(self):
        self.question = self.operation_generator()
        self.right_answer = eval(self.question)
        print(self.question)
        while True:
            # print(self.right_message if self.right_answer == self.answer else self.wrong_message)
            try:
                self.answer = int(input())
                if self.right_answer == self.answer:
                    print(self.right_message)
                    self.correct_answer += 1
                    break
                else:
                    print(self.wrong_message)
                    break
            except ValueError:
                print(self.incorrect_message)

    def operation_generator(self):
        self.operator = random.choice(self.operators)
        self.num_1 = random.choice(self.numbers)
        self.num_2 = random.choice(self.numbers)
        return f'{self.num_1} {self.operator} {self.num_2}'

    def start(self):
        self.exam_loop()

    def exam_loop(self):
        for _ in range(5):
            self.checker()
        self.mark_message = self.mark()
        print(self.mark_message)

    def mark(self):
        return f'Your mark is {self.correct_answer}/5.'


def main():
    exam = ArithmeticExamApplication()
    exam.start()


if __name__ == '__main__':
    main()