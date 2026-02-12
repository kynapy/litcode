// 1207. Unique Number of Occurrences
// https://leetcode.com/problems/unique-number-of-occurrences/description/
// Attempts: 1

use std::collections::HashMap;
use std::collections::HashSet;

fn main() {
    pub fn unique_occurrences(arr: Vec<i32>) -> bool {
        let mut occurrences = HashMap::new();
        for i in arr {
            if occurrences.contains_key(&i) {
                occurrences.insert(i, occurrences.get(&i).unwrap() + 1);
            } else {
                occurrences.insert(i, 1);
            }
        }

        let mut count = HashSet::new();
        for occurrence in occurrences.values() {
            if count.contains(occurrence) {
                return false;
            } else {
                count.insert(occurrence);
            }
        }
        true
    }

    // TEST CASES
    println!("{}", unique_occurrences([1, 2, 2, 1, 1, 3].to_vec()));
    println!("{}", unique_occurrences([1, 2].to_vec()));
    println!(
        "{}",
        unique_occurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0].to_vec())
    );
}
