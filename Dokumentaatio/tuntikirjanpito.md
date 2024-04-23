# Työaikakirjanpito

| päivä | aika | mitä tein  |
| :----:|:-----| :-----|
|  26.3 | 5    | Tutustuminen unicafe ja pytest  |
|  04.09| 5    | main.py ja test sai tehty, poetry run invoke test ja muut poetry testit toimii paitsi coverage, ja jostain syystä __pycache__ on vieläkinhan tulee 
esille vaikka on __pycache__ .gitignoreissa... 
| 4.16  |  5   | Sain ainakin generoitu normaali sudoku lauta ja jotktus lisatty - check if there are no 0s, check if there are numbers on the same row, 3x3 grid and columns!  Test are only 3 tests now. Further more I need to add U.I for the project at somepoints, I still need to figure out how to implement an algorithm that tests whether a sudoku game is solvable or not - e.g if we take a 9x9 grid filled with numbers and we now took the numbers off from the grid - it doesn't make the puzzle solvable - I also have looked for pygame U.I
| :----:|:-----| :-----|
| 04.22  |  3   | - I tried implmeneting the UI by myself but sadly could get far much
| 04.23  |  5   | - Finally got the UI implemented by help by some youtube videos and other familiar projects - added 2 extra tests - 1 check if a number is prestend once in a 3x3 grid which works, but the other test has not been implemented yet, I need to use backtrack to see if the puzze actually is solvable using backtrack, but I don't know how to implement this... 
