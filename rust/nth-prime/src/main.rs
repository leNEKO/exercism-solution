#![feature(iterator_step_by)]
extern crate nth_prime as np;
use std::env;

fn main() {
    // let args: Vec<String> = env::args().collect();
    // println!("{}", np::nth(args[1].parse::<u32>().unwrap()).unwrap());
    println!("{}", np::better_prime(10001));
}
