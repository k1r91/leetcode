use std::env;
use std::collections::HashMap;

mod solution;

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() != 2 {
        println!("Usage: cargo run <method_name>");
        std::process::exit(0);
    }
    let method = &args[1];
    let mut methods: HashMap<String, fn()> = HashMap::new();
    methods.insert(String::from("pivot_index"), solution::test_pivot_index);
    methods.insert(String::from("dominant_index"), solution::test_dominant_index);
    match methods.get(method) {
        Some(value) => value(),
        None => println!("Method not found")
    }
}
