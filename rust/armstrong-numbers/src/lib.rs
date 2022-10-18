pub fn is_armstrong_number(num: u32) -> bool {
    let digits_string = num.to_string();

    let digits_count = digits_string.chars().count();

    let armstrong_sum = digits_string
        .chars()
        .into_iter()
        .map(|digit_char| digit_char.to_digit(10).unwrap().pow(digits_count as u32))
        .sum();

    num == armstrong_sum
}
