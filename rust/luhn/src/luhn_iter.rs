pub fn is_valid(code: &str) -> bool {
    if !code
        .chars()
        .all(|c| c.is_ascii_digit() || c.is_ascii_whitespace())
    {
        return false;
    }

    let digits = code
        .chars()
        .rev()
        .filter(|c| c.is_numeric())
        .map(|c| c.to_digit(10).unwrap())
        .collect::<Vec<u32>>();

    if digits.len() < 2 {
        return false;
    }

    code_sum(digits) % 10 == 0
}

fn code_sum(digits: Vec<u32>) -> u32 {
    let mut odds: u32 = 0;
    let mut evens: u32 = 0;

    digits.chunks(2).for_each(|chunk| {
        let value = chunk.get(1).unwrap_or(&0_u32) * 2;
        let quotient = value / 10;
        let remainder = value % 10;
        evens += quotient + remainder;
        odds += chunk.first().unwrap_or(&0_u32);
    });

    odds + evens
}
