from Tkinter import Tk, Canvas, mainloop

import numpy as np


class Node:
    def __init__(self):
        self.node_id = -1

    def create(self, node_id, n_samples, split_dim, split_thresh):
        self.node_id = node_id
        self.is_leaf = False
        self.n_samples = n_samples
        self.split_dim = split_dim
        self.split_thresh = split_thresh

    def create_leaf(self, node_id, n_samples, split_dim, split_thresh, mean, covar):
      self.create(node_id, n_samples, split_dim, split_thresh)
      self.is_leaf = True
      self.mean = mean
      self.covar = covar


def read_node(f, print_leaves=False):
    n = Node()
    node_id = int(f.readline())
    is_leaf = int(f.readline())
    n_samples = int(f.readline())
    split_dim = int(f.readline())
    split_thresh = float(f.readline())
    if is_leaf:
        mean = list(f.readline())
        covar = list(f.readline())
        samples = list(f.readline())
        n.create_leaf(node_id, n_samples, split_dim, split_thresh, mean, covar)
        if print_leaves:
            print "%i: %i"%(node_id, n_samples)
    else:
        n.create(node_id, n_samples, split_dim, split_thresh)

    return n


def read_tree(f, print_leaves=False):
    f.readline()
    tree_id = int(f.readline())
    depth = int(f.readline())
    n_nodes = int(f.readline())
    n_leaves = int(f.readline())

    nodes = {}
    for n in range(n_nodes):
        node = read_node(f, print_leaves)
        nodes[node.node_id] = node
    return nodes


def read_forest(file, t=0):
    f = open(file, 'r')

    n_trees = f.readline()
    n_dim_in = f.readline()
    n_dim_out = f.readline()

    # go through trees that we don't want to read
    for tr in range(t):
        read_tree(f)

    nodes = read_tree(f, True)

    f.close()
    return nodes


def draw_circle(w, x, y, r = 10):
    if r > 20:
        r = 20;
    w.create_oval(x-r, y-r, x+r, y+r, fill='#dddddd')


def draw_node(w, node, tree_w, level_h, r = 10):
    depth = 0
    if (node.node_id > 0): depth = np.floor(np.log2(node.node_id + 1.1))
    n_nodes = pow(2, depth) # nodes at this depth
    node_dist = tree_w/(n_nodes+1)

    n = node.node_id + 1 - n_nodes # number of nodes on the left

    y = (level_h/2) + (depth*level_h)
    x = node_dist + n*node_dist
    draw_circle(w, x, y, node_dist/2)
    text_color = 'black'
    if node.is_leaf: text_color = '#00bb00'
    if depth < 7:
        w.create_text(x, y, text=node.n_samples, fill=text_color, font='Consolas, 7')


def draw_binary_tree(depth, nodes):
    tree_w = 128*depth	# tree width
    level_h = 75	# level height

    master = Tk()
    w = Canvas(master, width=tree_w, height=tree_w + level_h/2)
    w.pack()

    for node in nodes.values():
        draw_node(w, node, tree_w, level_h)

    mainloop()


if __name__ == '__main__':
    draw_binary_tree(9, read_forest('dummy.data', 0))
