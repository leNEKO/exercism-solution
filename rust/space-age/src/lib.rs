#[derive(Debug)]
pub struct Duration {
    duration: f64,
}

impl From<u64> for Duration {
    fn from(s: u64) -> Self {
        Self { duration: s as f64 }
    }
}

pub trait Planet {
    fn years_during(duration: &Duration) -> f64;
}

macro_rules! planet {
    ($name: ident, $ratio: expr) => {
        pub struct $name;
        impl Planet for $name {
            fn years_during(d: &Duration) -> f64 {
                d.duration / (31_557_600. * $ratio)
            }
        }
    };
}

planet!(Mercury, 0.2408467);
planet!(Venus, 0.61519726);
planet!(Earth, 1.);
planet!(Mars, 1.8808158);
planet!(Jupiter, 11.862615);
planet!(Saturn, 29.447498);
planet!(Uranus, 84.016846);
planet!(Neptune, 164.79132);
