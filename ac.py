from queue import Queue
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
        node = q.get() # blue link of this node is already set
        assert node.blue != None
        for ch in node.kids:
            x = node.blue
            while ch not in x.kids:
                if x is root:
                    break
                x = x.blue
            if ch in x.kids:
                node.kids[ch].blue = x.kids[ch]
            else:
                node.kids[ch].blue = root
            q.put(node.kids[ch])

    return root

def print_tree_edges(node):
    if node.flag:
        print('%s [color=red];' % id(node))
    if node.blue != None:
        print('%s -> %s [color=blue];' % (id(node), id(node.blue)))
    for ch in node.kids:
        print('%s -> %s [color=black,label=%s];' % (id(node), id(node.kids[ch]), ch))
        print_tree_edges(node.kids[ch])

def print_tree(root):
    print('digraph test {')
    print_tree_edges(root)
    print('}')

words = ['a','ab','bab','bc','bca','c','caa', 'cd']
tree = build_tree(words)
print_tree(tree)
