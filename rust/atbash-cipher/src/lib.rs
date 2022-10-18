fn codec(input: &str) -> Vec<char> {
    input
        .chars()
        .filter(char::is_ascii_alphanumeric)
        .map(|c| match c.is_ascii_alphabetic() {
            true => (b'z' - c.to_ascii_lowercase() as u8 + b'a') as char,
            false => c,
        })
        .collect()
}

pub fn encode(plain: &str) -> String {
    codec(plain)
        .chunks(5)
        .map(|c| c.iter().collect::<String>())
        .collect::<Vec<String>>()
        .join(" ")
}

pub fn decode(cipher: &str) -> String {
    codec(cipher).iter().collect()
}
