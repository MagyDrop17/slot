// Rust program simulating a slot machine
// Tries to do the same as Pirots 3 slot
use rand::Rng;
use std::io;
use std::collections::HashMap;

static ROWS: usize = 7;
static COLUMNS: usize = 6;
static SYMBOLS: [&str; 7] = ["R", "G", "B", "Y", "X", "T", "P"];
static PAYOUTS: [u32; 7] = [20, 20, 20, 20, 5, 10, 5];

fn create_symbols_colors_collection() -> HashMap<&'static str, &'static str> {
    let mut symbols_colors = HashMap::new();
    symbols_colors.insert("R", "red");
    symbols_colors.insert("G", "green");
    symbols_colors.insert("B", "blue");
    symbols_colors.insert("Y", "yellow");
    symbols_colors.insert("X", "black");
    symbols_colors.insert("T", "purple");
    symbols_colors.insert("P", "pink");
    symbols_colors
}

fn main() {
    
    let symbols_colors = create_symbols_colors_collection();
    
    println!("Symbols and their colors:");
    for (symbol, color) in &symbols_colors {
        println!("{}: {}", symbol, color);
    }

    println!("Welcome to the Slot Machine!");
   
}
