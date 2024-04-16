```mermaid
 classDiagram
    SudokuGame "1" -- "1" UI
    UI "1" -- "1..x" Account creation
    UI "1" -- "1..x" Players Score
    Account creation "1" -- "1" Game
    Game "1" -- "1..3" Difficulty
    Game "1" -- "1" User Interface
    User Interface "1" -- "1" Game
    Game "1" -- "1" Board
    Board "1" -- "1" Test Algorithm if its solvable
    Board "1" -- "1" Solve 
    Game "1" -- "1..x" Points
    Game "1" -- Timer
    Game "1" -- Hints
    Hints "1" -- "-1" Points
    
```

