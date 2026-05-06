#!/usr/bin/env python
""" LRU implementation using Python """

lru_hash = {}
lru_size = 0

def print_elem_addr(cache):
    i = 0
    for elem in cache:
        print "index:%02d addr:0x%x" % (i, id(elem))
        i += 1

def create_lru_cache(size):
    global lru_size
    lru_size = size
    return []

def remove_last_entry(cache, key):
    lru_hash.pop(key)
    cache.pop()

def insert_lru_cache(cache, key, value):
    global lru_hash
    global lru_size

    if lru_hash.has_key(key):
        print "Key:%s already in the cache" % key
        update_lru_cache(cache, key)
        return

    print "cache.count: %d lru_size:%d " % (len(cache), lru_size)
    if not len(cache) < lru_size:
        """ remove the last entry """
        print "last elem: %s" % cache[lru_size - 1]
        remove_last_entry(cache, cache[lru_size - 1])

    cache.append(key)
    "lru_hash[key] = len(cache) - 1"
    lru_hash[key] = id(cache[len(cache) - 1])


def remove_lru_cache():
    return []

def update_lru_cache(cache, key):
    index = lru_hash[key]
    cache.pop(index)
    cache.append(key)
    lru_hash[key] = len(cache) - 1

def lookup_lru_cache(cache, key):

    if not lru_hash.has_key(key):
        print "Cache miss"
        return

    update_lru_cache(cache, key)

def main():
    print "lru_size:%d" % lru_size
    lru_cache = create_lru_cache(3)
    print "lru_size:%d" % lru_size
    insert_lru_cache(lru_cache, "1", "abc1")
    print_elem_addr(lru_cache)
    print "1: ", lru_cache
    insert_lru_cache(lru_cache, "2", "abc2")
    print_elem_addr(lru_cache)
    print "2: ", lru_cache
    insert_lru_cache(lru_cache, "3", "abc3")
    print_elem_addr(lru_cache)
    print "3: ", lru_cache
    insert_lru_cache(lru_cache, "4", "abc4")
    print_elem_addr(lru_cache)
    print "4: ", lru_cache
    insert_lru_cache(lru_cache, "1", "abc1")
    print_elem_addr(lru_cache)
    print "1: ", lru_cache
    print lru_cache
    print lru_hash
    pass

if __name__ == '__main__':
    main()

