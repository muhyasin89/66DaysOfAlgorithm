# Singly-linked lists are already defined with this interface:
class ListNode(object):
    def __init__(self, x=0):
        self.value = x
        self.next = None
        self.head = None
        self.tail = None

    # This function prints contents of linked list
    # starting from head
    # def printList(self):
    #     temp = self.head
    #     while (temp):
    #         print temp.data,
    #         temp = temp.next
    def __len__(self):
        count = 0
        current_node = self.head
        while current_node is not None:
            count += 1
            current_node = current_node.next

        return count

    def add_list_item(self, item):
        """add item at end of list"""

        if not isinstance(item, ListNode):
            item = ListNode(item)

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item

        self.tail = item

        return


# split linked list in middle
def split_link(new_list, list1, list2):
    while 1:
        p = new_list.head
        q = new_list.head

        p = p.next.next
        if p.next == None:
            start_second = q.next.next
            break
        if p == None:
            start_second = q.next
            break
        q = q.next
    q.next = None

    current_list = new_list.head
    while 1:
        add_list = list1
        if current_list is new_list.head:
            add_list.head = current_list

        # first list
        if current_list is start_second:
            add_list.next = None
            add_list = list2
            add_list.head = current_list

        if current_list is p:
            break

        add_list.add_list_item(current_list)
        current_list = current_list.next

    add_list.next = None

    return {"list_1": list1, "list_2": list2}


# if odd ignore middle node
def ignore_middle_node(list1, list2):
    if list1.__len__ < list2.__len__:
        list2.head = list2.next

    return list2


# reverse second linkedList
def reverse_list(old_list):
    current_list = old_list.head
    new_list = ListNode()
    temp_list = []
    while 1:
        if current_list is None:
            break
        temp_list.append(current_list)

    # add from back
    n = len(temp_list)
    while 1:
        if n == 0:
            break
        new_list.add_list_item(temp_list[n - 1])

    return new_list


# compare two LinkedList
def equal_list(list1, list2):
    while list1 and list2 and list1.value == list2.value:
        list1 = list1.next
        list2 = list2.next
    if not list1 and not list2:
        return True
    return False


# prepare two linked list
l = [0, 1, 0]
ori_list = ListNode()

for item in l:
    ori_list.add_list_item(item)

list_1 = ListNode()
list_2 = ListNode()

split_list = split_link(ori_list, list_1, list_2)

list_1 = split_list["list_1"]
list_2 = split_list["list_2"]

# ignore middle node
list_2 = ignore_middle_node(list_1, list_2)

# reverse second node
list_2 = reverse_list(list_2)

# is palindromemurray
final = equal_list(list_1, list_2)

print(final)
