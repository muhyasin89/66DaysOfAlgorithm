import java.util.*;

public class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(target - nums[i]))
                return new int[] { map.get(target - nums[i]), i };

            map.put(nums[i], i);
        }
        return new int[] { -1, -1 };
    }

    public static void main(String args[]) {
        int[] arr = new int[] { 2, 7, 11, 15 };
        int n = 6;
        TwoSum curr_class = new TwoSum();
        int[] new_arr = curr_class.twoSum(arr, n);

        System.out.print("Sorted array: ");
        Arrays.stream(new_arr).forEach(i -> System.out.print(i + " "));
    }

}