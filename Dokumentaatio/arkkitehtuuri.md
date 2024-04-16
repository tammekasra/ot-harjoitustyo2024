```mermaid
 classDiagram
    SudokuGame "1" -- "1" UI
    SudokuGame "1" -- "1..x" Players
    SudokuGame "1" -- "1" Game
    Game "1" -- "1..3" Difficulty
    Game "1" -- "1" User Interface
    Game "1" -- "1" Board
    Board "1" -- "1" Solve
```

