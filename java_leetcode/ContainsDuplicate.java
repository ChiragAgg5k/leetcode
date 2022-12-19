package LeetCode.Java;

import java.util.HashSet;

public class ContainsDuplicate {
    public static void main(String[] args) {
        //test array
        int[] testArray = {1, 1, 1, 3, 3, 4, 3, 2, 4, 2};
        System.out.println(containsDuplicate(testArray));
    }

    /**
     * Checks if given array contains duplicate values
     *
     * @param array Integer Array
     * @return boolean
     */
    public static boolean containsDuplicate(int[] array) {

        HashSet<Integer> checkArray = new HashSet<>();

        for (int n : array) {
            if (checkArray.contains(n)) {
                return true;
            }
            checkArray.add(n);
        }
        return false;
    }
}