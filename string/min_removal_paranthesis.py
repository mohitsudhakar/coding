
def func(string):

    string = list(string)
    stack = []
    for i,s in enumerate(string):
        if s == '(':
            stack.append(i)
        else:
            if not stack:
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                else:
                    string[i] = "*"

    print(string, stack)
    while stack:
        i = stack.pop()
        string.pop(i)
    

if __name__ == '__main__':

    S = "()())()"

    func(S)