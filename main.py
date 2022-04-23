# lexer calculator

# input '142 + 4 * 10 + (4 * 5)'
# text = '142 + 4 * 10 + (4 * 5)'
text = '142 + 4'

# separate tokens from string
    # maybe toss them in a list
    # '142 + 4 * 10 + (4 * 5)' => [ '142', '+', '4', '*', '10', '+', '(', '4', '*', '5', ')' ]
        # will need to identify numbers, symbols and spaces (possibly invaldis chars too)

# all valid operation symbols
symbols =  [ '(', ')',  '^',  '*',  '/',  '+' ] 

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def is_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

def tokenize(string):
    # perform the split
    tokens = []
    current_string = ''
    for i, char in enumerate(string):
        if char == '(' or char == ')':
            # closing ')' will have value before them
            if current_string:
                tokens.append(current_string)
                current_string = ''
            # add the '(' or ')'
            tokens.append(char)
        elif char == ' ' and current_string != '':
            # if there is a space and a value we can assume a value has finished
            tokens.append(current_string)
            current_string = ''
        elif i + 1 == len(string):
            # we are on the last char
            current_string += char
            tokens.append(current_string)
        else:
            current_string += char
    
    # strings to nums 
    for i, token in enumerate(tokens):
        if is_int(token):
            tokens[i] = int(token)
        elif is_float(token):
            tokens[i] = float(token)
        elif token not in symbols:
            print(f'symbol {token} not recognized as a valid operator, use: () ^ * / + -')
            quit()

    return tokens

split = tokenize(text)
print(split)

# splitting calculations into sep functions so it can recurse
def calc(tokens):
    pass
    # going to have one loop per operator
    # because -- how can you add unless you know that all parens are taken care of
    # i = 0
    # stop = len(tokens)
    # while i < stop:
    #     if token == '(':
    #         # build list to recursively invoke
    #         sub_tokens = []
    #         # start one after i, since i is a '('
    #         j = i + 1
    #         while tokens[j] != ')':
    #             sub_tokens.append[token[i]]
    #             j += 1
            
            
        

            


# identify operators and order of operations
    # higher order operators could be  flattened in place as they are found
        # option 1 -- one loop per operator one by one
        # option 2 -- a single loop that checks each token for needed operation
    # strings of nums to nums
        # [ 142, '+', 4, '*', 10, '+', '(', 4, '*', 5, ')' ]
    # look for opening '(' and matches ')' -- recursively invoke
        # [ 142, '+', 4, '*', 10, '+', '(', 4, '*', 5, ')' ]
        # calc [ 4, '*', 5, ] => [ 20 ] => [ 142, '+', 4, '*', 10, '+', 20 ]
    # higher order ops first (* /)
        #  [ 142, '+', 4, '*', 10, '+', 20 ] =>  [ 142, '+', 20 '+', 20 ]
    # lower order ops (+ /)
        # [ 142, '+', 20 '+', 20 ] => [ 182 ]
    # only one item in the list, we are done

# Order of operations
    #  P E M D A S
    # () ^ * / + -


# print ("Welcome to the lexer!")

# while True: 
#     text = input(">")

