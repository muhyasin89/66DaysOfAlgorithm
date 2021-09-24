import java.util.*;

public class SingleLinkList {

    void printLinkedList(LinkedList<Integer> node) {
        for (int i = 0; i < node.size(); i++) {
            System.out.print(node.get(i) + "->");
        }

        System.out.println();
    }

    LinkedList<Integer> reverseLinkedList(LinkedList<Integer> list) {
        LinkedList<Integer> reverseList = new LinkedList<Integer>();

        for (int i = list.size() - 1; i >= 0; i--) {
            reverseList.add(list.get(i));
        }

        return reverseList;
    }

    LinkedList<Integer> changeListToLinkedList(LinkedList<Integer> list, int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            list.add(arr[i]);
        }
        return list;
    }

    ArrayList<Integer> changeLinkedListToArr(LinkedList<Integer> list) {
        ArrayList<Integer> arr = new ArrayList<>();

        for (int i = 0; i < list.size(); i++) {
            arr.add(list.get(i));
        }

        return arr;
    }

    public static void main(String[] args) {
        int[] arr = new int[] { 1, 4, 5, 6, 7 };
        LinkedList<Integer> list = new LinkedList<Integer>();

        SingleLinkList obj = new SingleLinkList();
        list = obj.changeListToLinkedList(list, arr);

        System.out.println(Arrays.toString(arr));

        obj.printLinkedList(list);

        list = obj.reverseLinkedList(list);
        obj.printLinkedList(list);

        System.out.println(obj.changeLinkedListToArr(list));
    }
}
