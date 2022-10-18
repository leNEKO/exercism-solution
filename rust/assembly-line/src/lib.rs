const DEFAULT_CARS_PER_HOUR: f64 = 221_f64;
const MINUTES_PER_HOUR: f64 = 60_f64;

fn success_rate(speed: u8) -> f64 {
    match speed {
        0 => 0.0,
        1..=4 => 1.0,
        5..=8 => 0.9,
        9..=10 => 0.77,
        _ => panic!("Too fast!"),
    }
}

pub fn production_rate_per_hour(speed: u8) -> f64 {
    DEFAULT_CARS_PER_HOUR * speed as f64 * success_rate(speed)
}

pub fn working_items_per_minute(speed: u8) -> u32 {
    (production_rate_per_hour(speed) / MINUTES_PER_HOUR) as u32
}
