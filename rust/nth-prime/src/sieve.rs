#![feature(iterator_step_by)]
pub fn sieve(limit: u32) -> Vec<u32> {
    let mut nums: Vec<u32> = (0..(limit + 1)).collect();
    nums[1] = 0;

    for i in 2..(limit + 1) {
        if i != 0 {
            println!("I: {}", i);
            for y in ((2 * i)..(limit + 1)).step_by(i as usize) {
                nums[y as usize] = 0;
            }
        }
    }
    nums.into_iter().filter(|&i| i != 0).collect::<Vec<_>>()
}
