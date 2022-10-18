pub enum CalculatorInput {
    Add,
    Subtract,
    Multiply,
    Divide,
    Value(i32),
}

fn operate<F>(stack: &mut Vec<i32>, f: F) -> ()
where
    F: Fn(&i32, &i32) -> i32,
{
    let b = stack.pop()?;
    let a = stack.pop()?;

    stack.push(f(&a, &b))
}

pub fn evaluate(inputs: &[CalculatorInput]) -> Option<i32> {
    // early return None if inputs is invalid
    if !matches!(inputs.first(), Some(CalculatorInput::Value(_))) {
        return None;
    }

    let mut stack: Vec<i32> = vec![];

    for input in inputs {
        match input {
            CalculatorInput::Value(value) => stack.push(*value),
            CalculatorInput::Add => operate(&mut stack, |a, b| a + b),
            CalculatorInput::Subtract => operate(&mut stack, |a, b| a - b),
            CalculatorInput::Multiply => operate(&mut stack, |a, b| a * b),
            CalculatorInput::Divide => operate(&mut stack, |a, b| a / b),
        };
    }

    // check for complete inputs
    (stack.len() == 1 ).then(|| stack[0])
}
