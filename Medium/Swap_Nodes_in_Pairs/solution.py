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
    if head is None or head.next is None:
        return head
    
    ptr = head
    temp = ptr
    ptr = ptr.next
    temp.next = ptr.next
    ptr.next = temp
    
    head = ptr
    ptr = temp
    
    while ptr.next is not None:
        temp = ptr.next
        ptr.next = temp.next
        if ptr.next is not None:
            temp.next = ptr.next.next
            ptr.next.next = temp
        else:
            temp.next = None
            ptr.next = temp
        
        if temp.next:
            ptr = temp
        else:
            return head
    return head


# Test cases
def list_to_array(head):
    result = []
    while head:
        result.append(head.value)
        head = head.next
    return result

def array_to_list(values):
    dummy = ListNode(0)
    ptr = dummy
    for v in values:
        ptr.next = ListNode(v)
        ptr = ptr.next
    return dummy.next

assert list_to_array(swapPairs(array_to_list([1, 2, 3, 4]))) == [2, 1, 4, 3]
assert list_to_array(swapPairs(array_to_list([]))) == []
assert list_to_array(swapPairs(array_to_list([1]))) == [1]
assert list_to_array(swapPairs(array_to_list([1,2,3]))) == [2,1,3]

print("All tests passed!")