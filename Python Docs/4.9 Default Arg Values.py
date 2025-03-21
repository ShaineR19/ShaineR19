def ask_ok(prompt, retries=4, reminder='Please try again!'):
    answer = True
    while answer:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return answer
        if reply in {'n', 'no', 'nop', 'nope'}:
            answer = False
            return answer
        retries = retries -1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

ask_ok('Do you really want to quit?(yes/no): ')
ask_ok('OK to overwrite the file?(yes/no): ', 2)
ask_ok('OK to overwrite the file?(yes/no): ', 2, 'Come on, only yes or no! ')