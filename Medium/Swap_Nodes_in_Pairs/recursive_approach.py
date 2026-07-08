class ListNode:
    def __init__(self, val, next=None):
        self.value = val
        self.next = next
        
        
    def printNodes(self, head):
        temp = head
        
        while temp is not None:
            print(temp.value, end="->" if temp.next else "")
            temp = temp.next
                
        print()
        
        
    def insertAtEnd(self, head, val):

        new_node = ListNode(val)

        if head is None:
            return new_node
        
        ptr = head
        
        while ptr.next is not None:
            ptr = ptr.next
            
        ptr.next = new_node
        return head

def swapPairs(head):
    if not head or not head.next:
        return head
    
    first = head
    second = head.next
    
    first.next = swapPairs(second.next)
    second.next = first
    
    return second