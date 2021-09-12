package Practice.Array.ReverseString;

public class solution {

    String reverseString(String s) {
        byte[] strAsByteArray = s.getBytes();
        byte[] result = new byte[strAsByteArray.length];

        for (int i = 0; i < strAsByteArray.length; i++) {
            result[i] = strAsByteArray[strAsByteArray.length - i - 1];
        }

        return new String(result);
    }

    public static void main(String args[]) {
        String str1 = "Hello"; // olleH
        String str2 = "Test"; // tseT
        String str3 = "Howdy"; // ydwoH

        solution obj = new solution();

        System.out.println(obj.reverseString(str1));
        System.out.println(obj.reverseString(str2));
        System.out.println(obj.reverseString(str3));
    }
}
