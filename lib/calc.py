# splitting calculations into sep functions so it can recurse
from soupsieve import match


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
            # the amount of closing parans needed to match
            matches = 1
            while matches > 0:
                if tokens[j] == ')':
                    matches = matches - 1
                    if matches == 0: break
                if tokens[j] == '(':
                    matches += 1
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

    # multiplacation / division
    i = 0
    while i < len(tokens):
        if tokens[i] == '*':
            prod = tokens[i - 1] * tokens[i + 1]
            tokens = tokens[:i - 1] + [prod] + tokens[i + 2:]
            i = i - 1
        if tokens[i] == '/':
            div = tokens[i - 1] / tokens[i + 1]
            tokens = tokens[:i - 1] + [div] + tokens[i + 2:]
            i = i - 1
        i += 1

    # division
    # i = 0
    # while i < len(tokens):
    #     if tokens[i] == '/':
    #         div = tokens[i - 1] / tokens[i + 1]
    #         tokens = tokens[:i - 1] + [div] + tokens[i + 2:]
    #         i = i - 1
    #     i += 1

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
