// insert

what you want to do ?

you want to insert value to binary search tree

-- summary --
so check if the value is less than left
    check if tree left is None set that value
    else make current is tree.left
so check if value is less than right
    check if tree right is None set that value
    else make current is tree.right

 -- pseudo algorithm -- 

current = self
using while True
if value is less than left
	check if tree.left is None
		set tree.left to BTS(value) --> what is BTS (class to set tree)
	else
		current  = tree.left
if value is less than right
	check if tree.right is None
		set tree.right to BTS(value)
	else
		current  = tree.right
return self


-- what do you want to do contains -- 
you want to check contains value

if less value than current node
    go to left
if value is greated than current
    go to right


-- pseudo algorithm --
current  =  self
while current is not None:
    if value is less than current.left
        go to current = current.left

    if value is greater than current.right
        go to current = current.right

    else
        true

return false


-- what you need to do? -- 
remove value from Binary search tree
you need to record parent node -- why? because when we remove node we want to reasign the child of parent node

-- summary --

-- pseudo code --
currentNode =self
    while currentNode
        check if value is less than currenNode
            move current node to left
        check if value is bigger than currentNode
            move current nod to right
        else
            check if currentNode.left and currentNode.right is not None
                set value to currentNode right minimum value
                remove current node in currentNode.right.value -- currentNode.value is smallest value in right tree
            if current parentNode left is currentNode
                set parentNode left to currentNode.left if currentNode is not none else currentNode.right
            if current parentNode right is currentNode    
                set parentNode right to currentNode.left if currentNode is not none else currentNode.right
            if parentNode is None
                if currentNode.left is not None
                    currentNode.value is currentNode.left.value
                    currentNode.left is currentNode.left.left
                    currentNode.right is currentNode.left.right
                if currentNode.right is not None
                    currentNode.value is currentNode.right.value
                    currentNode.left is currentNode.right.left
                    currentNode.right is currentNode.right.right
                else
                    currentNode.value is None
            break
        return self

    getMinValue
        currentNode =self
        while currenNode.left is not None
            currentNode = currentNode.left

        return currentNode.value



