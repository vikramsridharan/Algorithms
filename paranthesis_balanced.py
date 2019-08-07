from Stack import Stack


def unbalanced_paranthesis(a):
    i = 0
    stack = Stack()
    for e in a:
        if e == '(':
            i = i + 1
            stack.push(i)
        if e == ')':
            if stack.is_empty():
                i = i + 1
                return ") at " + str(i) + " is unbalanced"
            else:
                stack.pop()

    if stack.is_empty():
        return "balanced"
    else:
        first = 0
        while ( not stack.is_empty()):
            first = stack.pop()
        return "( at " + str(first) + " is unbalanced"

a = "(((()()("
print(unbalanced_paranthesis(a))
