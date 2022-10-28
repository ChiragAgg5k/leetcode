class Solution(object):
    def isValid(self, s):

        """
        In this solution,
        we first store our available options in the given order in a hashmap
        while iterating the given string , we append it to a list (stack),
        if its a opening one (aka not present in hashmap's keys)
        
        now if our hashmap is empty, that means a closing tag is iterated without a opening one existing

        2nd scenario , we iterated a closing para but it doesnt match 

        in these cases we will stop iterationg and return false.

        if both dont satisfy , we will remove that opening tag from our stack and iterate rest of the string.

        This solution is especially genius for scenario like this {[()]}.
        """
        
        match = {")":"(","}":"{","]":"["}
        l = []

        for i in s:
            if i not in match:
                l.append(i)
                continue

            if not l or l[-1] != match[i]:
                return False
            l.pop()

        return not l