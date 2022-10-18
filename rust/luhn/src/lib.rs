#![feature(test)]
extern crate test;

mod luhn_for;
mod luhn_iter;

pub fn is_valid(code: &str) -> bool {
    luhn_for::is_valid(code)
}

#[bench]
fn bench_for(b: &mut test::Bencher) {
    b.iter(|| {
        for _ in 0..100 {
            test::black_box(luhn_for::is_valid("9999 9999"));
        }
    });
}

#[bench]
fn bench_iter(b: &mut test::Bencher) {
    b.iter(|| {
        for _ in 0..100 {
            test::black_box(luhn_iter::is_valid("9999 9999"));
        }
    });
}
