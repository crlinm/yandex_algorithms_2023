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


def wagon_sorting(wagons):
    stack = Stack()
    order = []
    k = 0

    # stack.push(wagons[0])
    for i in range(0, len(wagons)):
        w = wagons[i]
        while stack.size() > 0 and k + 1 == stack.back():
            order.append(stack.pop())
            k += 1
        else:
            stack.push(w)

    while stack.size() > 0:
        if k + 1 == stack.back():
            order.append(stack.pop())
            k += 1
        else:
            return 'NO'

    # stack.print_stack()

    # print(order)
    return 'YES'


if __name__ == '__main__':
    reader = open('input.txt', 'r')
    n = int(reader.readline())
    wagons = [*map(int, reader.readline().split())]
    reader.close()

    # print(n)
    # print(wagons)

    print(wagon_sorting(wagons))

