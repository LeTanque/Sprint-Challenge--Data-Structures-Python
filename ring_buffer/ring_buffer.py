from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.current = None
        self.capacity = capacity
        self.storage = DoublyLinkedList()

    def append(self, item):
        # # We need to assign items to the dll
        # # Each new item get's moved to the tail
        # 
        # self.storage.add_to_tail(item)
        # # Once capacity is met
        # # Add to tail
        # # Remove the head
        # # Set current item
        # if self.storage.length >= self.capacity:
        #     print("Capacity has been met!")
        #     self.storage.add_to_tail(item)
        #     self.storage.remove_from_head()
        #     self.current = item
        # # If capacity is not met
        # # Add to tail
        # # Set current item
        # else:
        #     self.storage.add_to_tail(item)
        #     self.current = item
        # # New items replace the oldest item

        # IF we are not yet at capacity...
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
        # IF we are at capacity...
        else:
            # IF the last node (current) is the tail
            if self.current == self.storage.tail:
                # Remove the head and replace with item
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
                # Set the current to the head (circle back)
                self.current = self.storage.head
            # Always insert after the last item
            else:
                # insert after current node
                self.storage.insert_after(self.current, item)
                # Set current to current next (accelerate)
                self.current = self.current.next
                self.storage.delete(self.current.next)

    def get(self):
        # print('self.capacity: ', self.capacity)
        # print("self.current: ", self.current)
        # print("self.storage: ", self.storage.length)
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # If there is not list
        if self.current is None:
            # print("empty ring buffer")
            return list_buffer_contents
        else:
            node = self.storage.head
            while node is not None:
                list_buffer_contents.append(node.value)
                node = node.next

        # for rs in range(0, self.capacity):
        # print('node: ', node.value)
        # while node:
        #     list_buffer_contents.append(node.value)
        #     node = node.next

        # Print the list of items in the order needed
        # Find a way to print the current item as i[0]
        # and all subsequent items following it
        # This way the final array is correct
        # print("DLL tail ---> ", self.storage.tail, self.storage.tail.value)
        # print("DLL head ---> ", self.storage.head, self.storage.head.value)
        return list_buffer_contents


buffer = RingBuffer(3)
# print("Print Buffer get() ---> ", buffer.get())        # []
buffer.append('a')
# print("Print Buffer get() ---> ", buffer.get())        # 1 ['a']
buffer.append('b')
# print("Print Buffer get() ---> ", buffer.get())        # 2 ['a', 'b']
buffer.append('c')
# print("Print Buffer get() ---> ", buffer.get())        # should return ['a', 'b', 'c']
# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')
# print("Print Buffer get() ---> ", buffer.get())        # should return ['d', 'b', 'c']
buffer.append('e')
# print("Print Buffer get() ---> ", buffer.get())        # should return ['d', 'e', 'c']
buffer.append('f')
buffer.append('g')
buffer.append('h')
buffer.append('i')
print("Print Buffer get() ---> ", buffer.get())        # should return ['d', 'e', 'f']


# ----------------Stretch Goal-------------------
# class ArrayRingBuffer:
#     def __init__(self, capacity):
#         pass

#     def append(self, item):
#         pass

#     def get(self):
#         pass
