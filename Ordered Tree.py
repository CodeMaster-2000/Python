##==========================================================================
## Swethan Sivasegaran (20798865)
## CS 234 Spring 2023
## Assignment 4 Question 1
##==========================================================================
from tree import OrderedTree
from contiguous import Contiguous

##==========================================================================
## treeify(c): Given a Contiguous, returns a (2,3) tree of minimum depth and
## having equal children if possible with regards to size. Otherwise, make
## furthest-left children largest first.
## treeify: Contiguous -> OrderedTree
## Requires: c contains int values and is sorted in increasing order
def treeify(c: Contiguous) -> OrderedTree:
    """In O(n), create a minimum-depth (2-3) tree containing all the
    values in c.
    
    Requires: c contains int values and is sorted in increasing order.
    """
    tree = OrderedTree()
    last_index = c.size()-1
    if (last_index != -1):
        treeify_recurse(c, tree, None, 0, last_index)
    return tree

##==========================================================================
def treeify_recurse(c: Contiguous, t: OrderedTree, parent, start, end) -> None:
    num_of_nodes = end - start + 1
    upper_bound = 0
    count = 0
    if (num_of_nodes == 1):
        key = c.access(start)
        t.add_leaf(parent, key)
    elif (num_of_nodes == 2):
        key_one = c.access(start)
        key_two = c.access(end)
        t.add_leaf(parent, list[key_one, key_two])
    else:
        while (num_of_nodes >= upper_bound):
            count = count + 1
            upper_bound = pow(3, count)
        count = count - 1
        lower_bound = 2 * (pow(3, count))
        if (lower_bound > num_of_nodes):
            halfway = start + int (num_of_nodes/2)
            key = c.access(halfway)
            new_parent = t.add_leaf(parent, key)
            treeify_recurse(c, t, new_parent, start, halfway - 1)
            treeify_recurse(c, t, new_parent, halfway + 1, end)
        else:
            index_one = start + int(num_of_nodes/3)
            index_two = index_one + int(num_of_nodes/3)
            if ((index_two - index_one - 1) < (end - index_two)):
                index_two = index_two + 1
            key_one = c.access(index_one)
            key_two = c.access(index_two)
            new_parent = t.add_leaf(parent, list[key_one, key_two])
            treeify_recurse(c, t, new_parent, start, index_one - 1)
            treeify_recurse(c, t, new_parent, index_one + 1, index_two - 1)
            treeify_recurse(c, t, new_parent, index_two + 1, end)
##==========================================================================        
## You may use this function to help create tests.
def list_to_contiguous(vals: 'list[any]') -> Contiguous:
    """Create a Contiguous containing the items in vals."""
    c = Contiguous(len(vals))
    for i in range(len(vals)):
        c.store(i, vals[i])

    return c
##==========================================================================
## These should display the trees shown in the assignment:
print(treeify(list_to_contiguous([])))
print(treeify(list_to_contiguous(list(range(10,31)))))
print(treeify(list_to_contiguous(list(range(10,41)))))

