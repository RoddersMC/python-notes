from singlyLinkedList import LinkedList

class SeperateChainHashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [LinkedList() for _ in range(array_size)]
    
    def get_size(self):
        return self.array_size

    def get_index(self, key):
        h = self.hash(key)
        return self.compress(h)

    def hash(self, key):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code
  
    def compress(self, hash_code):
        return hash_code % self.get_size()
  
    def assign(self, key, value):
        array_index = self.get_index(key)
        list_at_index = self.array[array_index]
        for node_value in list_at_index:
            if node_value[0] == key:
                node_value[1] = value
                return
        list_at_index.insert_end([key, value])

    def retrieve(self, key):
        array_index = self.get_index(key)
        list_at_index = self.array[array_index]
        for node_value in list_at_index:
            if node_value[0] == key:
                return node_value[1]
        return None

    def delete(self, key):
        array_index = self.get_index(key)
        list_at_index = self.array[array_index]
        for node_value in list_at_index:
            if node_value[0] == key:
                list_at_index.remove_node(node_value)
                return