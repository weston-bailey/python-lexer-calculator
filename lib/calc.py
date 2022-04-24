# splitting calculations into sep functions so it can recurse
def calc(tokens):
    '''
        flattens list of tokens down to single value
    '''
    # going to have one loop per operator
    # because -- how can you add unless you know that all parens are taken care of

    # ## # ## #
    # parenthsis
    print(tokens)
    i = 0
    stop = len(tokens)
    while i < stop:
        if tokens[i] == '(':
            # build list to recursively invoke
            sub_tokens = [i]

            # start one after i, since i is a '('
            j = i + 1
            # the problem is, when parens are nested (4 * (2 + 3))
            # the first paran '3)' is matched and the second paren is not passed to the recursion 4 * (2 + 3
            # when it should be  4 * (2 + 3)
            # keep track if another opening parens '(' is encountered
            matches = 1
            while matches > 0:
                print('j', j, tokens[j], len(tokens))
                # print(tokens)
                sub_tokens.append(tokens[j])
                if tokens[j] == '(':
                    matches = matches + 1
                elif tokens[j] == ')':
                    matches = matches - 1
                j += 1
            
            print(sub_tokens)
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