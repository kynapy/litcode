// 290. Word Pattern
// https://leetcode.com/problems/word-pattern/description/
// Attempts: 2

import java.util.HashMap;

public class WordPattern {
    public static boolean wordPattern(String pattern, String s) {
        HashMap<Character, String> patternToWord = new HashMap<>();
        HashMap<String, Character> wordToPattern = new HashMap<>();

        String[] words = s.split(" ");
        if (words.length != pattern.length()) {
            return false;
        }

        for (int i = 0; i < words.length; i++) {
            char letter = pattern.charAt(i);
            String word = words[i];

            if (patternToWord.containsKey(letter)) {
                if (!patternToWord.get(letter).equals(word)) {
                    return false;
                }
            } else {
                patternToWord.put(letter, word);
            }

            if (wordToPattern.containsKey(word)) {
                if (!wordToPattern.get(word).equals(letter)) {
                    return false;
                }
            } else {
                wordToPattern.put(word, letter);
            }
        }

        return true;
    }

    // TEST CASES
    public static void main(String[] args) {
        System.out.println(wordPattern("abba", "dog cat cat dog"));
        System.out.println(wordPattern("abba", "dog cat cat fish"));
        System.out.println(wordPattern("aaaa", "dog cat cat dog"));
        System.out.println(wordPattern("aaa", "aa aa aa aa"));
    }
}
