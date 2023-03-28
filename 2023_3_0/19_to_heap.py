class Heap:
    def __init__(self):
        self.heap = []

    def insert(self, k):
        size = len(self.heap)
        self.heap.append(k)
        while size > 0 and self.heap[size] > self.heap[(size-1)//2]:
            [self.heap[size], self.heap[(size-1)//2]] = [self.heap[(size-1)//2], self.heap[size]]
            size = (size - 1)//2

    def extract(self):
        if len(self.heap) == 0:
            return None
        extracted = self.heap[0]
        self.heap[0] = self.heap[-1]
        pos = 0
        while pos*2+1<len(self.heap)-1:
            max_son_pos = pos*2+1
            if self.heap[pos*2+2] > self.heap[max_son_pos]:
                max_son_pos = pos*2+2
            if self.heap[pos] < self.heap[max_son_pos]:
                self.heap[pos], self.heap[max_son_pos] = \
                    self.heap[max_son_pos], self.heap[pos]
                pos = max_son_pos
            else:
                break
        self.heap.pop()
        return extracted

    def print_heap(self):
        print(self.heap)


if __name__ == '__main__':
    reader = open('input.txt', 'r')

    operators = []
    n = int(reader.readline())
    for i in range(n):
        line = [*map(int, reader.readline().split())]
        if line == []:
            break
        else:
            operators.append(line)

    reader.close()

    # print(operators)
    heap = Heap()
    for oper in operators:
        if oper[0] == 0:
            heap.insert(oper[1])
        else:
            print(heap.extract())

    # heap.print_heap()

