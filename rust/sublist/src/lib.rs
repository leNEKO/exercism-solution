#[derive(Debug, PartialEq)]
pub enum Comparison {
    Equal,
    Sublist,
    Superlist,
    Unequal,
}

pub fn sublist<T: PartialEq>(first_list: &[T], second_list: &[T]) -> Comparison {
    if first_list == second_list {
        return Comparison::Equal;
    }

    if is_a_slice(first_list, second_list) {
        return Comparison::Sublist;
    }

    if first_list.len() > second_list.len() && is_a_slice(second_list, first_list) {
        return Comparison::Superlist;
    }

    Comparison::Unequal
}

fn is_a_slice<T: PartialEq>(part: &[T], full: &[T]) -> bool {
    if part.is_empty() {
        return true;
    }

    full.windows(part.len()).any(|w| w == part)
}
