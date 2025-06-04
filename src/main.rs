use eframe::egui;
use rand::prelude::*;

const ROWS: usize = 7;
const COLS: usize = 6;

const SYMBOLS: [char; 7] = ['R', 'G', 'B', 'Y', 'X', 'T', 'P'];
const WEIGHTS: [u32; 7] = [20, 20, 20, 20, 5, 10, 5];

fn symbol_color(symbol: char) -> egui::Color32 {
    match symbol {
        'R' => egui::Color32::RED,
        'G' => egui::Color32::GREEN,
        'B' => egui::Color32::BLUE,
        'Y' => egui::Color32::YELLOW,
        'X' => egui::Color32::BLACK,
        'T' => egui::Color32::from_rgb(255, 165, 0), // orange
        'P' => egui::Color32::from_rgb(165, 42, 42), // brown
        _ => egui::Color32::GRAY,
    }
}

fn generate_grid() -> [[char; COLS]; ROWS] {
    let mut rng = thread_rng();
    let total_weight: u32 = WEIGHTS.iter().sum();
    let mut grid = [[' '; COLS]; ROWS];

    for row in &mut grid {
        for cell in row.iter_mut() {
            let mut roll = rng.gen_range(0..total_weight);
            for (i, &weight) in WEIGHTS.iter().enumerate() {
                if roll < weight {
                    *cell = SYMBOLS[i];
                    break;
                }
                roll -= weight;
            }
        }
    }

    grid
}

struct SlotApp {
    grid: [[char; COLS]; ROWS],
}

impl Default for SlotApp {
    fn default() -> Self {
        Self {
            grid: generate_grid(),
        }
    }
}

impl eframe::App for SlotApp {
    fn update(&mut self, ctx: &egui::Context, _frame: &mut eframe::Frame) {
        egui::CentralPanel::default().show(ctx, |ui| {
            ui.vertical_centered(|ui| {
                for row in self.grid.iter() {
                    ui.horizontal(|ui| {
                        for &cell in row.iter() {
                            ui.colored_label(symbol_color(cell), format!(" {} ", cell));
                        }
                    });
                }

                ui.add_space(20.0);
                if ui.button("Spin / Regenerate Grid").clicked() {
                    self.grid = generate_grid();
                }
            });
        });
    }
}

fn main() -> eframe::Result<()> {
    let options = eframe::NativeOptions::default();
    eframe::run_native("Pirots3-style Grid", options, Box::new(|_| Box::new(SlotApp::default())))
}