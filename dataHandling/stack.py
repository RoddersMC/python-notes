from singlyNode import SinglyNode as Node

class Stack:
    def __init__(self, name=None, limit=None):
        self.top_item = None
        self.name = None
        self.size = 0
        self.limit = limit
  
    def push(self, value):
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
        else:
            print("No room!")

    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        print("Stack empty.")

    def peek(self):
        if not self.is_empty():
            return self.top_item.get_value()
        print("Stack empty.")

    def has_space(self):
        if self.limit is None:
            return True
        return self.limit > self.get_size()

    def is_empty(self):
        return self.get_size() == 0

    def get_size(self):
        return self.size
    
    def get_name(self):
        return self.name
    
    def print_items(self):
        pointer = self.top_item
        print_list = []
        while(pointer):
            print_list.append(pointer.get_value())
            pointer = pointer.get_next_node()
            print_list.reverse()
            print("{0} Stack: {1}".format(self.get_name(), print_list))