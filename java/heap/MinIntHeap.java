package heap;

import java.util.Arrays;

public class MinIntHeap {

    private int capacity = 10;
    private int size = 0;

    int[] items = new int[capacity];

    private int getLeftChildIndex(int parentIndex){
        return 2 * parentIndex + 1;
    }

    private int getRightChildIndex(int parentIndex){
        return 2 * parentIndex + 2;
    }

    private int getParentIndex(int childIndex){
        return (childIndex - 1) / 2;
    }

    private boolean hasLeftChild(int Index){
        return getLeftChildIndex(Index) < size;
    }

    private boolean hasRightChild(int Index){
        return getRightChildIndex(Index) >= size;
    }

    private boolean hasParent(int Index){
        return getParentIndex(Index) >= 0;
    }

    private int leftChild(int Index){
        return items[getLeftChildIndex(Index)];
    }

    private int rightChild(int Index){
        return items[getRightChildIndex(Index)];
    }

    private int parent(int Index){
        return items[getParentIndex(Index)];
    }

    private void swap(int IndexOne, int IndexTwo){
        int temp = items[IndexOne];
        items[IndexOne] = items[IndexTwo];
        items[IndexTwo] = temp;
    }

    private void ensureExtraCapacity(){
        if(size == capacity){
            items = Arrays.copyOf(items, capacity * 2);
            capacity *= 2;
        }
    }

    public void peek(){
        if(size == 0) throw new IllegalStateException();
    }


    public int pool(){
        if(size == 0) throw new IllegalStateException();

        int item = items[0];
        items[0] = items[size - 1];
        size--;

        heapifyDown();
        return item;
    }


    public void add(int Item){
        ensureExtraCapacity();
        items[size] = Item;
        size++;
        heapifyUp();
    }

    public void heapifyUp(){
        int Index = size - 1;
        while(hasParent(Index) && parent(Index) > items[Index]){
            swap(getParentIndex(Index), Index);
            Index = getParentIndex(Index);
        }
    }


    public void heapifyDown(){
        int Index = 0;
        while(hasLeftChild(Index)){
            int smallerChildIndex = getLeftChildIndex(Index);
            if(hasRightChild(Index) && rightChild(Index) < leftChild(Index)){
                smallerChildIndex =  getRightChildIndex(Index);
            }

            if(items[Index] < items[smallerChildIndex]){
                break;
            }else{
                swap(Index, smallerChildIndex);
            }

            Index = smallerChildIndex;
        }
    }

    public static void main(String[] args){
        System.out.println("Hello Java");  
    }
}
