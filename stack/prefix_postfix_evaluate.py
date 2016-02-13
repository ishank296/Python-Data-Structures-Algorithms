'''
Evaluation of prefix and postfix expressions

INFIX: a * b + c * d - e = [(a * b) + (c * d)] - e
POSTFIX: ab*cd*+e-
PREFIX: -+*ab*cde
'''

import stack
import operator
def evaluate_postfix(postfix_exp):
    s = stack.Stack()
    ans = 0
    operands=['1','2','3','4','5','6','7','8','9','0']
    operators = {
                '+':operator.add,
                '-':operator.sub,
                '*':operator.mul,
                '/':operator.div
                }
    for elem in postfix_exp:
        if elem in operands:
            s.push(int(elem))
        else:
            if elem in operators:
                op2 = s.pop()
                op1 = s.pop()
                ans = operators[elem](op1,op2)
                s.push(ans)
            else:
                print 'iinvalid token'
    if len(s)>1:
            print "invalid expression"
    else:
        print s.pop()

def evaluate_prefix(exp):
    evaluate_postfix(exp[::-1])


if __name__=='__main__':
    evaluate_postfix('54*23*+9-')
    evaluate_prefix('-+*54*239')
