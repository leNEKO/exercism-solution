pub fn is_valid(code: &str) -> bool {
    let (pos, sum) = luhn_sum(code);

    pos > 1 && sum % 10 == 0
}

fn luhn_sum(code: &str) -> (u32, u8) {
    let mut pos = 0;
    let mut sum = 0;

    for byte in code.bytes().rev() {
        match byte {
            b' ' => (),
            _ => {
                if !(b'0'..=b'9').contains(&byte) {
                    return (0, 0);
                }
                let digit = byte - b'0';

                if pos % 2 == 0 {
                    sum += digit
                } else {
                    sum += {
                        let value = digit * 2;
                        let quotient = value / 10;
                        let remainder = value % 10;

                        quotient + remainder
                    }
                }
                pos += 1;
            }
        }
    }

    (pos, sum)
}
