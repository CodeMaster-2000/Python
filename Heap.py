##==========================================================================
## Swethan Sivasegaran (20798865)
## CS 234 Spring 2023
## Assignment 4 Question 2
##==========================================================================
from contiguous import Contiguous

##==========================================================================
## heapify(c): Given a contiguous, treats it as a complete tree and returns
## it following heap order property
## heapify: Contiguous -> None
## Effects: Mutates c so that it follows heap order property in O(n) time
def heapify(c: Contiguous) -> None:
    """Mutate c so it contains a heap, in O(n) time."""
    end = c.size() - 1
    i = end
    while (i >= 0):
        p_index = int((i-1)/2)
        low_bound = p_index
        while (i >= low_bound):
            p_index = int((i-1)/2)
            index_one = 2*p_index + 1
            index_two = 2*p_index + 2
            if ((index_one <= end) and (index_two <= end)):
                child_one = c.access(index_one)
                child_two = c.access(index_two)
                i = i - 2
            elif (index_one <= end):
                child_one = c.access(index_one)
                child_two = c.access(index_one)
                i = i - 1
            parent = c.access(p_index)
            while ((parent > child_one) or (parent > child_two)):
                child = min(child_one, child_two)
                c.store(p_index, child)
                if (child_one == child):
                    c.store(index_one, parent)
                    p_index = index_one
                else:
                    c.store(index_two, parent)
                    p_index = index_two
                index_one = 2*p_index + 1
                index_two = 2*p_index + 2
                parent = c.access(p_index)
                if ((index_one <= end) and (index_two <= end)):
                    child_one = c.access(index_one)
                    child_two = c.access(index_two)
                elif (index_one <= end):
                    child_one = c.access(index_one)
                    child_two = c.access(index_one)
                if (index_one > end):
                    child_one = parent
                    child_two = parent
##==========================================================================           
def list_to_contiguous(vals: 'list[any]') -> Contiguous:
    """Create a Contiguous containing the items in vals."""
    c = Contiguous(len(vals))
    for i in range(len(vals)):
        c.store(i, vals[i])

    return c
##==========================================================================
c = list_to_contiguous([11,7,1,6,5,12,9,2,4,10,8,3])
print(c)
heapify(c)
print(c)
