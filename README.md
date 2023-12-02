# Game-of-Life

## Overview
This is a console-based implementation of Conway's Game of Life. The following description was extracted from [Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life):

The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, live or dead (or populated and unpopulated, respectively). Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:
- any live cell with fewer than two live neighbours dies, as if by underpopulation
- any live cell with two or three live neighbours lives on to the next generation
- any live cell with more than three live neighbours dies, as if by overpopulation
- any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction
  
The initial pattern constitutes the seed of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed, live or dead; births and deaths occur simultaneously, and the discrete moment at which this happens is sometimes called a **tick**.

## Features
- built using layered architecture
- changes made to the repository persist
- patterns are read from a text file
- the user is allowed to save and load board configurations to text files specified by them
- the user can place predefined patterns on the board
- the user can advance the state of the game ('tick') multiple times with a single command, allowing them to control the game's progression as they wish.
  
## Technologies used
- Pyhton
- Python's unittest framework

## Screenshots
![image](https://github.com/Rares1707/Game-of-Life/assets/115061254/b57ce082-18f1-420d-be8a-c5f6541291c6)
![image](https://github.com/Rares1707/Game-of-Life/assets/115061254/11454ba6-5e0b-4c03-8f22-ca00d3f8f8cc)
![image](https://github.com/Rares1707/Game-of-Life/assets/115061254/6eaa4e30-5e70-48a0-8ddf-1063899c4a97)
![image](https://github.com/Rares1707/Game-of-Life/assets/115061254/0badc3b7-8d2a-4daa-b2ca-1bb4a36e2729)
![image](https://github.com/Rares1707/Game-of-Life/assets/115061254/68c4684a-2901-4c55-be34-e4695606235a)
![image](https://github.com/Rares1707/Game-of-Life/assets/115061254/00e69316-a991-48f3-acdd-56750389770f)
![image](https://github.com/Rares1707/Game-of-Life/assets/115061254/f6799d1e-2151-4177-b176-7c84677f2086)

