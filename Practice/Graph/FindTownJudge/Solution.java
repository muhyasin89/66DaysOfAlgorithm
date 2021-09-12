package InterviewPreparation.LeetCode.Graph.FindTownJudge;

import java.util.ArrayList;

public class Solution {
    public int findJudge(int n, ArrayList<ArrayList<Integer>> trust) {
        // to store trust value of each element
        int[] res = new int[n];

        // find trust for each element
        for (int i = 0; i < trust.size(); i++) {
            res[(trust.get(i).get(0) - 1)]--;
            res[(trust.get(i).get(1) - 1)]++;

        }

        // find element whose trust value is n-1
        for (int i = 0; i < res.length; i++) {
            if (res[i] == n - 1)
                return i + 1;
        }

        // return -1 if no element with n-1 trust found
        return -1;
    }

    public void Example1() {
        int n = 2;
        ArrayList<ArrayList<Integer>> trust = new ArrayList<ArrayList<Integer>>();
        ArrayList<Integer> rec_trust = new ArrayList<Integer>();

        rec_trust.add(1);
        rec_trust.add(2);

        trust.add(rec_trust);

        Solution solution = new Solution();

        System.out.println(solution.findJudge(n, trust));
    }

    public void Example3() {
        int n = 3;
        ArrayList<ArrayList<Integer>> trust = new ArrayList<ArrayList<Integer>>();
        ArrayList<Integer> rec_trust = new ArrayList<Integer>();
        ArrayList<Integer> rec_trust1 = new ArrayList<Integer>();
        ArrayList<Integer> rec_trust2 = new ArrayList<Integer>();

        rec_trust.add(1);
        rec_trust.add(3);

        rec_trust1.add(2);
        rec_trust1.add(3);

        rec_trust2.add(3);
        rec_trust2.add(1);

        trust.add(rec_trust);
        trust.add(rec_trust1);
        trust.add(rec_trust2);

        Solution solution = new Solution();

        System.out.println(solution.findJudge(n, trust));
    }

    public static void main(String[] args) {

        // example 2

        Solution solution = new Solution();
        solution.Example1();
        // solution.Example3();

    }
}
