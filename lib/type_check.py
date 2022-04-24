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
