##==========================================================================
## Swethan Sivasegaran
##==========================================================================
from stackqueue import Stack, Queue
from tree import OrderedTree

##==========================================================================
## Q1a:

## Start with an empty OrderedTree:
mytree = OrderedTree()

## Add steps here as necessary.
root_node = mytree.add_leaf(None, 42)
mytree.add_leaf(root_node, 7)
mytree.add_leaf(root_node, 8)
child_one = mytree.one_child(root_node, 0)
child_two = mytree.one_child(root_node, 1)
mytree.add_leaf(child_one, 3)
node_six = mytree.add_leaf(child_one, 6)
mytree.add_leaf(child_one, 5)
mytree.add_leaf(child_one, 4)
mytree.add_leaf(child_two, 9)
mytree.add_leaf(node_six, 11)
mytree.add_leaf(node_six, 12)
## When your solution is complete,
## this will show the diagram from the assignment.
print(mytree)

## This verifies that you haven't accidentally turned replaced mytree
## with an object of the wrong type.
assert type(mytree) == OrderedTree, "mytree is not an OrderedTree" 


##==========================================================================
## Q1b:

## stick(vals): Given a list of n integers, returns an ordered tree of n nodes
## such that each node has one child except the last node which has no children
## sticks: list[int] -> OrderedTree
##==========================================================================
def stick(vals: list[int]) -> OrderedTree:
    stick_tree = OrderedTree()
    length = len(vals)
    parent_node = None
    for i in range(length):
        value = vals[i]
        parent_node = stick_tree.add_leaf(parent_node, value)        
    return stick_tree
##==========================================================================
## Testing for Q1b:

## You may use these examples to help verify your code works:
##ans = stick([2,4,6,0,1])
##print(ans)

##empty = stick([])
##print(empty)
##==========================================================================


##==========================================================================
## Q1c:

## perfect_tree(d): Given an integer d, returns a perfect binary tree of
## depth d. The nodes are labelled from 0 to 2^(d+1) - 2 starting from the
## root and going down the tree left to right on each level.
## perfect_tree: int -> OrderedTree
##==========================================================================
def perfect_tree(d: int) -> OrderedTree:
    perfect_tree = OrderedTree()
    parent_list = Queue()
    if (d == 0):
        perfect_tree.add_leaf(None, 0)
    for i in range(d):
        if (i == 0):
            root = perfect_tree.add_leaf(None, 0)
            parent_list.enqueue(root)
        count = int(pow(2, i))
        for j in range (count):
            parent = parent_list.dequeue()
            value = (2* (perfect_tree.value(parent))) + 1
            child_one = perfect_tree.add_leaf(parent, value)
            value = value + 1
            child_two = perfect_tree.add_leaf(parent, value)
            parent_list.enqueue(child_one)
            parent_list.enqueue(child_two)
            
    return perfect_tree
##==========================================================================
## Testing for Q1c:

##t2 = perfect_tree(2)
# ## This verifies that you haven't accidentally created an object of
# ## the wrong type.
##assert isinstance(t2, OrderedTree), "t is not an OrderedTree"
##print(t2)

##t3 = perfect_tree(3)
##print(t3)
##==========================================================================
