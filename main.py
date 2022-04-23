# lexer calculator

# input '142 + 4 * 10 + (4 * 5)'
text = '142 + 4 * 10 + (4 * 5)'

def tokenize(string):
    # perform the split
    tokens = []
    current_string = ''
    for char in string:
        if char == '(' or char == ')':
            # closing ')' will have value before them
            if current_string:
                tokens.append(current_string)
                current_string = ''
            # add the '(' or ')'
            tokens.append(char)
        elif char == ' ' and current_string != '':
            # is there is a space and a value we can assume a value has finished
            tokens.append(current_string)
            current_string = ''
        else:
            current_string += char
    
    return tokens

split = tokenize(text)

# separate tokens from string
    # maybe toss them in a list
    # '142 + 4 * 10 + (4 * 5)' => [ '142', '+', '4', '*', '10', '+', '(', '4', '*', '5', ')' ]
        # will need to identify numbers, symbols and spaces (possibly invaldis chars too)

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

