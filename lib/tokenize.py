from lib.type_check import is_float, is_int

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
            return False
    print(tokens)
    return tokens
