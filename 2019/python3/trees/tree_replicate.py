class Node:
    def __init__(self, data):
        self.data = data
        self.left = none
        self.right = none
        self.extra = none

h = {}
replicate(root, h)

def replicate(root, h):
    if not root:
        return None
    
    new_node = Node(root.data)
    new_node.left = replicate(root.left)
    new_node.right = replicate(root.right)
    
    h[root.data] = new_node
    return new_node
 
    
    none
      10<------
    6---->11
  5<-----------

        10' -> 5'
    6' -->      11'
  5'-> 10'

hash:
    <root, new_node>
    5, 5'
    .
    .
    .
    10, 10'
    
def join_extra(root, new_root, h):
    if not root:
        return
    
    new_root.extra = h[root.extra.data]
    join_extra(root.left, new_root.left)
    join_extra(root.right, new_root.right)
    
 
def replicate_extra(root, h):
    if not root:
        return None
    
    if not root and h[root.data]:
        new_node = h[root.data]
        new_node.extra = h[root.extra.data]
    else:
        new_node = Node(root.data)
        extra_node = Node(root.extra.data)
        
        h[root.extra.data] = extra_node
        h[root.data] = new_node
        new_node.extra = extra_node
        
    new_node.left = replicate_extra(root.left)
    new_node.right = replicate_extra(root.right)
    
   
    return new_node
 
    
    
 
