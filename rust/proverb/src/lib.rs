pub fn build_proverb(list: &[&str]) -> String {
    match list.first() {
        Some(word) => list
            .windows(2)
            .map(|chunck| format!("For want of a {} the {} was lost.", chunck[0], chunck[1]))
            .chain(std::iter::once(format!(
                "And all for the want of a {word}."
            )))
            .collect::<Vec<String>>()
            .join("\n"),
        None => String::new(),
    }
}
