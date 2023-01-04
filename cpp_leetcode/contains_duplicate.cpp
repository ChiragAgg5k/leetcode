#include <vector>
#include <unordered_set>
#include <map>
#include <iostream>

using namespace std;

class Solution
{
public:
    /**
     * @brief Solution to LeetCode problem 217: Contains Duplicate
     * Hashmap solution. Inrement count of each number in the vector. If count is > 1, return true.
     * @param nums vector of integers
     * @return bool
     */
    bool containsDuplicate(vector<int> &nums)
    {
        map<int, int> m;
        for (int i = 0; i < nums.size(); i++)
        {
            if (m[nums[i]])
            {
                return true;
            }

            m[nums[i]]++;
        }
        return false;
    }
};

int main()
{
    Solution s;
    vector<int> v = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10};

    cout << "Vector: ";

    for (int i : v)
    {
        cout << i << " ";
    }

    cout << '\n';
    cout << "Contains Duplicate? : ";

    if (s.containsDuplicate(v))
        cout << "True" << endl;
    else
        cout << "False" << endl;

    return 0;
}
