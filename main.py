if __name__ == "__main__":
    from lib.tokenize import tokenize
    from lib.calc import calc

    QUIT_CHAR = 'q'
    history = []

    print("Welcome to the lexer!")
    print(f"Enter an expression or type {QUIT_CHAR} to exit") 

    while True: 
        text = input("> ")
        if text == QUIT_CHAR:
            print("Goodbye!")
            break
        tokens = tokenize(text)
        if not tokens: continue
        history.append(text)
        result = calc(tokens)
        print(result)

