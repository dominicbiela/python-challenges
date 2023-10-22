
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class ListNode:
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head == None:
            print('Linked list is empty')
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.value) + '-->'
            itr = itr.next
        print(llstr)

    def removeKFromList(self, k: int) -> None:
        curr = self.head
        while curr:
            if curr.next and curr.next.value == k:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return self.head.next if self.head and self.head.value == k else self


    def isPalindrome(self) -> bool:
        slow, fast, prev = self.head, self.head, None
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        prev, slow, prev.next = slow, slow.next, None
        while slow:
            temp = slow.next
            slow.next, prev, slow = prev, slow, temp
        fast, slow = self.head, prev
        while slow:
            if fast.value != slow.value: return False
            fast, slow = fast.next, slow.next
        return True

    #1->2->3->2->1


if __name__ == '__main__':
    # Create a new instance of the ListNode class
    linked_list = ListNode()

    # Add nodes to the linked list
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    linked_list.insert(2)
    linked_list.insert(1)

    # Print Linked List before removal
    linked_list.print()
    # Call the removeKFromList method on the linked list
    new_head = linked_list.removeKFromList(2)
    # Print Linked List after removal
    linked_list.print()

    print(linked_list.isPalindrome())
