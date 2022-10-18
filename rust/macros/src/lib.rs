#[macro_export]
macro_rules! hashmap {
    () => (
        ::std::collections::HashMap::new()
    );
    ( $( $x:expr => $y:expr ),+ $(,)? )=> {
        {
            let mut temp_hashmap = ::std::collections::HashMap::new();
            $(
                temp_hashmap.insert($x, $y);
            )*
            temp_hashmap
        }
    };
}
