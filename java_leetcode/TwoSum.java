import java.util.Arrays;
import java.util.HashMap;

public class TwoSum {

    public static void main(String[] args) {

        int[] testArray = {2, 7, 11, 15};
        int testTarget = 9;
        System.out.println(Arrays.toString(twoSum(testArray, testTarget)));

    }

    /**
     * Function to find indexes of two numbers in an array which add up to the given target number
     *
     * @param nums   int[]
     * @param target int
     * @return int[] , null if sum not found
     */
    public static int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hashmap = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {

            int diff = target - nums[i];

            if (hashmap.containsKey(diff)) {
                return new int[]{hashmap.get(diff), i};
            }
            hashmap.put(nums[i], i);
        }
        return null;
    }
}
