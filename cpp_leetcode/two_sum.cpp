#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;

class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        unordered_map<int, int> umap;
        for (int i = 0; i < nums.size(); i++)
        {
            int diff = target - nums[i];
            if (umap.count(diff) != 0)
            {
                vector<int> res;
                res.push_back(i);
                res.push_back(umap[diff]);

                return res;
            }

            umap[nums[i]] = i;
        }

        vector<int> null;
        return null;
    }
};

int main()
{

    Solution sol;
    vector<int> nums = {3, 2, 4};
    int target = 6;
    vector<int> res = sol.twoSum(nums, target);

    cout << "[" << res[0] << "," << res[1] << "]" << endl;

    return 0;
}