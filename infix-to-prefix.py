
def isOperator(c): 
    if (c.isalpha() or c.isdigit()):
        return False
    return True

def getPriorty(c): 
    if(c== '+' or c =='-'):
        return 1
    if (c=='*' or c == '/'):
        return 2
    if(c=='^'):
        return 3 
    return 0

def infixToPrefix(expression): 
    operands = [] 
    operators =[] 
    new = expression.replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ').replace('^', ' ^ ').replace('(', ' ( ').replace(')', ' ) ') #adding spaces before and after each operator
    s = [i for i in new.split(' ') if i != '']
    for c in s[::-1]: 
        if (not isOperator(c) and c!=' '):
            operands.append(c)       
        elif(c == ')'):
            operators.append(c)
        
        elif(c=='('):
            while operators[-1] !=')':
                operands.append(operators.pop())
            operators.pop()
        
        else:
            while operators and getPriorty(operators[-1]) > getPriorty(c):
                operands.append(operators.pop())
            operators.append(c)
        
    while operators:
        operands.append(operators.pop())
    
    return ' '.join(operands[::-1])

def evaluation(prefix): 
    s = []
    tokens = prefix.split(' ')
    for c in tokens[::-1]:
        if (not isOperator(c)):
            s.append(int(c))
        else:
            o1=s.pop()
            o2=s.pop()
            if c=='+':
                s.append(o1+o2)
            if c=='-':
                s.append(o1-o2)
            if c=='*':
                s.append(o1*o2)
            if c=='/':
                s.append(o1//o2)
            if c=='^':
                s.append(o1**o2)
    return s.pop()




infix ='5+12-3+(3*4)'
prefix =infixToPrefix(infix)
evaluation = evaluation(prefix)

print(f"The prefix expression for '{infix}' is: '{prefix}'")
print(f"The evaluation for the prefix expression is: {evaluation}")




        
    

        
            