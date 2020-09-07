def exec_oper(a, b, oper):
    if oper == '+':
        return a + b
    if oper == '-':
        return a - b
    if oper == '/':
        return a / b
    if oper == '*':
        return a * b
    raise Exception('Operation is not defined')

def check_literal(literals):
        if literals.last == literals.current:
            raise Exception('Two numbers in a row are forbidden'
                if literals.current == 'num'
                else 'Two operators in a row are forbidden')
        literals.last = literals.current

def add_number(nums, number):
    check_literal('num')
    if number:
        nums.append(int(number))
            

def calc(expr):
    nums, opers = [], []

    curr_num = ''
    last_literal = '' # num or oper
    

    for c in expr:
        c = ord(c)
        if c == 32:
            add_number()
            if curr_num:
                last_literal = check_literal(last_literal, 'num')
                nums.append(int(curr_num))
                curr_num = ''
            continue
        if c in range(48, 58):
            curr_num += chr(c)
        elif c in [42, 43, 45, 47]:
            if curr_num:
                if last_literal == 'num':
                    raise Exception('Two numbers in a row are forbidden')
                nums.append(int(curr_num))
                curr_num = ''
                last_literal = 'num'
            if last_literal == 'oper':
                    raise Exception()
            opers.append(chr(c))
            last_literal = 'oper'
        else:
            print('Expression contains invalid characters')
            break
    
    if curr_num:
        nums.append(int(curr_num))

    print('Initial expression: %s' % expr)
    print('Numbers list: %s' % nums)
    print('Operators list: %s' % opers)



# expr = input('Type the expression: ')
calc('11 + 2 * 30')
