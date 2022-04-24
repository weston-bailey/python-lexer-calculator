def is_float(string):
    '''
        tests if string is a valid float, returns bool
    '''
    try:
        float(string)
        return True
    except ValueError:
        return False

def is_int(string):
    '''
        tests if string is a valid int, returns bool
    '''
    try:
        int(string)
        return True
    except ValueError:
        return False

def tokenize(string):
    '''
        takes string and returns valid token list
    '''
    # all valid operation symbols
    symbols =  [ '(', ')',  '^',  '*',  '/',  '+', '-' ]
    # list to store tokens 
    tokens = []
    current_string = ''
    for i, char in enumerate(string):
        if char == '(' or char == ')':
            # closing ')' will have value before them
            if current_string:
                tokens.append(current_string.strip())
                current_string = ''
            # add the '(' or ')'
            tokens.append(char)
        elif char == ' ' and current_string != '':
            # if there is a space and a value we can assume a value has finished
            tokens.append(current_string.strip())
            current_string = ''
        elif i + 1 == len(string):
            # we are on the last char
            current_string += char
            tokens.append(current_string.strip())
        else:
            current_string += char
    
    # strings to nums 
    for i, token in enumerate(tokens):
        if is_int(token):
            tokens[i] = int(token)
        elif is_float(token):
            tokens[i] = float(token)
        elif token not in symbols:
            print(f'symbol "{token}" not recognized as a valid operator, use: () ^ * / + -')
            quit()

    return tokens

# splitting calculations into sep functions so it can recurse
def calc(tokens):
    '''
        flattens list of tokens down to single value
    '''
    # going to have one loop per operator
    # because -- how can you add unless you know that all parens are taken care of

    # ## # ## #
    # parenthsis

    i = 0
    stop = len(tokens)
    while i < stop:
        if tokens[i] == '(':
            # build list to recursively invoke
            sub_tokens = []
            # start one after i, since i is a '('
            j = i + 1
            # the problem is, when parens are nested (4 * (2 + 3))
            # the first paran '3)' is matched and the second paren is not passed to the recursion 4 * (2 + 3
            # when it should be  4 * (2 + 3)
            while tokens[j] != ')':
                print('j', j, tokens[j])
                print(tokens)
                sub_tokens.append(tokens[j])
                j += 1
            
            return calc(tokens[:i] + [calc(sub_tokens)] + tokens[j + 1:])
        
        i += 1

    # ## # ## #          
    
    # non parens ops
    # exponents
    i = 0
    while i < len(tokens):
        if tokens[i] == '^':
            power = tokens[i - 1] ** tokens[i + 1]
            tokens = tokens[:i - 1] + [power] + tokens[i + 2:]
            i = i - 1
        i += 1

    # multiplacation
    i = 0
    while i < len(tokens):
        if tokens[i] == '*':
            prod = tokens[i - 1] * tokens[i + 1]
            tokens = tokens[:i - 1] + [prod] + tokens[i + 2:]
            i = i - 1
        i += 1

    # division
    i = 0
    while i < len(tokens):
        if tokens[i] == '/':
            div = tokens[i - 1] / tokens[i + 1]
            tokens = tokens[:i - 1] + [div] + tokens[i + 2:]
            i = i - 1
        i += 1

    # addition
    i = 0
    while i < len(tokens):
        if tokens[i] == '+':
            sum_of = tokens[i - 1] + tokens[i + 1]
            tokens = tokens[:i - 1] + [sum_of] + tokens[i + 2:]
            i = i - 1
        i += 1

    # subraction
    i = 0
    while i < len(tokens):
        if tokens[i] == '-':
            diff = tokens[i - 1] - tokens[i + 1]
            tokens = tokens[:i - 1] + [diff] + tokens[i + 2:]
            i = i - 1
        i += 1


    return tokens[0]


# input '142 + 4 * 10 + (4 * 5)'
text = '142 + 4 * 10 + (4 * 5) + (2 ^ 4) - (10 / 2)'
# text = '142 + 4 - 6 / 2 * 3'
# text = '142 + 4 + 3 - 5 * 5'
# text = '3 * 3 + 2 - 10 / 2'

## curently failing nested parens
# text = '142 + 4 * 10 + (4 * 5) - (10 / (1 + 1))'


split = tokenize(text)
print('split:', split)

calculation = calc(split)
print('calculation:', calculation )

# print ("Welcome to the lexer!")

# while True: 
#     text = input(">")

