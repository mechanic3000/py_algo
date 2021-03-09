"""
2. Закодировать любую строку по алгоритму Хаффмана.


Не доделано!
"""
from collections import Counter
from collections import deque

class Node():
    def __init__(self, freq=None, left=None, right=None):
        self.left = left  # левая часть
        self.right = right  # правая часть
        self.freq = freq


    # def __repr__(self):
    #     return self.left or self.right

class HaffmanHash:
    def __init__(self):
        self.string = ''
        self.que = deque()

    def _sort(self):
        for i, item in enumerate(self.que):
            for j, sub_item in enumerate(self.que):
                if item.freq < sub_item.freq:
                    self.que[i], self.que[j] = self.que[j], self.que[i]

    def make(self, string):
        self.string = Counter(string)  #  .most_common()[::-1]
        for k, v in self.string.items():
            self.que.append(Node(v, k))
        self._sort()
        while len(self.que) > 1:
            item_1 = self.que.popleft()
            item_2 = self.que.popleft()

            if item_1.freq < item_2.freq:
                self.que.append(Node(item_1.freq + item_2.freq, item_1.left, item_2.right))
            else:
                self.que.append(Node(item_1.freq + item_2.freq, item_2.left, item_1.right))

        return self.que


hh = HaffmanHash()
print(hh.make("beep boop beer!"))
