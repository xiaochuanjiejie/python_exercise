#-*- coding: utf-8 -*-

def is_operation(oper):
    if oper == '+' or oper == '-' or oper == '*' or oper == '/':
        print 'True'
        return True
    else:
        print 'False'
        return False

def mixed_operation (exp):
    exp_list = list(exp)
    print exp_list,'***'
    temp = ''
    behavor_list = []
    i = 0
    length = len(exp_list)
    print length
    for item in exp_list:
        print item,'-',type(item)
        if is_operation(item):
            behavor_list.append(int(temp))
            behavor_list.append(item)
            temp = ''
        else:
            temp += item
            print temp,'--'
        if i == length - 1:
            behavor_list.append(int(temp))
            break;
        i += 1
    return behavor_list

print mixed_operation('12+23*4/2')

# cal a o b
def get_aob(a, o, b):
    if o == '+':
        return a + b
    elif o == '-':
        return a - b
    elif o == '*':
        return a * b
    elif o == '/':
        return a / b

# Calculation op1 and op2('*' and '/' or '+' and '-')
def cal_op1_op2(exp_list, op1, op2):
    if len(exp_list) == 1:
        return exp_list

    i = 0
    has_op = False
    for i in range(2, len(exp_list), 2):
        a = exp_list[i - 2]
        o = exp_list[i - 1]
        b = exp_list[i]
        if o == op1 or o == op2:
            has_op = True
            exp_list[i - 2] = get_aob(a, o, b)
            del exp_list[i]
            del exp_list[i - 1]
            break

    if has_op == False:
        return exp_list

    return cal_op1_op2(exp_list, op1, op2)

# cal exp
def cal_exp(exp_list):
    exp_list = cal_op1_op2(exp_list, '*', '/')
    exp_list = cal_op1_op2(exp_list, '+', '-')

    return exp_list[0]

while True:
    expre = raw_input('Enter your expression(0 to end):\n')
    if expre == '0':
        break

    result = mixed_operation(expre)
    print 'list result = ',
    print result
    print cal_exp(result)

print 'END'