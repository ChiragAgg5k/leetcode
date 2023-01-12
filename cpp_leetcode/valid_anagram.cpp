#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

class Solution
{
public:
    /**
     * @brief Leetcode 242: Check if two strings are anagrams of each other.
     * Two strings are anagrams if they contain the same characters but in a different order.
     */
    bool isAnagram(string s, string t)
    {
        if (s.size() != t.size())
        {
            return false;
        }

        unordered_map<char, int> count_s;
        unordered_map<char, int> count_t;

        for (int i = 0; i < s.size(); i++)
        {
            count_s[s[i]]++;
            count_t[t[i]]++;
        }

        return count_s == count_t;
    }
};

int main()
{
    Solution solution;
    string s = "anagram";
    string t = "nagaram";

    if (solution.isAnagram(s, t))
    {
        cout << "Is valid anagram.";
    }
    else
    {
        cout << "Is not valid anagram.";
    }

    return 0;
}