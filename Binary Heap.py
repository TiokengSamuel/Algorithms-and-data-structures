# binary heap
# heap list 1
class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    # listing 2
    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] == self.heapList[i]

                self.heapList[i] = tmp
                i = i // 2
