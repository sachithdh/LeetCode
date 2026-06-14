class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def insertAtEnd(self, val):
        temp = self

        while temp.next is not None:
            temp = temp.next

        temp.next = ListNode(val)

    def printData(self):
        ptr = self
        while ptr is not None:
            print(ptr.val, end=" -> ")
            ptr = ptr.next
        print("None")


def countNodes(self):
    ptr = self
    count = 0
    while ptr is not None:
        count += 1
        ptr = ptr.next
    return count


ListNode.countNodes = countNodes

def removeNthFromEnd(head, n):
    count = head.countNodes()
    
    if count == n:
        return head.next
    ptr = head
    temp = ptr
    
    for i in range (count - n):
        temp = ptr
        ptr = ptr.next
        
    temp.next = ptr.next
    return head