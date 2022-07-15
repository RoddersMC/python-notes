from singlyNode import SinglyNode as Node

class LinkedList:
    def __init__(self, value=None):
        self.head_node = None if value is None else Node(value)
    
    def __iter__(self):
        current_node = self.head_node
        while(current_node):
            yield current_node.get_value()
            current_node = current_node.get_next_node()

    def get_head_node(self):
        return self.head_node
    
    def stringify_list(self):
        string_list = ""
        current_node = self.get_head_node()
        while current_node is not None:
            string_list += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string_list
    
    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node
    
    def insert_end(self, new_value):
        new_node = Node(new_value)
        current_node = self.head_node

        if current_node is None:
            self.head_node = new_node

        while(current_node):
            next_node = current_node.get_next_node()
            if next_node is None:
                current_node.set_next_node(new_node)
            current_node = next_node
    
    def remove_node(self, value_to_remove):
        current_node = self.get_head_node()
        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node:
                next_node = current_node.get_next_node()
                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    current_node = None
                else:
                    current_node = next_node
    
    def swap_nodes(input_list, val1, val2):
        if val1 == val2:
            return ValueError("Elements are the same - no swap needed")

        node1_prev = None
        node2_prev = None
        node1 = input_list.head_node
        node2 = input_list.head_node

        while node1 is not None:
            if node1.get_value() == val1:
                break
            node1_prev = node1
            node1 = node1.get_next_node()

        while node2 is not None:
            if node2.get_value() == val2:
                break
            node2_prev = node2
            node2 = node2.get_next_node()

        if (node1 is None or node2 is None):
            return LookupError("Swap not possible - one or more element is not in the list")

        if node1_prev is None:
            input_list.head_node = node2
        else:
            node1_prev.set_next_node(node2)

        if node2_prev is None:
            input_list.head_node = node1
        else:
            node2_prev.set_next_node(node1)

        temp = node1.get_next_node()
        node1.set_next_node(node2.get_next_node())
        node2.set_next_node(temp)
    
    def nth_last_node(self, n=1):
        count = 1
        t_pointer = self.head_node
        n_pointer = None
        while t_pointer is not None:
            t_pointer = t_pointer.get_next_node()  
            count +=1
            if count >= n+1:
                if n_pointer is None:
                    n_pointer = self.head_node
                else:
                    n_pointer = n_pointer.get_next_node()
            return n_pointer

    def find_middle(self):
        t_pointer = self.head_node
        m_pointer = self.head_node
        while t_pointer is not None:
            t_pointer = t_pointer.get_next_node()
            if t_pointer is not None:
                t_pointer = t_pointer.get_next_node()
                m_pointer = m_pointer.get_next_node()
        return m_pointer