if __name__ == "__main__":
    from lib.tokenize import tokenize
    from lib.calc import calc

    QUIT_CHAR = 'q'

    print("Welcome to the lexer!")
    print(f"Enter an expression or type {QUIT_CHAR} to exit") 

    while True: 
        text = input("> ")
        if (text == QUIT_CHAR): break
        tokens = tokenize(text)
        result = calc(tokens)
        print(result)

