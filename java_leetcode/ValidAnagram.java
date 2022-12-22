import java.util.HashMap;

public class ValidAnagram {

    public static void main(String[] args) {
        System.out.println(isValid("anagram", "nmgraaa"));
    }

    /**
     * Method to check if two given strings are Anagram or not.
     * @param s String 1
     * @param t String 2
     * @return true if Anagram, else false
     */
    public static boolean isValid(String s, String t) {

        if (s.length() != t.length()) {
            return false;
        }

        HashMap<Character, Integer> countS = new HashMap<>();
        HashMap<Character, Integer> countT = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            countS.put(s.charAt(i), 1 + countS.getOrDefault(s.charAt(i), 0));
            countT.put(t.charAt(i), 1 + countT.getOrDefault(t.charAt(i), 0));
        }
        return countS.equals(countT);
    }
}