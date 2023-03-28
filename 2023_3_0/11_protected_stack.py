class Stack:

    def __init__(self):
        self.stack = []

    def clear(self):
        self.stack = []
        print('ok')

    def size(self):
        return len(self.stack)

    def push(self, item):
        self.stack.append(item)
        print('ok')

    def pop(self):
        if len(self.stack) == 0:
            return 'error'
        removed = self.stack.pop()
        return removed

    def back(self):
        if len(self.stack) == 0:
            return 'error'
        return self.stack[len(self.stack)-1]

    def print_stack(self):
        print(self.stack)


if __name__ == '__main__':
    reader = open('input.txt', 'r')
    operators = []
    while True:
        line = reader.readline().split()
        if line == []:
            break
        else:
            operators.append(line)
    reader.close()

    stack = Stack()

    for oper in operators:
        if oper[0] == 'push':
            stack.push(oper[1])
        elif oper[0] == 'size':
            print(stack.size())
        elif oper[0] == 'back':
            print(stack.back())
        elif oper[0] == 'pop':
            print(stack.pop())
        elif oper[0] == 'clear':
            stack.clear()
        elif oper[0] == 'exit':
            print('bye')
            break

    # print(operators)
