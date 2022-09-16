class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, elem):
        self.stack.append(elem)

    def pop(self):
        if not(self.is_empty()):
            index_num = len(self.stack) - 1
            return self.stack.pop(index_num)
        else:
            return 'Error Empty stack'

    def peek(self):
        if not(self.is_empty()):
            index_num = len(self.stack) - 1
            return self.stack[index_num]
        else:
            return 'Error Empty stack'

    def size(self):
        if not(self.is_empty()):
            return len(self.stack)
        else:
            return 0

def balanced_check(str, stack_in:Stack, stack_out:Stack):
    pairs = {'(': ')', '{':'}', '[':']'}
    b_true = 'balanced'
    b_false = 'not balanced'
    opennings = ['(', '{', '[']

    for elem in str:
        stack_in.push(elem)

    if stack_in.is_empty():
        print('balanced')
        return b_true
    elif stack_in.size() % 2 > 0:
        print('not balanced')
        return b_false
    elif stack_in.peek() in opennings:
        print('not balanced')
        return b_false

    while not stack_in.is_empty():
        popped = stack_in.pop()

        if popped in opennings:
            if pairs[popped] != stack_out.pop():
                print('not balanced')
                return b_false
        else:
            stack_out.push(popped)

    if stack_out.is_empty():
        print('balanced')
        return b_true
    else:
        print('not balanced')
        return b_false



if __name__ == '__main__':
    myStack = Stack()
    print(f'{myStack.is_empty()}')
    print(f'{myStack.size()}')
    myStack.push(100)
    myStack.push(5)
    myStack.push(10)
    myStack.push(25)
    myStack.push(4)
    myStack.push(-1)
    myStack.push(10)
    print(f'{myStack.size()}')
    print(f'{myStack.peek()}')
    print(f'{myStack.pop()}')
    print(f'{myStack.pop()}')
    print(f'{myStack.size()}')
    print(f'{myStack.stack}')
    test_str = '([{}])[]'
    test_str_= '([{}])(({]))'
    print()
    print()
    print('balanced check..')
    balanced_check(test_str, Stack(), Stack())
    balanced_check(test_str_, Stack(), Stack())

