import java.util.*;

public class solution {

    List<ArrayList<Integer>> arrChopped(ArrayList<Integer> arr, int L) {
        List<ArrayList<Integer>> result = new ArrayList<>();
        int arr_len = arr.size();
        for (int i = 0; i < arr_len; i += L) {
            result.add(new ArrayList<Integer>(arr.subList(i, Math.min(arr_len, i + L))));
        }

        return result;
    }

    ArrayList<Integer> combinationUtils(int arr[], int data[], int start, int end, int index, int L) {

        ArrayList<Integer> result = new ArrayList<>();
        if (index == L) {
            for (int i = 0; i < L; i++) {
                result.add(data[i]);
            }
            return result;
        }

        for (int j = start; (j <= end) && (end - j + 1 >= L - index); j++) {
            data[index] = arr[j];
            result.addAll(combinationUtils(arr, data, j + 1, end, index + 1, L));
        }

        return result;
    }

    List<ArrayList<Integer>> getAllCombinations(List<ArrayList<Integer>> result_arr, int arr[], int L) {
        int arr_len = arr.length;
        int data[] = new int[L];
        result_arr = arrChopped(combinationUtils(arr, data, 0, arr_len - 1, 0, L), L);

        return result_arr;
    }

    public static void main(String[] args) {
        int[] arr = { 1, 2, 3, 4, 5 };
        int L = 2;
        List<ArrayList<Integer>> result_arr = new ArrayList<>();

        solution obj = new solution();
        result_arr = obj.getAllCombinations(result_arr, arr, L);
        System.out.println(result_arr);

    }
}