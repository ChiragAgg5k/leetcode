package LeetCode.Java;

public class ValidPalindrome {

    public static void main(String[] args) {
        System.out.println(isPalindrome("A man, a plan, a canal: Panama"));
    }

    public static boolean isPalindrome(String s) {

        // intellij thinks string builders are better for concatenation than +=
        StringBuilder alphaStr = new StringBuilder();
        StringBuilder revAlphaStr = new StringBuilder();

        // converting string to alphanumeric
        for (char i : s.toCharArray()) {

            // another way is to use Character.isLetterDigit()
            if (i >= '0' && i <= '9' || i >= 'a' && i <= 'z' || i >= 'A' && i <= 'Z') {
                alphaStr.append(Character.toLowerCase(i));
            }
        }

        // reversing the resulting string
        for (int i = alphaStr.length() - 1; i >= 0; i--) {
            revAlphaStr.append(alphaStr.charAt(i));
        }

        /* Uncomment for debugging
        *
        * System.out.println(alphaStr);
          System.out.println(revAlphaStr); */

        return alphaStr.toString().equals(revAlphaStr.toString());
    }
}
