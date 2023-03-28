class Stack:

    def __init__(self):
        self.stack = []

    def clear(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def push(self, item, i):
        t = tuple([item, i])
        self.stack.append(t)

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


def cities_n(n, prices):

    cities = [-1 for _ in range(n)]
    stack = Stack()

    for i in range(n):
        if stack.size() > 0:
            if prices[i] > stack.back()[0]:
                stack.push(prices[i], i)
                # print('push ', prices[i], i)
            else:
                while stack.size() > 0 and stack.back()[0] > prices[i]:
                    t = stack.pop()
                    cities[t[1]] = i
                stack.push(prices[i], i)
                # print('else push ', prices[i], i)
        else:
            stack.push(prices[i], i)
            # print('else else push ', prices[i], i)

    # stack.print_stack()

    return cities


if __name__ == '__main__':
    reader = open('input.txt', 'r')
    n = int(reader.readline())
    prices = [*map(int, reader.readline().split())]
    reader.close()

    cities = cities_n(n, prices)
    for city in cities:
        print(city, end=' ')

