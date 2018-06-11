pub fn raindrops(n: usize) -> String {

    let mut r = format!("{}{}{}",
        if n % 3 == 0 { "Pling" }else{ "" },
        if n % 5 == 0 { "Plang" }else{ "" },
        if n % 7 == 0 { "Plong" }else{ "" }
    );
    if r.is_empty(){
        r = format!("{}", n);
    }
    r

}