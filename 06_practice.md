
# Python Programming Tasks with Hints


## Task 1: Fibonacci Sequence Generator
Develop a program that asks the user how many Fibonacci numbers to generate and then generates them. The Fibonacci sequence is a series of numbers where the next number is the sum of the two preceding ones, usually starting with 0 and 1.

## Task 2: Tic Tac Toe Game
Develop a program that allows two players to play a game of tic-tac-toe. Use a 3x3 grid and ask the players for their moves turn by turn.
```
Variable akueller spieler --> Welcher spieler ist am Zug?
Loop solang keiner gewonnen hat:
    Loop eingabe:
        Aktueller Spieler gibt Koordinaten ein
        Prüfen, ob an den Koordinaten etwas ist?
        Wenn ja:
            Neue Koordinaten
        Wenn nein:
            exit loop
    Koordinaten setzen
    Prüfen, ob der aktuelle Spieler gewonnen hat?
    Wenn ja:
        Aktueller Spieler hat gewonnen!
    Wenn nein:
        Prüfen, ob noch Felder frei sind?
        Wenn ja:
            Spieler wechsel und nächster Zug
        Wenn nein:
            unentschieden!
```
## Task 3: Game of Life
Implement the Game of Life. The Game of Life is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves. The rules are as follows:

- Any live cell with fewer than two live neighbours dies, as if by underpopulation.
- Any live cell with two or three live neighbours lives on to the next generation.
- Any live cell with more than three live neighbours dies, as if by overpopulation.
- Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

### Use the Help Functions