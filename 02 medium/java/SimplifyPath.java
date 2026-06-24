// 71. Simplify Path
// https://leetcode.com/problems/simplify-path/description/
// Attempts: 2

import java.util.Stack;

class SimplifyPath {
    public static String simplifyPath(String path) {
        String[] words = path.split("/");
        String result = "";
        Stack<String> stack = new Stack<>();

        for (int i = 0; i < words.length; i++) {
            String curr = words[i];
            if (curr.equals("..")) {
                if (stack.size() != 0) {
                    stack.pop();
                }
            } else if (curr.equals(".") || curr.length() == 0) {
                continue;
            } else {
                stack.push(curr);
            }
        }

        if (stack.size() == 0) {
            return "/";
        }

        while (stack.size() > 0) {
            result = "/" + stack.pop() + result;
        }

        return result;
    }

    public static void main(String[] args) {
        System.out.println(simplifyPath("/home/"));
        System.out.println(simplifyPath("/home//foo/"));
        System.out.println(simplifyPath("/home/user/Documents/../Pictures"));
        System.out.println(simplifyPath("/../"));
        System.out.println(simplifyPath("/.../a/../b/c/../d/./"));
    }
}
