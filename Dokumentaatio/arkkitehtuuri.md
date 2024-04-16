```mermaid
 classDiagram
    SudokuGame "1" -- "1" UI
    UI "1" -- "1..x" Account creation
    SudokuGame "1" -- "1..x" Players Score
    SudokuGame "1" -- "1" Game
    Game "1" -- "1..3" Difficulty
    Game "1" -- "1" User Interface
    User Interface "1" -- "1" The game
    Game "1" -- "1" Board
    Board "1" -- "1" Solve
    Game "1" - "1..x" Point
    Game "1" -- Timer
    
```

