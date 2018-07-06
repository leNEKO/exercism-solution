#![feature(test)]
extern crate test;

pub fn better_prime(x: u32) -> bool {
    let mut prime = x == 2;
    // exclude even :
    if (x > 2) && (x % 2 != 0) {
        prime = true;
        let mut k = 2;
        let n = (x as f64).sqrt(); // to find square of x only once
        while (k <= (n as u32)) && (prime == true) {
            if x % k == 0 {
                prime = false;
            }
            k = k + 1;
        }
    }
    return prime;
}

pub fn nth(n: u32) -> Option<u32> {
    let mut i = 0;
    let mut c = 0;
    if n > 0 {
        while c < n {
            i += 1;
            let p = better_prime(i);
            if p {
                c += 1;
            }
        }
        Some(i)
    } else {
        None
    }
}

pub fn slow_nth(n: u32) -> Option<u32> {
    match n {
        0 => None,
        _ => {
            let mut primes: Vec<u32> = vec![2];
            let mut num: u32 = 3;

            while primes.len() != n as usize {
                // divide num by every prime found so far,
                // if any are a factor, then num is not prime
                if primes.iter().any(|p| num % p == 0) {
                    num += 2;
                } else {
                    primes.push(num)
                }
            }
            primes.pop()
        }
    }
}

pub fn o_nth(n: u32) -> Option<u32> {
    use std::cmp;
    let limit: u32 = cmp::max(20, ((n as f64) * (n as f64).ln() * 1.3) as u32);
    let mut sieve: Vec<u32> = (0..limit + 1).map(|x| x).collect();

    for e in 0..limit + 1 {
        if sieve[e as usize] > 1 {
            let mut i = (e as usize) * (e as usize);
            while i <= limit as usize {
                sieve[i] = 0;
                i += e as usize;
            }
        };
    }

    sieve.retain(|&p| p >= 2);

    if n > 0 {
        Some(sieve[(n - 1) as usize])
    } else {
        None
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use test::Bencher;

    #[bench]
    fn bench_nth(b: &mut Bencher) {
        b.iter(|| nth(10001));
    }

    #[bench]
    fn bench_o_nth(b: &mut Bencher) {
        b.iter(|| o_nth(10001));
    }

    // #[bench]
    // fn bench_slow_nth(b: &mut Bencher) {
    //     b.iter(|| slow_nth(10001));
    // }
}
