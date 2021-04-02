"""
Author: Ibad Rather
email: ibad.rather.ir@gmail.com
Date: 02-04-2021
"""
# Linked list can store all types of data


class Node:
    # Represents individual element in linked list
    def __init__(self, data=None, next=None):
        self.data = data  # can contain any data
        self.next = next  # pointer to the next element


class LinkedList:
    def __init__(self):
        self.head = None  # points to the head of linked list

    # insert element at the begining
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    # print linked list
    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next
        print(llstr)

    # inserting at end
    def insert_at_end(self, data):
        # if linked list is empty, insert at beginning
        if self.head is None:
            self.head = Node(data, None)
            return
        # if LL is not empty
        itr = self.head     # make an iteration variable
        while itr.next:     # loop until we reach end of LL  # when at end it becomes None
            itr = itr.next
        itr.next = Node(data, None)

    # Insert Values
    def insert_values(self, data_list):
        # we are wiping all current values and inserting new ones from the given data list
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    # Length of Linked List
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    # Remove Element at a particular index
    def remove_at(self, index):
        # We will raise exception if the index is not valid
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        # If we are removing the head
        if index == 0:
            self.head = self.head.next
        """
        Advantageously we are using python which will take care of 
        Garbage Collection automatically, but if we are using C++,
        we will have to do it manually here.
        """

        # Other general cases
        count = 0
        itr = self.head
        while itr:
            """
            In linked list we have to stop at element prior to the
            element we want to remove. We can modify the links there.
            That will automatically remove the element.
            """
            if count == index - 1:
                """
                We link the previous element to next element and the 
                element at the required index is removed.
                """
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    # Insert at a particular index
    def insert_at(self, index, data):
        # We will raise exception if the index is not valid
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            # self.head = Node(data, self.head)
            # or
            self.insert_at_beginning(data)
            return

        # other general cases
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)     # creating a new node with data and next as link of next element
                # we are slipping a new element here
                itr.next = node
                break

            itr = itr.next
            count += 1

    # Insert after a particular data
    def insert_after_value(self, data_after, data_to_insert):
        """
        First we want to find the index at which the data after which we want to
        insert is present. We do this by counting indexes up to that point.

        NOTE: This function does not check whether the data is present in the LL.
        """
        itr = self.head
        count = 0
        run = True
        while run:
            if itr.data == data_after:
                run = False
            itr = itr.next
            count += 1
        """
        After Finding the index, we use insert at function previously defined
        by us to insert at the particular index.
        """
        self.insert_at(count, data_to_insert)

    # Remove element after a given element
    def remove_by_value(self, data):
        # Remove first node that contains data
        itr = self.head
        count = 0
        # we will iterate untill we find the data in LL
        # to keep the count of the index, we will use count variable
        while itr:
            if itr.data == data:
                break
            itr = itr.next
            count += 1
        # After finding the index using count we will use remove_at() method
        # to remove that particular element from the list
        self.remove_at(count)


if __name__ == "__main__":
    # create LL
    ll = LinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print()
    ll.insert_after_value("mango", "apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    ll.insert_after_value("mango", "figs")
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()

