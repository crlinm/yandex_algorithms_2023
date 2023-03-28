class Queue:

    def __init__(self):
        self.queue = []

    def size(self):
        return len(self.queue)

    def front(self):
        if len(self.queue) == 0:
            return 'error'
        return self.queue[0]

    def push(self, item):
        self.queue.append(item)
        print('ok')

    def pop(self):
        if len(self.queue) == 0:
            return 'error'
        removed = self.queue[0]
        self.queue = self.queue[1:]
        return removed

    def clear(self):
        self.queue = []
        print('ok')

    def print_queue(self):
        print(self.queue)


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

    queue = Queue()

    for oper in operators:
        if oper[0] == 'push':
            queue.push(oper[1])
        elif oper[0] == 'size':
            print(queue.size())
        elif oper[0] == 'front':
            print(queue.front())
        elif oper[0] == 'pop':
            print(queue.pop())
        elif oper[0] == 'clear':
            queue.clear()
        elif oper[0] == 'exit':
            print('bye')
            break
