pub fn yelly(phrase: &str) -> f32 {
    let mut uc: f32 = 0_f32;
    let mut tc: f32 = 0_f32;
    for c in phrase.chars() {
        if c.is_uppercase() {
            uc += 1_f32;
        }
        if c.is_alphabetic() {
            tc += 1_f32;
        }
    }
    return uc / tc;
}

pub fn reply(message: &str) -> &str {
    let phrase = message.trim();
    let mut tone = 0b000;
    if phrase == "" {
        tone = tone + 0b100;
    } else {
        if phrase.chars().last() == Some('?') {
            tone = tone + 0b010;
        }
        if yelly(phrase) > 0.5 {
            tone = tone + 0b001;
        }
    }

    let r = match tone {
        0b001 => "Whoa, chill out!",
        0b010 => "Sure.",
        0b011 => "Calm down, I know what I'm doing!",
        0b100 => "Fine. Be that way!",
        _ => "Whatever.",
    };
    return r;
}
