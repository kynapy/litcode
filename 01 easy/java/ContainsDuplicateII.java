// 219. Contains Duplicate II
// https://leetcode.com/problems/contains-duplicate-ii/
// Attempts: 1

import java.util.HashMap;

public class ContainsDuplicateII {
    public static boolean containsNearbyDuplicate(int[] nums, int k) {
        HashMap<Integer, Integer> lastSeen = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int curr = nums[i];
            if (lastSeen.containsKey(curr)) {
                if (i - lastSeen.get(curr) <= k) {
                    return true;
                }
            }
            lastSeen.put(curr, i);
        }

        return false;
    }

    public static void main(String[] args) {
        System.out.println(containsNearbyDuplicate(new int[] { 1, 2, 3, 1 }, 3));
        System.out.println(containsNearbyDuplicate(new int[] { 1, 0, 1, 1 }, 1));
        System.out.println(containsNearbyDuplicate(new int[] { 1, 2, 3, 1, 2, 3 }, 2));
    }
}
