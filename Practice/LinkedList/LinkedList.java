package Practice.LinkedList;

import java.util.List;
import java.util.Arrays;

public class LinkedList {
    Node head;

    static class Node {
        int data;
        Node next;

        Node(int d) {
            data = d;
            next = null;
        }
    }

    void setLinkedList(List<Integer> nums) {
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

        llist.printList(llist);
        System.out.println();

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
        // ArrayList<Integer> firstList = new ArrayList<>();
        // [2, 4, 1, 5, 3, 7, 10, 8, 9];
        List<Integer> list_1 = Arrays.asList(2, 4, 1, 5, 3, 7, 10, 8, 9);

        LinkedList list_a = new LinkedList();
        // list_a.printListInteger(list_1);
        // list_a.setLinkedList(list_1);
        list_a.setLinkedList(list_1);

        // [4, 3, 1, 10, 5, 7, 6, 8, 9];
        List<Integer> list_2 = Arrays.asList(4, 3, 1, 10, 5, 7, 6, 8, 9);

        LinkedList list_b = new LinkedList();
        // list_b.printListInteger(list_2);
        list_b.setLinkedList(list_2);
    }
}