pub fn twofer(name: &str) -> String {
    let n = if name.is_empty() { "you" } else { name };
    format!("One for {}, one for me.", n)
}
