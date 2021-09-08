package Basic.List;

public class PermutationExample4 {
    public static void main(String args[]) {
        // string to permutate
        String str = "come";
        // determines the length of the given string
        int length = str.length();
        PermutationExample4 per = new PermutationExample4();
        // calling the method to find the permutation
        per.permutation(str, 0, length - 1);
    }

    // function that determines the permutations
    // str: is the string to permutate
    // si: is the starting index
    // li: is the last index
    private void permutation(String str, int si, int li) {
        if (si == li)
            System.out.println(str);
        else {
            for (int i = si; i <= li; i++) {
                // calling user-defined swapping method
                str = swapChar(str, si, i);
                // calling permutation() method
                permutation(str, si + 1, li);
                str = swapChar(str, si, i);
            }
        }
    }

    // user-defined method to swap characters
    public String swapChar(String str, int i, int j) {
        char temp;
        // converts string into character array
        char[] chArray = str.toCharArray();
        temp = chArray[i];
        chArray[i] = chArray[j];
        chArray[j] = temp;
        // returns string after swapping
        return String.valueOf(chArray);
    }
}
