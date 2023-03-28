class Deque:

    def __init__(self, n):
        self.deque = []
        self.n = n

    def size(self):
        return len(self.deque)

    def push_front(self, item):
        self.deque.insert(0, item)
        print('ok')

    def push_back(self, item):
        self.deque.append(item)
        print('ok')

    def pop_front(self):
        if len(self.deque) == 0:
            return 'error'
        removed = self.deque[0]
        self.deque = self.deque[1:]
        return removed

    def pop_back(self):
        if len(self.deque) == 0:
            return 'error'
        removed = self.deque.pop()
        return removed

    def back(self):
        if len(self.deque) == 0:
            return 'error'
        return self.deque[len(self.deque)-1]

    def front(self):
        if len(self.deque) == 0:
            return 'error'
        return self.deque[0]

    def clear(self):
        self.deque = []
        print('ok')

    def print_deque(self):
        print(self.deque)


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

    # print(operators)

    deque = Deque(100)

    for oper in operators:
        if oper[0] == 'push_front':
            deque.push_front(oper[1])
        elif oper[0] == 'push_back':
            deque.push_back(oper[1])
        elif oper[0] == 'pop_front':
            print(deque.pop_front())
        elif oper[0] == 'pop_back':
            print(deque.pop_back())
        elif oper[0] == 'front':
            print(deque.front())
        elif oper[0] == 'back':
            print(deque.back())
        elif oper[0] == 'size':
            print(deque.size())
        elif oper[0] == 'clear':
            deque.clear()
        elif oper[0] == 'exit':
            print('bye')
            break

