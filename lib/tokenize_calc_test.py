from lib.tokenize import tokenize
from lib.calc import calc
from unittest import TestCase, main

input_one = '142 + 4 * 10 / 1 ^ 2 - 1'
tokens_one = [142, '+', 4, '*', 10, '/', 1, '^', 2, '-', 1]
result_one = 181.0

input_two = '142 + 4 - 6 / 2 * 3'
tokens_two = [142, '+', 4, '-', 6, '/', 2, '*', 3]
result_two = 137

input_three = '142 + (4 + 3) ^ (5 * 5)'
tokens_three = [142, '+', '(', 4, '+', 3, ')', '^', '(', 5, '*', 5, ')']
result_three = 1341068619663964900949

input_four = '3 * (3 + 2) - 10 / 2'
tokens_four = [3, '*', '(', 3, '+', 2, ')', '-', 10, '/', 2]
result_four = 10

## curently failing nested parens
input_five = '142 + 4 * 10 + (4 * 5) - (10 / (1 + 1))'
tokens_five = [142, '+', 4, '*', 10, '+', '(', 4, '*', 5, ')', '-', '(', 10, '/', '(', 1, '+', 1, ')', ')']
result_five = 197

class TestTokenize(TestCase):
    def test_input_one(self):
        print(f"input_one: {input_one}")

        print(f"\tshould return {tokens_one}")
        self.assertListEqual(tokenize(input_one), tokens_one)

    def test_input_two(self):
        print(f"input_two: {input_two}")

        print(f"\tshould return {tokens_two}")
        self.assertListEqual(tokenize(input_two), tokens_two)

    def test_input_three(self):
        print(f"input_three: {input_three}")

        print(f"\tshould return {tokens_three}")
        self.assertListEqual(tokenize(input_three), tokens_three)

    def test_input_four(self):
        print(f"input_four: {input_four}")

        print(f"\tshould return {tokens_four}")
        self.assertListEqual(tokenize(input_four), tokens_four)

    def test_input_five(self):
        print(f"input_five: {input_five}")

        print(f"\tshould return {tokens_five}")
        self.assertListEqual(tokenize(input_five), tokens_five)

class TestCalc(TestCase):
    def test_tokens_one(self):
        print(f"tokens_one: {tokens_one}")

        print(f"\tit should return {result_one}")
        self.assertEquals(calc(tokens_one), result_one)
    
    def test_tokens_two(self):
        print(f"tokens_two: {tokens_two}")

        print(f"\tit should return {result_two}")
        self.assertEquals(calc(tokens_two), result_two)

    def test_tokens_three(self):
        print(f"tokens_three: {tokens_three}")

        print(f"\tit should return {result_three}")
        self.assertEquals(calc(tokens_three), result_three)
    
    def test_tokens_four(self):
        print(f"tokens_four: {tokens_four}")

        print(f"\tit should return {result_four}")
        self.assertEquals(calc(tokens_four), result_four)
    
    def test_tokens_five(self):
        print(f"tokens_five: {tokens_five}")

        print(f"\tit should return {result_five}")
        self.assertEquals(calc(tokens_five), result_five)

if __name__ == "main":
    main()
