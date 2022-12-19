package LeetCode.Java;

import java.util.HashMap;
import java.util.Stack;

public class ValidParentheses {
    public static void main(String[] args) {
        System.out.println(isValid("{([])}"));
    }

    public static boolean isValid(String s) {

        // I would highly suggest watching neetcode's explanation for this solution

        Stack<Character> stack = new Stack<>();
        HashMap<Character, Character> map = new HashMap<>();

        map.put(')', '(');
        map.put(']', '[');
        map.put('}', '{');

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (!map.containsKey(c)) {
                stack.add(c);
                continue;
            }

            if (stack.isEmpty() || stack.lastElement() != map.get(c)) {
                return false;
            }

            stack.pop();
        }

        return (stack.isEmpty());
    }
}