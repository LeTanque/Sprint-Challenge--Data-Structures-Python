class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)
        self.head = node

    def print_nodes(self):
        node = self.head
        while node:
            print("node", node.value)
            if node.next_node is not None:
                print("   next node value", node.next_node.value)
            node = node.next_node

    def contains(self, value):
        if not self.head:
            print("there is no list")
            return False
        # get a reference to the node we're currently at; update this as we traverse the list
        # starts at the head
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def reverse_list(self):
        # these are the pointers. Starts at head with no previous
        prev = None
        node = self.head
        # While node is not none
        while node:
            # Store current next node in new next
            new_next = node.next_node
            # nodes next node becomes previous
            node.next_node = prev
            # Previous node becomes current node
            prev = node
            # Current node becomes next node
            node = new_next
            # Head becomes prev, which is node
            self.head = prev


# Driver program to test above functions
llist = LinkedList()
llist.add_to_head(1)
llist.add_to_head(2)
llist.add_to_head(10)

print("Given Linked List")
llist.contains(2)
llist.contains(10)
llist.contains(13)
llist.reverse_list()
print("\nreverse_list Linked List")
# llist.contains()
# Complexity is linear of reverse list
