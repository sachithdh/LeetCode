This is kind of an easy task if you are familiar with classes in Python.

First, I have defined a function to get the count of nodes in the given list and added it as a method to the `ListNode` class.

`nth` from the end of the list means `(Node count - n)` from the start of the list.

So the idea is pretty straightforward: First calculate the total number of nodes in the linked list. After that, convert the problem from “remove nth node from end” into a simple “remove (count - n)th node from the beginning”.

If the count is equal to `n`, it means we need to remove the head node itself, so simply return `head.next`.

Otherwise, I used two pointers:

* `ptr` is used to traverse the list and reach the target node
* `temp` keeps track of the previous node so we can update its `next` pointer

It iterate `(count - n)` steps from the beginning. During this traversal, `ptr` ends up pointing to the node that needs to be removed, while `temp` stays just behind it.

Finally, it simply skip the target node by doing:

```python
temp.next = ptr.next
```

and return the modified head of the linked list.
