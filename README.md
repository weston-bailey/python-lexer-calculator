# Lexer/Math Expression Evaluator

This is a command line program that evaluates mathmatical expressions according to PEMDAS.

* run `make` to start the program
* run `make test` to run the unit tests
* run `make debug` to start the pdb 
* run `make watch` to run the test suite with nodemon

Example usage:

Respected operators: `() ^ * / + -`

```shell
$ make
Welcome to the lexer!
Enter an expression or type q to exit
> 142 + 4 * 10 / 1 ^ 2 - 1
181.0
> (10 * (4 + 2))         
60
> q
Goodbye!
$
```



## Notes/Pseudocode

```python
# separate tokens from string
    # maybe toss them in a list
    # '142 + 4 * 10 + (4 * 5)' => [ '142', '+', '4', '*', '10', '+', '(', '4', '*', '5', ')' ]
        # will need to identify numbers, symbols and spaces (possibly invalid chars too)

# identify operators and order of operations
    # higher order operators could be  flattened in place as they are found
        # option 1 -- one loop per operator one by one -- this must be done to preserve the order of operations
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
```

## Todos

* [x] write some unit tests
* [x] add parens
* [x] make cli interface