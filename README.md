draw_tree
=========
A small script to plot binary trees created by a (regression) random forest

maciej.gryka@gmail.com

The script needs a text file that describes a tree. This text file should contain parameters as specified below, each on a separate line.

The first three numbers describe the forest as a whole - how many trees there are and how many input and output dimensions there are. 

Each tree has an ID, depth, overall number of nodes and number of leaves. 

Each node is described with an id, leaf status (1 for leaf, 0 for non-leaf), number of samples at the node and split parameters: split dimension and threshold. In the case of leaf nodes there's also information about label mean and covariance, but it's not needed for plotting.

dummy.data is a sample file that uses 888 for all split parameterss and 444 for all leaf parameters.

Example format, also in dummy.data (the file should have just the numbers, without comments):

1   # number of trees in the forest
1   # number of input dimensions
1   # number of output dimensions
    # empyt line (required)
0   # tree ID
3   # tree depth
11  # number of nodes in the tree
6   # number of leaves in the tree
0   # node ID
0   # is_leaf (1 if this node is a leaf node, 0 otherwise)
100 # number of samples at this node
888 # split dimension
888 # split threshold
2   # node ID
0   # is_leaf
50  # samples
888 # split params
888
3   # node ID
1   # this is a leaf
25  
888 # split params
888
444 # leaf params
444
444
.
.
.
