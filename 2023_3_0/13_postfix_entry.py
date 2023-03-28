class Stack:

    def __init__(self):
        self.stack = []

    def clear(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop()
        return removed

    def back(self):
        if len(self.stack) == 0:
            return None
        return self.stack[len(self.stack)-1]

    def print_stack(self):
        print(self.stack)


def postfix_result(entry):
    stack = Stack()

    for pos in entry:
        if pos == '+':
            a = stack.pop()
            b = stack.pop()
            stack.push(a + b)
        elif pos == '-':
            a = stack.pop()
            b = stack.pop()
            stack.push(b - a)
        elif pos == '*':
            a = stack.pop()
            b = stack.pop()
            stack.push(a * b)
        else:
            stack.push(int(pos))

    return stack.pop()


if __name__ == '__main__':
    reader = open('input.txt', 'r')
    entry = reader.readline().split()
    reader.close()

    # print(entry)
    print(postfix_result(entry))
