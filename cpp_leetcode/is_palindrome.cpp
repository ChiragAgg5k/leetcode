#include <iostream>
#include <string>

using namespace std;

class Solution
{
public:
    /**
     * @brief Solution to LeetCode problem 125: Valid Palindrome
     * Two pointers, one from the beginning and one from the end.
     * Move the pointers until they are on alphanumeric characters.
     * @param s string
     * @return bool
     */
    bool isPalindrome(string s)
    {
        int i = 0;
        int j = s.size() - 1;

        while (i < j)
        {
            while (!isalnum(s[i]) && i < j)
            {
                i++;
            }
            while (!isalnum(s[j]) && i < j)
            {
                j--;
            }
            if (tolower(s[i]) != tolower(s[j]))
            {
                return false;
            }
            i++;
            j--;
        }

        return true;
    }
};

int main()
{
    Solution sol;
    string s = "A man, a plan, a canal: Panama";
    cout << sol.isPalindrome(s) << endl;
}