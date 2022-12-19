#include <vector>
#include <unordered_set>
#include <map>
#include <iostream>

using namespace std;

class Solution
{
public:
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
    vector<int> v = {1, 2, 3};
    cout << s.containsDuplicate(v);
    return 0;
}
