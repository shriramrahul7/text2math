

def evalute(exp):
    
    stack = [];

    for c in exp[::-1]:

        if c.isdigit():
            stack.append(c)
        else :

            if len(stack) >= 2:
                op1 = int(stack.pop())
                op2 = int(stack.pop())
                if c == '+':
                    result = op2 + op1
                elif c == '-':
                    result = op2 - op1
                elif c == '*':
                    result = op2 * op1
                elif c == '/':
                    result = op1 / op2
                else : 
                    print('invalid character')
                    break

            else : 
                

            stack.append(result)

    final = stack.pop()

    return final

if __name__ == "__main__":
    expression = "+5+61"
    print(evalute(expression))
            