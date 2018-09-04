extern crate pythagorean_triplet;

#[test]
fn test_answer() {
    assert_eq!(pythagorean_triplet::find(), Some(31875000));
}

// custom test on the 40 first primary pythagorean triplet
#[test]
fn test_sub_answer() {
    let vec = [
        [3, 4, 5],
        [5, 12, 13],
        [8, 15, 17],
        [7, 24, 25],
        [20, 21, 29],
        [12, 35, 37],
        [9, 40, 41],
        [28, 45, 53],
        [11, 60, 61],
        [16, 63, 65],
        [33, 56, 65],
        [48, 55, 73],
        [13, 84, 85],
        [36, 77, 85],
        [39, 80, 89],
        [65, 72, 97],
        [20, 99, 101],
        [60, 91, 109],
        [15, 112, 113],
        [44, 117, 125],
        [88, 105, 137],
        [17, 144, 145],
        [24, 143, 145],
        [51, 140, 149],
        [85, 132, 157],
        [119, 120, 169],
        [52, 165, 173],
        [19, 180, 181],
        [57, 176, 185],
        [104, 153, 185],
        [95, 168, 193],
        [28, 195, 197],
        [84, 187, 205],
        [133, 156, 205],
        [21, 220, 221],
        [140, 171, 221],
        [60, 221, 229],
        [105, 208, 233],
        [120, 209, 241],
        [32, 255, 257],
    ];
    for t in vec.iter() {
        let sum = t.iter().fold(0, |acc, x| acc + x);
        let prod = t.iter().fold(1, |acc, x| acc * x);
        println!("triangle: {:?}, sum: {}, prod: {}", t, sum, prod);
        assert_eq!(pythagorean_triplet::_find(sum), Some(prod));
    }
}
