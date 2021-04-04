def eval_loop():
    stdin = input()
    while (stdin != 'done'):
        eval(stdin)
        stdin = input()

eval_loop()