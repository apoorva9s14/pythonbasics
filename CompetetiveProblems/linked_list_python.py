"""
4 steps to reverse linked list:
While traversing the linked list
1. Store the current node's next Node.
2. Then change the current nodes's next to Previous node
3. Then assign the Previous node as current node
4. Then assign the current node as the stored next Node in the first step
"""
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
        for node in self:
            nodes.append(str(node.data))
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
        for current_node in self:
            pass
        current_node.next = node

    def reverse(self):
        # prev = None
        # current = self.head
        # while current:
        #     next = current.next
        #     current.next = prev
        #     prev = current
        #     current = next
        #     print(prev.data)
        # # print(self.head.data)
        # self.head = prev
        prev, _next = None, None
        each = self.head
        while each:
            _next = each.next
            each.next = prev
            prev = each
            each = _next
            # print(prev.data)
        self.head = prev

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




def sort_linked_list(linked_list_1):
    nodes = []
    for i in linked_list_1:
        nodes.append(i.data)
    nodes.sort()
    return LinkedList(nodes=nodes)


def merge_linked_lists(linked_list_1, linked_list_2):
    # print(linked_list_1, linked_list_2)
    for i in linked_list_2:
        linked_list_1.insert_at_end(Node(i.data))


def reverse_linked_list_in_place(linked_list_1):
    new_head = None
    head = linked_list_1.head
    # for head in linked_list_1:
    while head:
        tmp = head.next
        head.next = new_head
        new_head = head
        head = tmp
    return linked_list_1


if __name__ == "__main__":
    ########SingleLinkedlist#########
    new_linkedlist = LinkedList(nodes=[3, 1, 2])
    # new_linkedlist_2 = LinkedList(nodes=[6, 4, 5])
    # merge_linked_lists(new_linkedlist, new_linkedlist_2)
    # print(sort_linked_list(new_linkedlist))
    # reverse_linked_list_in_place(new_linkedlist)
    # print(new_linkedlist)
    new_linkedlist.reverse()
    print(new_linkedlist)

    # ########CircularLinkedList#######
    # new_linkedlist = CircularLinkedList(nodes=[1, 2, 3])
    # new_linkedlist.insert(Node(0))
    # print(new_linkedlist)
    # new_linkedlist.insert_at_end(Node(4))
    # print(new_linkedlist)
    # for each in new_linkedlist:
    #     print(each.data)
    #
    # ########Doubly LinkedList#######
    # new_linkedlist = DoublyLinkedList(nodes=[1, 2, 3])
    # new_linkedlist.insert(Node(0))
    # print(new_linkedlist)
    # new_linkedlist.insert_at_end(Node(4))
    # print(new_linkedlist)
