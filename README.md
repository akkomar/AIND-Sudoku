# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  

A: Naked twins are two boxes in an unit that both contain two, same possible values. Although we don't know which box
should have been assigned with which value, we know for sure that no other boxes in the same unit can contain either
of these values (this is our _constraint_).

For each unit (row, column, square, diagonal) we look for boxes with exactly two, same possible values, if such boxes exist,
we remove these values from other boxes in this row. Thus, we are _propagating_ the constraint (defined above)
to each unit. Each removal in this process is reducing our search space, which makes solving sudoku faster.

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: The process of constraint propagation consists of iteratively applying sudoku strategies over each grid unit.
In diagonal sudoku problem, we have two more constraints (comparing to plain sudoku) - numbers on two diagonals
can appear only once. We solve this problem by defining two additional units for these diagonals and including 
them in process of applying strategies.


### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.