'''
    /**
     * Given a matrix of following relationships between N LinkedIn users (with ids from 0 to N-1):
     * followingMatrix[i][j] == true iff user i is following user j
     * thus followingMatrix[i][j] doesn't imply followingMatrix[j][i].
     * Let's also agree that followingMatrix[i][i] == false.
     *
     * An influencer is a user who is:
     * - followed by everyone else and
     * - not following anyone herself/himself
     *
     * This method should return the influencer's id in a given matrix of following relationships,
     * or return -1 if there is no influencer in this group.
     */
     
    int getInfluencer(boolean[][] followingMatrix);

    influencers i
      for all idx i
        iff for all j, f[j][i] = true except i != j
            and for all j, f[i][j] = False
            return True

    return False

    3x3
    0 1 1
    0 0 0
    0 1 0
    '''
def getInfluencer(following):
    r, c = len(following), len(following[0])

    if r <= 1:
        return -1

    for i in range(r):
        influencer = True

        for j in range(c):
            if i != j and following[j][i] == False:
                influencer = False
                break
        
        if not influencer:
            continue

        for k in range(r):
            if following[i][k] == True:
                influencer = False
                break
        
        if influencer:
            return i

    return -1

run time: O(r^^2)

hmap: {user_id: following_count, followed by count}

'''
    T1          T2
    a     |     a
   / \    |    / \
  b   c   |   c   b
 / \      |      / \
d   e     |     e   d    return true
 
    a     |     a
   / \    |    / \
  b   c   |   c   b
 / \      |      / \
d   e     |     e   x    return false (value doesn't match for last node)
  
    a     |     a
   / \    |    / \
  b   c   |   c   b
 / \      |    \   \
d   e     |     e   d    return false
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

bool isMirror(Node node1, Node node2):
    if not node1 and not node2:
        return True

    if (node1 and not node2) or (not node1 and node2):
        return False

    if node1.val != node2.val:
        return False

    if not isMirror(node1.left, node2.right):
        return False

    if not isMirror(node1.right, node2.left):
        return False

    return True

# edge case: null nodes both, one null node, single node diff val, single node same val.
# 
#
# node1, node2
# if not node1 and not node2: return True.
# node1.left, node2.right   and node1.right, node2.left
# if node1.left and not node2.left: return False, other way as well where node2.left is not null
# if node1.right and not node2.right: return False
# node1.value != node2.value: return False
#


