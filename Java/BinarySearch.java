package LeetCode.Java;

public class BinarySearch {

    public static void main(String[] args) {

        int[] testArray = {1, 2, 3, 4, 5, 6, 7, 8, 9};
        System.out.println(binarySearch(testArray, 11));
        System.out.println(binarySearch(testArray,2));
    }

    /**
     * Implementation of the classic binary search algorithm in Java
     *
     * @param array  Must be sorted
     * @param target Integer to search for
     * @return index pos. of the target integer. If not present , returns -1
     */
    public static int binarySearch(int[] array, int target) {

        int l = 0;
        int r = array.length - 1;

        while (l <= r) {

            int mid = (l + r) / 2;

            if (array[mid] > target) {
                r = mid - 1;
            } else if (array[mid] < target) {
                l = mid + 1;
            } else {
                return mid;
            }
        }
        return -1;
    }
}
