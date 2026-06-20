# In memory data structure
# Map
# String -> String
# Support snapshots
# Single threaded

# (1) void put(string key, string value)
# (2) void delete(string key)
# (3) string get(string key, Snapshot snap)
# (4) Snapshot takeSnapshot()
# (5) void deleteSnapshot(Snapshot snap)

# Snapshot -> frozen view of the map at tiime of takeSnapshot()
# Frozen -> put() and delete() cannot modify a snapshot after it is created

# put(k1,v1)
# put(k2,v2)
# put(k3,v3)
# takeSnapshot() -> snap1 {}
# get(k1,snap1) -> v1
# get(k2,snap1) -> v2
# get(k3,snap1) -> v3
# put(k1,v4)
# delete(k3)
# takeSnapshot() -> snap2
# get(k1,snap2) -> v4
# get(k2,snap2) -> v2
# get(k3,snap2) -> ERROR "Key not found"
# get(k1,snap1) -> v1
# get(k2,snap1) -> v2
# get(k3,snap1) -> v3
# deleteSnapshot(snap1)
# get(k1,snap1) -> ERROR "Snapshot not found"
# get(k1,snap2) -> v4
# get(k2,snap2) -> v2
# get(k3,snap2) -> ERROR "Key not found"

# Requirement: space efficiency

class Snapshots():
    def __init__(self):
        self.snap_add_map = {} # snap_id -> hmap
        self.snap_del_map = {} # snap_id -> hmap
        self.cur_id = 0 # auto-incrementing number

    def take_snapshot(self, add_hmap, del_hmap):
        # allocate an id
        # use the current hmap, take delta and generate added_map and removed_map
        
        self.cur_id += 1
        new_add_hmap = copy(add_hmap)
        new_del_hmap = copy(del_hmap)
        self.snap_add_map[self.cur_id] = new_add_hmap
        self.snap_del_map[self.cur_id] = new_del_hmap
        return self.cur_id
        
    def get_from_snapshot(self, id, k):
        if self.snap_add_map[id] == None:
            return True, -1
            # indicates that look at the previous snap since current one is deleted.
        
        if k in self.snap_del_map[id]:
            return False, -1
        
        if k in self.snap_add_map[id]:
            return True, self.snap_add_map[id][k]
        
        return True, -1
            
'''
snap1: k1, k2, k3, k4, k5
snap2: k1(v1')
snap3:del: k2,
'''
   
    def del_snapshot(self, id):
        if id <= self.cur_id:
            self.snap_add_map.pop(id)
            self.snap_del_map.pop(id)
        
        return
    
class mem_map():
    def __init__(self):
        self.add_hmap = {}
        self.del_hmap = {}
        self.snapshot = Snapshots()
    
    def put(self, k, v):
        self.add_hmap[k]  = v
        
    def delete(self, k):
        self.del_hmap[k] = 1
        
    def get(self, k, snap_id):
        
        for id in range(snap_id, 0, -1):
            status, value = self.snapshot(self.snapshot, id, k)
            
            if status == True:
                if value != -1:
                    return value
                if value == -1:
                    continue
            else:
                return -1
            
    def takeSnapShot():
        self.snapshot.take_snapshot(add_hmap, del_hmap)
        self.add_hmap = {}
        self.del_hmap = {}
    

    
