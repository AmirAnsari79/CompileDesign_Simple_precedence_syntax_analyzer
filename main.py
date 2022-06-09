from prettytable import PrettyTable

"""
This is a program for checking incoming strings
This program checks whether the string belongs to Grammar S -> aSSb|c  or not
"""

# table
diction = {
    'S': {'S': '=.', 'a': '<.', 'b': '=.', 'c': '<.', '$': ''},
    'a': {'S': '=.', 'a': '<.', 'b': '', 'c': '<.', '$': ''},
    'b': {'S': '', 'a': '<.', 'b': '', 'c': '<.', '$': ''},
    'c': {'S': '', 'a': '.>', 'b': '.>', 'c': '.>', '$': '.>'},
    '$': {'S': '', 'a': '<.', 'b': '', 'c': '<.', '$': ''},
}

# stack
stack = list('$')

# input string and generate to list
input_stack = input(' inp: ')
input_stack = [i for i in input_stack]
input_stack.append('$')

# initialize table for show
table = PrettyTable(border=True, header=True, padding_width=15)
table.field_names = ["Stack", "input_string", "output"]

# flag for check
flag = True

# first check if acb in input
if 'a' not in input_stack or 'c' not in input_stack or 'b' not in input_stack or input_stack[0] != 'a' or input_stack[
    -2] != 'b':
    print('ERROR')
    flag = False
# this while for checking condition
while flag:

    # check if <.assb in stack and shift
    if stack[-5:] == ['<.', 'a', 'S', 'S', 'b']:
        for i in range(5):
            stack.pop(-1)
        stack.append('S')
        table.add_row([''.join(stack), ''.join(input_stack), "Shift"])

    # check this column contains <. SYMBOL and shift
    elif diction[stack[-1]][input_stack[0]] == '<.':
        stack.extend(['<.', input_stack[0]])
        input_stack.pop(0)
        table.add_row([' '.join(stack), ' '.join(input_stack), "Shift"])

    # check this column contains =. SYMBOL and shift
    elif diction[stack[-1]][input_stack[0]] == '=.':
        stack.append(input_stack[0])
        input_stack.pop(0)
        table.add_row([' '.join(stack), ' '.join(input_stack), "Shift"])

    # check this column contains .> SYMBOL and Reduce
    elif diction[stack[-1]][input_stack[0]] == '.>':
        stack.append(input_stack[0])
        for item in reversed(stack):
            if item == '<.':
                stack.pop()
                break
            else:
                stack.pop()
        stack.append('S')
        table.add_row([' '.join(stack), ' '.join(input_stack), "Reduce"])

    # last check if len is correct and stack & input are match else ERROR
    elif len(input_stack) == 1:
        if len(stack) == 2 and stack == ['$', 'S']:
            print(table)
            print('\n\n OK')
            flag = False
        else:
            print('ERROR')
            flag = False
