import random
import sys


class ArithmeticExamApplication:

    def __init__(self):
        # for expression generator
        self.operators = ['+', '-', '*']
        self.yes = ['yes', 'Yes', 'YES', 'y']
        self.numbers = None
        self.operator = None
        self.num_1 = None
        self.num_2 = None

        # messages
        self.right_message = "Right!"
        self.wrong_message = "Wrong!"
        self.incorrect_message = "Incorrect format."
        self.mark_message = None
        self.introductory_message = """Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29"""
        self.one_message = "simple operations with numbers 2-9"
        self.two_message = "integral squares of 11-29"
        self.saving_message = "Would you like to save the result? Enter yes or no."
        # for checker
        self.question = None
        self.right_answer = None

        self.answer = None
        self.right_answer = None
        self.level_description = 0
        # for score
        self.score = 0

        # for start
        self.level = None

    def level_one(self):
        self.question = self.expression_generator()  # picking the expression
        self.right_answer = eval(self.question)  # solving the expression
        print(self.question)
        while True:
            try:
                self.answer = int(input())
                if self.right_answer == self.answer:  # correct answer
                    print(self.right_message)
                    # add 1 to score
                    self.score += 1
                    break
                else:
                    print(self.wrong_message)
                    break
            except ValueError:
                print(self.incorrect_message)

    # returning a randomized expression
    def expression_generator(self):
        self.numbers = [_ for _ in range(2, 10)]
        self.operator = random.choice(self.operators)  # random operator
        self.num_1 = random.choice(self.numbers)  # random single digit
        self.num_2 = random.choice(self.numbers)  # random single digit
        return f'{self.num_1} {self.operator} {self.num_2}'

    def integral_squares(self):
        self.numbers = [_ for _ in range(11, 30)]
        self.num_1 = random.choice(self.numbers)
        return f'{self.num_1}'

    def level_two(self):
        self.question = self.integral_squares()
        self.right_answer = eval(self.question + ' ** 2')
        print(self.question)
        while True:
            try:
                self.answer = int(input())
                if self.right_answer == self.answer:  # correct answer
                    print(self.right_message)
                    # add 1 to score
                    self.score += 1
                    break
                else:
                    print(self.wrong_message)
                    break
            except ValueError:
                print(self.incorrect_message)

    def start(self):
        while True:
            try:
                print(self.introductory_message)
                self.level = input()
                if len(self.level) == 1:
                    if int(self.level) == 1:
                        self.level_description = 1
                        self.exam_loop_one()
                        break
                    elif int(self.level) == 2:
                        self.level_description = 2
                        self.exam_loop_two()
                        break
                    else:
                        print(self.wrong_message)
                        continue
                else:
                    print(self.incorrect_message)
                    continue
            except ValueError:
                print(self.incorrect_message)

    def exam_loop_one(self):
        [self.level_one() for _ in range(5)]
        self.save()

    def exam_loop_two(self):
        [self.level_two() for _ in range(5)]
        self.save()

    def mark(self):
        return f'Your mark is {self.score}/5.' + self.saving_message

    def save(self):
        self.mark_message = self.mark()
        print(self.mark_message)
        self.answer = input()
        if self.answer in self.yes:
            print("What is your name?")
            username = input()
            with open('results.txt', 'a') as results:
                results.write(f'{username}: {self.score}/5 in level {self.level_description} ({ self.one_message if self.level_description == 1 else self.two_message}).')
            print('The results are saved in "results.txt".')
        else:
            sys.exit()


# 1. With the first message, the program should ask for a
#    difficulty level:
#    1 - simple operations with numbers 2 - 9
#    2 - integral squares 11 - 29
def main():
    exam = ArithmeticExamApplication()
    exam.start()


if __name__ == '__main__':
    main()