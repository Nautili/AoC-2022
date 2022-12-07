import sys

class Node:
    def __init__(self, is_dir=False, size=0):
        self.nodes = {}
        self.parent = None
        self.is_dir = is_dir
        self.size = size

    def add_node(self, node, key):
        self.nodes[key] = node
        node.parent = self

    def get_size(self):
        return self.size + sum(node.get_size() for node in self.nodes.values())

def build_dirs(lines):
    root = Node(is_dir=True)
    for i in range(len(lines)):
        cur_line = lines[i]

        if cur_line.startswith("$ cd"):
            dest = cur_line.split()[2]
            if dest == "..":
                cur_dir = cur_dir.parent
            elif dest != "/":
                cur_dir = cur_dir.nodes[dest]
            else:
                cur_dir = root
            
        elif cur_line.startswith("$ ls"):
            while i + 1 < len(lines) and not lines[i + 1].startswith("$"):
                i += 1
                cur_line = lines[i]
                new_node = cur_line.split()
                if new_node[0] == "dir":
                    cur_dir.add_node(Node(is_dir=True), new_node[1])
                else:
                    cur_dir.add_node(Node(size=int(new_node[0])), new_node[1])
    return root

def get_dir_sizes(root):
    sizes = [root.get_size()]
    for node in root.nodes.values():
        if node.is_dir:
            sizes.extend(get_dir_sizes(node))
    return sizes

def get_total_under(dirs, max_size):
    return sum(size for size in dirs if size < max_size)

def smallest_greater_than(l, min_size):
    return min(size for size in l if size > min_size)

def main():
    with open(sys.argv[1]) as f:
        lines = [line.strip() for line in f.readlines()]
        dirs = build_dirs(lines)
        dir_sizes = (get_dir_sizes(dirs))
        print(get_total_under(dir_sizes, 100000))
        print(smallest_greater_than(dir_sizes, dirs.get_size() - 40000000))

if __name__ == '__main__':
    main()