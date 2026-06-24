// 228. Summary Ranges
// https://leetcode.com/problems/summary-ranges/description/
// Attempts: 2

import java.util.ArrayList;
import java.util.List;

class SummaryRanges {
    public static List<String> summaryRanges(int[] nums) {
        List<String> result = new ArrayList<>();
        if (nums.length == 0) {
            return result;
        }

        int prev = nums[0];
        int start = nums[0];

        for (int i = 1; i < nums.length; i++) {
            int curr = nums[i];
            if (curr == prev + 1) {
                prev = curr;
            } else {
                if (prev == start) {
                    result.add(String.valueOf(start));
                } else {
                    result.add(String.format("%s->%s", String.valueOf(start), String.valueOf(prev)));
                }
                start = curr;
                prev = curr;
            }
        }

        if (prev != start) {
            result.add(String.format("%s->%s", String.valueOf(start), String.valueOf(prev)));
        } else {
            result.add(String.valueOf(start));
        }

        return result;
    }

    public static void main(String[] args) {
        System.out.println(summaryRanges(new int[] { 0, 1, 2, 4, 5, 7 }));
        System.out.println(summaryRanges(new int[] { 0, 2, 3, 4, 6, 8, 9 }));
    }
}
