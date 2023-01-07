#include <iostream>
#include <vector>

class Solution
{
public:
    /**
     * @brief Search for a target element in a sorted array using binary search.
     *
     * Time complexity: O(log n)
     * Space complexity: O(1)
     *
     * @param nums sorted vector of integers
     * @param target target element
     *
     * @return index of target element if found, -1 otherwise
     */
    int search(std::vector<int> &nums, int target)
    {

        int left = 0;
        int right = nums.size() - 1;
        int mid;

        while (left <= right)
        {

            mid = (left + right) / 2;

            if (nums[mid] > target)
            {
                right = mid - 1;
            }
            else if (nums[mid] < target)
            {
                left = mid + 1;
            }
            else
            {
                return mid;
            }
        }

        return -1;
    }
};

int main()
{
    Solution solution;
    int size, target, n;
    std::vector<int> array;

    std::cout << "Enter size of the array: ";
    std::cin >> size;

    std::cout << "Enter elements of the array (space separated): ";

    for (int i = 0; i < size; i++)
    {
        std::cin >> n;
        array.push_back(n);
    }

    std::cout << "Enter target element: ";
    std::cin >> target;

    int res = solution.search(array, target);
    if (res == -1)
    {
        std::cout << "Element not present in the array." << std::endl;
    }
    else
    {
        std::cout << "Element found at index: " << res << std::endl;
    }

    return 0;
}