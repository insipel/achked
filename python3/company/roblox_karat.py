def hello_world():
    print("Hello, world!")
    print("This is a fully functioning Python 3 environment.")

hello_world()



# Suppose we have some input data describing a graph of relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.

# For example, in this diagram, 3 is a child of 1 and 2, and 5 is a child of 4:
            
#   11
#    \ 
# 1   2   4
#  \ /   / \
#   3   5   8
#    \ / \   \
#     6   7   10

# Write a function that, for a given individual in our dataset, returns their earliest known ancestor -- the one at the farthest distance from the input individual. If there is more than one ancestor tied for "earliest", return any one of them. If the input individual has no parents, the function should return null (or -1).

# Sample input and output:
parent_child_pairs = [
    (1, 3), (2, 3), (3, 6), (5, 6),
    (5, 7), (4, 5), (4, 8), (8, 10), (11, 2)
]


# findEarliestAncestor(parentChildPairs, 8) => 4
# findEarliestAncestor(parentChildPairs, 7) => 4
# findEarliestAncestor(parentChildPairs, 6) => 11
# findEarliestAncestor(parentChildPairs, 1) => null or -1

def findEarliestAncestor(parentChildPairs, n):
    # collect all the parents for the Child
    # Do a DFS to find the max depth parent and keep track of that in a list object in the recursion frame.

def hasCommonAncestor(pairs, n1, n2):
    cmap = {}
   
    for p, c in pairs:
     
        if c in cmap:
            cmap[c].append(p)
        else:
            cmap[c] = [p]
    
    if n1 not in cmap or n2 not in cmap:
        return False
    
    node1 = cmap[n1]
    node2 = cmap[n2]
    plist1 = {}
    #plist2 = {}
    
    q = []
    q.append(n1)
    while q:
        n1 = q.pop()
        l1 = []
        if n1 in cmap:
            l1 = cmap[n1]
            
        for node in l1:
            q.append(node)
            plist1[node] = 1

    q.append(n2)
    while q:
        n2 = q.pop()
        l1 = []
        if n2 in cmap:
            l1 = cmap[n2]
            
        for node in l1:
            q.append(node)
            if node in plist1:
                return True
    
    return False
        

#print(hasCommonAncestor(parentChildPairs2, 4, 8))
print(hasCommonAncestor(parentChildPairs1, 5, 6))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
