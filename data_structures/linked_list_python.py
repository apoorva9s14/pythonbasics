
class Node:
    """Each node in the linkedlist"""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        # while node is not None:
        for node in self:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        """To traverse the linked list"""
        node = self.head
        while node:
            yield node
            node = node.next

    @staticmethod
    def check_if_valid_node(node):
        if type(node) != Node:
            raise ValueError

    def insert(self, node):
        """TO insert Nodes at the beginning"""
        self.check_if_valid_node(node)
        prev_head = self.head
        self.head = node
        self.head.next = prev_head

    def insert_at_end(self, node):
        self.check_if_valid_node(node)
        # if not self.head:
        #     self.head = node
        #     return
        for current_node in self:
            pass
        current_node.next = node

class CircularLinkedList(LinkedList):
    def __init__(self, nodes=None):
        self.head = None
        if nodes:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next
            node.next = self.head

    def __iter__(self):
        """To traverse the circular linked list"""
        print("iter called")
        traversed_nodes = []
        node = self.head
        while node and node not in traversed_nodes:
            yield node
            traversed_nodes.append(node)
            node = node.next

    def insert(self, node):
        """TO insert Nodes at the beginning"""
        self.check_if_valid_node(node)
        prev_head = self.head
        self.head = node
        self.head.next = prev_head
        for cur_node in self:
            pass
        cur_node.next = self.head

    def insert_at_end(self, node):
        self.check_if_valid_node(node)
        for cur_node in self:
            pass
        cur_node.next = node
        node.next = self.head


class DoublyLinkedList(LinkedList):
    def __init__(self, nodes=None):
        self.head = None
        if nodes:
            node = Node(data=nodes.pop(0))
            previous_node = None
            self.head = node
            self.prev = previous_node
            for elem in nodes:
                node.next = Node(data=elem)
                node.prev = previous_node
                previous_node = node
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        # while node is not None:
        for node in self:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " <-> ".join(nodes)


    def insert(self, node):
        """TO insert Nodes at the beginning"""
        self.check_if_valid_node(node)
        prev_head = self.head
        self.head = node
        self.head.next = prev_head
        self.head.prev = prev_head

    def insert_at_end(self, node):
        self.check_if_valid_node(node)
        # if not self.head:
        #     self.head = node
        #     return
        for current_node in self:
            pass
        current_node.next = node
        node.prev = current_node


# class TestRunner:
#     def __init__(self, class_name, *args, **kwargs):
#         self.class_name = class_name
#         self.class_args = kwargs
#         self.class_methods = args
#         self.test_class_obj = class_name.__init__(**self.class_args)
#         for each_meth in self.class_methods:
#             self.test_class_obj.each_meth


if __name__ == "__main__":
    ########SingleLinkedlist#########
    # new_linkedlist = LinkedList(nodes=[1,2,3])
    # new_linkedlist.insert(Node(0))
    # print(new_linkedlist)
    # new_linkedlist.insert_at_end(Node(4))
    # print(new_linkedlist)
    ########CircularLinkedList#######
    new_linkedlist = CircularLinkedList(nodes=[1, 2, 3])
    new_linkedlist.insert(Node(0))
    print(new_linkedlist)
    new_linkedlist.insert_at_end(Node(4))
    print(new_linkedlist)
    for each in new_linkedlist:
        print(each.data)

    ########Doubly LinkedList#######
    new_linkedlist = DoublyLinkedList(nodes=[1, 2, 3])
    new_linkedlist.insert(Node(0))
    print(new_linkedlist)
    new_linkedlist.insert_at_end(Node(4))
    print(new_linkedlist)
