import java.sql.Array;
import java.util.*;

public class solution {
    ArrayList<Integer> convertArrayList(int arr[], int n, int arr_len, int L){
        ArrayList<Integer> result = new ArrayList<>();
        for(int i=0; i<L;i++){
            result.add(arr[n%arr_len]);
            n /=arr_len;
        }

        return result;

    }

    List<ArrayList<Integer>> getAllPermutations(List<ArrayList<Integer>> result_arr, int arr[], int L){
        int arr_len = arr.length;

        for(int  i=0; i< (int)Math.pow(arr_len, L); i++){
            result_arr.add(convertArrayList(arr, i, arr_len, L));
        }

        return result_arr;
    }

    public static void main(String[] args) {
        int arr[] = { 1, 2, 3, 4, 5 };
        int L = 2;

        List<ArrayList<Integer>> result_arr = new ArrayList<>();
        solution obj =new solution();

        result_arr = obj.getAllPermutations(result_arr, arr, L);
        System.out.println(result_arr);
    }
}
