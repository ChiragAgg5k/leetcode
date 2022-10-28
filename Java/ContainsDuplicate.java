package LeetCode.Java;

import java.util.HashSet;

public class ContainsDuplicate{
    public static void main(String[] args) {
        //test array
        int[] nums = {1,1,1,3,3,4,3,2,4,2};
        System.out.println(containsDuplicate(nums));
    }

    public static boolean containsDuplicate(int[] nums){

        // This solution is very similar to the one implemented in python.
        // Hashsets are basically set() of python in Java.

        HashSet<Integer> checknums = new HashSet<>();
        
        for(int n : nums){
            if(checknums.contains(n)){
                return true;
            }
            checknums.add(n);
        }
        return false;
    }
}