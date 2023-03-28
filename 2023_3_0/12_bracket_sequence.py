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


def check_sequence(sequence):
    stack = Stack()
    for s in sequence:
        if s in '[{(':
            stack.push(s)
        elif s in ']})':
            if stack.size() == 0:
                return 'no'
            elif stack.back() == '[' and s == ']':
                stack.pop()
            elif stack.back() == '{' and s == '}':
                stack.pop()
            elif stack.back() == '(' and s == ')':
                stack.pop()
            else:
                return 'no'
    if stack.size() == 0:
        return 'yes'
    return 'no'


if __name__ == '__main__':
    reader = open('input.txt', 'r')
    sequence = reader.readline().strip()
    reader.close()

    print(check_sequence(sequence))

