package LeetCode.Java;

import java.util.HashSet;

public class ContainsDuplicate{
    public static void main(String[] args) {
        //test array
        int[] testArray = {1,1,1,3,3,4,3,2,4,2};
        System.out.println(containsDuplicate(testArray));
    }

    public static boolean containsDuplicate(int[] array){

        // This solution is very similar to the one implemented in python.
        // Hashsets are basically set() of python in Java.

        HashSet<Integer> checkArray = new HashSet<>();
        
        for(int n : array){
            if(checkArray.contains(n)){
                return true;
            }
            checkArray.add(n);
        }
        return false;
    }
}