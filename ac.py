from queue import Queue
import sys

class Node:
    def __init__(self):
        self.kids = {}
        self.blue = None
        self.green = None
        self.flag = False

def build_tree(words):
    root = Node()
    for word in words:
        node = root
        for ch in word:
            if ch not in node.kids:
                node.kids[ch] = Node()
            node = node.kids[ch]
        node.flag = True

    q = Queue()
    for kid in root.kids.values():
        kid.blue = root
        q.put(kid)
    while not q.empty():
        node = q.get() # blue and green link of this node is already set
        assert node.blue != None
        for ch in node.kids:
            x = node.blue
            while ch not in x.kids:
                if x is root:
                    break
                x = x.blue
            if ch in x.kids:
                node.kids[ch].blue = x.kids[ch]
                if x.kids[ch].flag:
                    node.kids[ch].green = x.kids[ch]
                elif x.kids[ch].green != None:
                    node.kids[ch].green = x.kids[ch].green
            else:
                node.kids[ch].blue = root
            q.put(node.kids[ch])

    return root

def print_tree_edges(node):
    if node.flag:
        print('%s [color=red];' % id(node))
    if node.blue != None:
        print('%s -> %s [color=blue];' % (id(node), id(node.blue)))
    if node.green != None:
        print('%s -> %s [color=green];' % (id(node), id(node.green)))
    for ch in node.kids:
        print('%s -> %s [color=black,label=%s];' % (id(node), id(node.kids[ch]), ch))
        print_tree_edges(node.kids[ch])

def print_tree(root):
    print('digraph test {')
    print_tree_edges(root)
    print('}')

def run_tree(root, s):
    res = []
    node = root
    for i in range(len(s)):
        ch = s[i]

        while ch not in node.kids:
            if node is root:
                break
            node = node.blue

        if ch in node.kids:
            node = node.kids[ch]

        x = node
        while True:
            if x.flag:
                res.append((id(x), i))
            if not x.green:
                break
            x = x.green

    return res

words = ['a','ab','bab','bc','bca','c','caa']
tree = build_tree(words)

cmd = 'draw'
try:
    cmd = sys.argv[1]
except:
    pass

if cmd == 'draw':
    print_tree(tree)
elif cmd == 'test':
    res = run_tree(tree, input())
    print(res)
