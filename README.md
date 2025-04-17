# 🎮 Sudoku Game with Pygame

This is a fun, interactive Sudoku game built using Python and Pygame. It features randomly generated Sudoku puzzles, color feedback for correct and incorrect answers, and even some nostalgic background music.

---

## 📁 Structure


---

## 🚀 How It Works

- A Sudoku puzzle is generated via `SudokuGenerator.py`, which uses helper logic from the library `sudoku`.
- The puzzle is displayed on a 9x9 grid rendered with Pygame.
- Players can click on empty cells and enter numbers (1-9).
- Press `Enter` to check your solution.
- Correct cells are highlighted in green, incorrect ones in red.
- Background music plays on a loop to make the game more enjoyable.

---

## 🎮 Controls

- 🖱️ Click on an empty cell to select it.
- ⌨️ Press any number key (1–9) to fill the selected cell.
- ⏎ Press `Enter` to check your solution.
- ⌫ Press `Backspace` (not fully implemented yet).
- ❌ Click the close window button or press `Esc` to quit.

---

## 🎨 Features

- ✅ Random Sudoku puzzle generation
- ✅ Fully playable grid with cell selection
- ✅ Number input using keyboard
- ✅ Solution checker with color feedback
- ✅ Background music (Rick Astley approved 😉)
- 🔄 Auto-refresh display using Pygame
- 🚫 No external UI libraries required

---

## 📦 Requirements

- Python
- `pygame`
- `sudoku` (Python library for generating/solving puzzles)

Install dependencies with:

```bash
pip install pygame sudoku
pip install pygame pygame
