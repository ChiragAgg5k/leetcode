package LeetCode.Java;

public class ValidPalindrome {

    public static void main(String[] args) {
        System.out.println(isPalindrome("A man, a plan, a canal: Panama"));
    }

    /**
     * Method to check if given string is a palindrome.
     * Ignores anything non-alphanumeric
     * @param s String
     * @return true if palindrome, else false
     */
    public static boolean isPalindrome(String s) {

        StringBuilder alphaStr = new StringBuilder();
        StringBuilder revAlphaStr = new StringBuilder();

        for (char i : s.toCharArray()) {

            if (i >= '0' && i <= '9' || i >= 'a' && i <= 'z' || i >= 'A' && i <= 'Z') {
                alphaStr.append(Character.toLowerCase(i));
            }
        }

        for (int i = alphaStr.length() - 1; i >= 0; i--) {
            revAlphaStr.append(alphaStr.charAt(i));
        }

        return alphaStr.toString().equals(revAlphaStr.toString());
    }
}
