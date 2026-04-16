class PriorityQueue:
    def __init__(self):
        self.A = [None]
        self.heap_size = 0

    def parent(self, i):
        return i // 2

    def left(self, i):
        return 2 * i

    def right(self, i):
        return 2 * i + 1

    def min_heapify(self, i):
        l = self.left(i)
        r = self.right(i)

        if l <= self.heap_size and self.A[l].frequency < self.A[i].frequency:
            smallest = l
        else:
            smallest = i

        if r <= self.heap_size and self.A[r].frequency < self.A[smallest].frequency:
            smallest = r

        if smallest != i:
            self.A[i], self.A[smallest] = self.A[smallest], self.A[i]
            self.min_heapify(smallest)

    def heap_minimum(self):
        if self.heap_size < 1:
            raise IndexError("heap index out of range")
        return self.A[1]

    def pop(self):
        if self.heap_size < 1:
            raise IndexError("heap index out of range")

        minimum = self.A[1]
        self.A[1] = self.A[self.heap_size]
        self.A.pop()
        self.heap_size -= 1

        if self.heap_size >= 1:
            self.min_heapify(1)

        return minimum

    def decrease_key(self, i, key):
        if key.frequency > self.A[i].frequency:
            raise IndexError("heap index out of range")

        self.A[i] = key

        while i > 1 and self.A[self.parent(i)].frequency > self.A[i].frequency:
            p = self.parent(i)
            self.A[i], self.A[p] = self.A[p], self.A[i]
            i = p

    def insert(self, key):
        self.heap_size += 1
        self.A.append(Node())
        self.decrease_key(self.heap_size, key)


class Node:
    def __init__(self, char=None, frequency=float('inf')):
        self.frequency = frequency
        self.value = char
        self.left = None
        self.right = None


def encode_huffman(content):
    chars_and_frequency = {} # частота символов

    for char in content:
        if char not in chars_and_frequency.keys():
            chars_and_frequency[char] = 1
        else:
            chars_and_frequency[char] += 1

    n = len(chars_and_frequency.keys())

    queue = PriorityQueue()

    for char, frequency in chars_and_frequency.items():
        queue.insert(Node(char, frequency))

    # структура как в CLRS
    for i in range(n - 1):
        z = Node()
        x = queue.pop()
        y = queue.pop()
        z.left = x
        z.right = y
        z.frequency = x.frequency + y.frequency
        queue.insert(z)

    return queue.pop()


def decode_huffman(content, root):
    decoded = ''
    current = root

    # если задано пустое дерево
    if root is None:
        return decoded

    # если дерево состоит из одного узла, то это один символ
    if root.left is None or root.right is None:
        return root.value * len(content)

    for bit in content:
        if bit == '0':
            current = current.left
        else:
            current = current.right

        # если наследников нет, то мы дошли до нужного символа
        if current.left is None and current.right is None:
            decoded += current.value
            current = root

    return decoded


def get_codes(root):
    codes = {}

    def dfs(node, path):
        if node is None:
            return

        if node.left is None and node.right is None:
            codes[node.value] = path if path != '' else '0' # '0' если путь не успел составиться, а значение уже найдено
            return

        dfs(node.left, path + '0')
        dfs(node.right, path + '1')

    dfs(root, '')
    return codes

root = encode_huffman("длинношеее")

print(get_codes(root))
# {'н': '00', 'д': '010', 'л': '011', 'е': '10', 'и': '110', 'ш': '1110', 'о': '1111'}

print(decode_huffman("010011110000011111110101010", root))
# длинношеее