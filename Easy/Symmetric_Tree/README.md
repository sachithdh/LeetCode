# First attempt

I first wrote the code in [attempt_01.py](./attempt_01.py). It passed 198 out of 202 test cases, but it failed on this tree:

`root = [5,2,2,4,null,null,1,null,1,null,4,2,null,2,null]`

```mermaid
graph TD;
    %% Node Definitions (Circles)
    n0(("5"))
    n1(("2"))
    n2(("2"))
    n3(("4"))
    n6(("1"))
    n8(("1"))
    n10(("4"))
    n13(("2"))
    n17(("2"))
    
    %% Hidden Spacer Nodes
    h1[ ]:::hidden
    h2[ ]:::hidden
    h3[ ]:::hidden
    h4[ ]:::hidden
    h5[ ]:::hidden
    h6[ ]:::hidden
    h7[ ]:::hidden
    h8[ ]:::hidden
    h9[ ]:::hidden
    h10[ ]:::hidden
    
    %% Level 0 -> 1
    n0 --> n1
    n0 --> n2
    
    %% Level 1 -> 2
    n1 --> n3
    n1 ~~~ h1
    n2 ~~~ h2
    n2 --> n6
    
    %% Level 2 -> 3
    n3 ~~~ h3
    n3 --> n8
    n6 ~~~ h4
    n6 --> n10
    
    %% Level 3 -> 4
    h3 ~~~ h5
    h3 ~~~ h6
    n8 --> n13
    n8 ~~~ h7
    h4 ~~~ h8
    h4 ~~~ h9
    n10 --> n17
    n10 ~~~ h10

    %% Invisible styling for layout spacers
    classDef hidden display:none,position:absolute;
```

The problem is that the `1` and `4` nodes appear in different orders in the left and right subtrees. Because of that, comparing the left and right slices of the inorder traversal made them look identical.

For example:

```python
l = ['null', '4', '2', '1', 'null', '2', 'null', '5', 'null', '2', 'null', '1', '2', '4', 'null']

l[:mid - 1] = ['null', '4', '2', '1', 'null', '2', 'null']
l[-1:-mid:-1] = ['null', '4', '2', '1', 'null', '2', 'null']
```

# Second attempt

I then wrote [attempt_02.py](./attempt_02.py). That version passed 199 out of 201 cases.

# Final attempt

Finally, I came up with the working solution in [solution.py](./solution.py). 