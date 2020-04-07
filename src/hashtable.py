# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def delete(self):
        if self.next:
            self.value = self.next.value
            self.key = self.next.key
            self.next.delete()
        else:
            self = None

    def delete_by_key(self, key):
        if self.key == key:
            self.delete()
            return key
        elif self.next:
            return self.next.delete_by_key(key)
        else:
            return None

    def set_key_value(self, value, key):
        """
        recursiv method to insert in lis
        will override same keys,
        if there is a next node, call the function againg
        """
        if self.key == key:
            self.value = value
        elif self.next:
            self.next.set_key_value(value, key)
        else:
            self.next = LinkedPair(key, value)
        
    
    def get_key_value(self, key ):
        if self.key == key:
            return self.value
        elif self.next:
            return self.next.get_key_value(key)
        else:
            return None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.count = 0


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''

        return self._hash_djb2(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        hash_num = 5381

        for x in key:
            hash_num = ((hash_num << 5) + hash_num) + ord(x)
        return hash_num & 0xFFFFFFFF



    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''

        index = self._hash_mod(key)
        print("insert index", index, "value", value, "with key", key)
        node = LinkedPair(key, value)

        if self.storage[index] is None:
            self.storage[index] = node

            self.count += 1
            print("count", self.count)
            # self.resize()
        else:
            self.storage[index].set_key_value(value,key)

    def get_index(self, key):

        index = self._hash_mod(key)
        if self.storage[index] is not None:
            return index
        else:
            return None

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self.get_index(key)
        if index is None:
            return "Key is not present"

        node = self.storage[index]
        if node.key == key:
            self.storage[index] = node.next
            self.count -=1
            # self.resize()
            return key
        else:
            current = node
            next_node = node.next
            while next_node is not None:
                if next_node.key == key:
                    current.next = next_node.next
                    self.count -= 1
                    # self.resize()
                    return key
                else:
                    current = next_node
                    next_node = current.next


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self.get_index(key)
        if index is None:
            return "Key is missing"

        else:
            # node = self.capacity[index]
            return self.storage[index].get_key_value(key)
        


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        
        storage = self.storage
        capacity = self.capacity
        self.capacity = capacity * 2
        self.storage = [None] * self.capacity
        for i in range(capacity):
            node = storage[i]
            while node != None:
                self.insert(node.key, node.value)
                node = node.next



# if __name__ == "__main__":
#     ht = HashTable(2)

#     ht.insert("line_1", "Tiny hash table")
#     ht.insert("line_2", "Filled beyond capacity")
#     ht.insert("line_3", "Linked list saves the day!")

#     print("")

#     # Test storing beyond capacity
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     # Test resizing
#     old_capacity = len(ht.storage)
#     ht.resize()
#     new_capacity = len(ht.storage)

#     # print(f"hhh")

#     # Test if data intact after resizing
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     print("")
