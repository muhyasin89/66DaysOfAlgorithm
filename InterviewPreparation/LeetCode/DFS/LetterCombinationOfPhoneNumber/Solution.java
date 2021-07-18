package interview_preparation.LeetCode.DFS.LetterCombinationOfPhoneNumber;

public class Solution {
    public List letterCombinations(String digits) {
        // store our answer
        ArrayList<String> result = new ArrayList<>();

        // check input and call DFS
        if (digits != null && digits.length() > 0) {
            String map[] = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"}
            dfs(digits, map, result, new StringBuilder(), 0);
        }

        return result;
    }

    public void dfs(String digits, String[] map, ArrayList<String> result, StringBuilder sb, int index) {
        // when we reach the end of phone number (digits), we should have a valid letter
        // combination
        if (index == digits.length()) {
            result.add(sb.toString());
            return;
        }

        // get current digit/what letter it represents
        int digit = Character.getNumericValue(digits.charAt(index));
        String letters = map[digit];

        // try adding each letter to the string we've build so far
        for (int i = 0; i < letters.length(); i++) {
            char ch = letters.charAt(i);
            sb.append(ch);
            dfs(digits, map, result, sb, index + 1); // take the string and move on to the next digit
            sb.deleteCharAt(sb.length() - 1);
        }
    }
}
