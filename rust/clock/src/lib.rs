use std::fmt;

#[derive(PartialEq, Debug)]
pub struct Clock {
    minutes: i32,
}

impl Clock {
    const HOUR: i32 = 60;
    const DAY: i32 = 24 * Self::HOUR;

    pub fn new(hours: i32, minutes: i32) -> Self {
        let remainder: i32 = (hours * Self::HOUR + minutes) % Self::DAY;
        Clock {
            minutes: match remainder >= 0 {
                true => remainder,
                false => remainder + Self::DAY,
            },
        }
    }

    pub fn add_minutes(self, minutes: i32) -> Self {
        Self::new(0, self.minutes + minutes)
    }
}

impl fmt::Display for Clock {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        let hours = self.minutes / Self::HOUR;
        let minutes = self.minutes % Self::HOUR;
        write!(f, "{:02}:{:02}", hours, minutes)
    }
}
