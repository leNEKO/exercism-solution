use std::collections::HashSet;

fn sorted_chars(lowercase_word: &str) -> Vec<char> {
    let mut word_chars = lowercase_word.chars().collect::<Vec<char>>();
    word_chars.sort_unstable();

    word_chars
}

pub fn anagrams_for<'a>(word: &str, possible_anagrams: &[&'a str]) -> HashSet<&'a str> {
    let lowercase_word = word.to_lowercase();
    let expected_chars = sorted_chars(&lowercase_word);

    possible_anagrams
        .iter()
        .cloned()
        .filter(|possible_anagram| {
            let lowercase_possible_anagram = possible_anagram.to_lowercase();
            lowercase_word.len() == lowercase_possible_anagram.len()
                && lowercase_word != lowercase_possible_anagram
                && expected_chars == sorted_chars(&lowercase_possible_anagram)
        })
        .collect::<HashSet<&'a str>>()
}
