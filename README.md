<h1 align="center">:game_die: Sudoku with Solver :jigsaw:</h1>

This python-based Sudoku solver employs backtracking, which is essentially retreating back to the previous step or solution when we discover that our current solution cannot be completed. To implement the algorithm, I employed this backtracking principle.

## :electric_plug: What to Expect
- Sudoku GUI 

![Sudoku GUI](https://user-images.githubusercontent.com/62080362/126641053-6fd911b2-7502-4096-b0f2-3917bfecaacf.png)

- Sudoku Solver in Terminal

![Solver In Terminal](https://user-images.githubusercontent.com/62080362/126643964-13489a46-75dd-4c95-a5d5-91c88e95cc77.png)


## :abacus: Backtracking Logic Used
<p>Backtracking is a <em>depth-first search</em> (as opposed to a <em>breadth-first search</em>) in that it will fully explore one branch to a possible answer before going on to the next. Despite the fact that there are approximately 5.96 × 11<sup>26</sup> final grids, a brute force technique can be a useful method for solving Sudoku problems.</p>

<p>A brute force technique explores vacant cells in a specific order, sequentially filling in digits or backtracking if the number is discovered to be invalid. In a nutshell, a program would solve a puzzle by placing the digit "1" in the first cell and checking whether it is permitted. The method moves to the next cell and places a "1" in that cell if there are no violations (checking row, column, and box constraints). When checking for violations, if the value "1" is found to be invalid, the value is advanced to "2." If the algorithm discovers a cell where none of the nine digits are permitted, it leaves that cell blank and returns to the previous cell. After that, the value in that cell is increased by one. This process is continued until the last (81<sup>st</sup>) cell's acceptable value is discovered.</p>

## :high_brightness: Advantages of backtracking
- A solution is guaranteed (as long as the puzzle is valid).
- Solving time is mostly unrelated to degree of difficulty.
- The algorithm (and therefore the program code) is simpler than other algorithms, especially compared to strong algorithms that ensure a solution to the most difficult puzzles.

### :no_entry_sign: Limitations of this program
The disadvantage of this backtracking strategy is that it may take longer to solve problems than algorithms based on deductive procedures. According to one programmer,([Read Here](https://www.flickr.com/photos/npcomplete/2341937186) & [Here](https://www.flickr.com/photos/npcomplete/2384354604)), solving a Sudoku can take as few as 15,000 cycles or as much as 900,000 cycles, with each cycle representing the change in location of a "pointer" as it passes through the cells.

## :hammer_and_wrench: Tools & Languages Used
- Anaconda Version 4.10.1
- Python Version 3.8.8 
- PyGame - PyGame is a set of cross-platform Python tools for creating video games. It offers sound and graphics libraries that can be utilized with the Python programming language.
- `time` Module - Time access and conversions. This module provides various time-related functions.

---
## :v: Contributing

You wanna contribute? Wow amazing. That's great to hear.

After cloning & setting up the local project you can push the changes to your github fork and make a pull request.

### Pushing the changes

```bash
git add .
git commit -m "feat: added new stuff"
git push YOUR_REPO_URL BRANCH_NAME
```

---

<h3 align="center"> This code was built with :heart: and alot of Coffee:coffee:</h3>
