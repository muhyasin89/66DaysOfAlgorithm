package Practice.LinkedList;

import java.util.List;
import java.util.Arrays;

public class LinkedList {
    Node head;
    LinkedList globalList;

    static class Node {
        int data;
        Node next;

        Node(int d) {
            data = d;
            next = null;
        }
    }

    LinkedList setLinkedList(List<Integer> nums) {
        LinkedList llist = new LinkedList();
        Node temp = new Node(0);
        llist.head = new Node(nums.get(0));
        llist.head.next = new Node(nums.get(1));
        temp = llist.head.next;

        for (int i = 2; i < nums.size(); i++) {
            // System.out.print(nums.get(i));
            temp.next = new Node(nums.get(i));
            temp = temp.next;
        }

        return llist;

    }

    // adding node
    public void addNode(int data) {
        if (head == null) {
            head = new Node(data);
            return;
        }

        Node curr = head;
        while (curr.next != null) {
            curr = curr.next;
        }

        Node newNode = new Node(data);
        curr.next = newNode;
    }

    // take first and last linkedlist
    Node partitionLast(Node start, Node end) {
        if (start == end || start == null || end == null) {
            return start;
        }

        Node pivot_prev = start;
        Node curr = start;
        int pivot = end.data;

        // iterate till one before the end, the end is pivot
        while (start != end) {
            if (start.data < pivot) {
                pivot_prev = curr;
                int temp = curr.data;
                curr.data = start.data;
                start.data = temp;
                curr = curr.next;
            }
            start = start.next;
        }

        // swap the position of curr
        int temp = curr.data;
        curr.data = pivot;
        end.data = temp;

        // return one previous to current
        // because current is now pointing to pivot
        return pivot_prev;

    }

    public void sort(Node start, Node end) {
        if (start == null || start == end || start == end.next) {
            return;
        }

        // split list and partition recurse
        Node pivot_prev = partitionLast(start, end);
        sort(start, end);

        // if pivot is picked and moved to the start,
        // that means start and pivot is same
        // so pick from next of pivot
        if (pivot_prev != null && pivot_prev == start) {
            sort(pivot_prev.next, end);
        } else if (pivot_prev != null && pivot_prev.next != null) {
            // if pivot is in between of the last
            // start from next of pivot
            // since we have pivot_prev, so we move two nodes
            sort(pivot_prev.next.next, end);
        }

    }

    public void printList(LinkedList llist) {
        Node n = llist.head;
        while (n != null) {
            System.out.print(n.data + " ");
            n = n.next;
        }
    }

    void printListInteger(List<Integer> nums) {
        for (Integer s : nums) {
            int i = nums.indexOf(s);
            System.out.print("-> " + s);
            // System.out.println("Item " + i + " : " + s);
        }
        System.out.println();
    }

    public static void main(String[] args) {
        // [2, 4, 1, 5, 3, 7, 10, 8, 9];
        List<Integer> list_1 = Arrays.asList(2, 4, 1, 5, 3, 7, 10, 8, 9);

        LinkedList list_a = new LinkedList();

        list_a = list_a.setLinkedList(list_1);
        list_a.printList(list_a);
        System.out.println();

        // [4, 3, 1, 10, 5, 7, 6, 8, 9];
        List<Integer> list_2 = Arrays.asList(4, 3, 1, 10, 5, 7, 6, 8, 9);

        LinkedList list_b = new LinkedList();
        list_b = list_b.setLinkedList(list_2);
        list_b.printList(list_b);
        System.out.println();
    }
}