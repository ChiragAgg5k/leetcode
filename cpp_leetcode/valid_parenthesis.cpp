#include <vector>
#include <string>
#include <unordered_map>
#include <iostream>
using namespace std;

class Solution
{
public:
    bool isValid(string s)
    {
        vector<char> stack;
        unordered_map<char, char> hashmap;
        int n;

        hashmap[')'] = '(';
        hashmap[']'] = '[';
        hashmap['}'] = '{';

        for (char bracket : s)
        {
            if (!hashmap.count(bracket))
            {
                stack.push_back(bracket);
                continue;
            }

            n = stack.size();
            if (n == 0 || (stack[n - 1] != hashmap[bracket]))
                return false;

            stack.pop_back();
        }

        return stack.size() == 0;
    }
};

int main()
{
    Solution solution;
    string test_string1 = "()[]{}";
    string test_string2 = "(]";

    cout << solution.isValid(test_string1) << '\n';
    cout << solution.isValid(test_string2) << '\n';
}