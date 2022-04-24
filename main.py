from lib.tokenize import tokenize
from lib.calc import calc

# input '142 + 4 * 10 + (4 * 5)'
# text = '142 + 4 * 10 + (4 * 5) + (2 ^ 4) - (10 / 2)'
# text = '142 + 4 - 6 / 2 * 3'
# text = '142 + 4 + 3 - 5 * 5'
# text = '3 * 3 + 2 - 10 / 2'

## curently failing nested parens
text = '142 + 4 * 10 + (4 * 5) - (10 / 2)'


split = tokenize(text)
print('split:', split)

calculation = calc(split)
print('calculation:', calculation )

# print ("Welcome to the lexer!")

# while True: 
#     text = input(">")

