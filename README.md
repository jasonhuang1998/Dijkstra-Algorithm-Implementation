# Dijkstra Algorithm Implementation

## Table of Content
- [Introduction](#Introduction)
- [Input File](#Input-File)
- [Input](#Input)
- [Output](#Output)
- [Usage](#Usage)

## Introduction
![](https://i.imgur.com/uZyu0lG.png)
Consider the rectangle graph above, black blocks are regarded as obstacles. X is start coordinate and G is end coordinate. Suppose that the autonomous car can only move in four directions: up, down, left, and right. It moves one space each time, and it is impossible to move on obstacles or boundaries. I implement the Dijkstra Algorithm to find the shortest path betweent start points and end point.
- It is the optimal path searching problem in autonomous cars system with obstacles
- The code for Artificial Intelligence cources at NCUE. 
## Input File
- First line : m n (represent graph format)
- Graph detail is in second line to n+1<sup>th</sup> line
- Each line is a bit string which is m bits long
- Totally n+1 lines in file(including first line : graph format)
- Examples:  
    4 6  
    0000  
    0000  
    0100  
    0100  
    0100  
    0000  
    (The graph size is 4*6, and there are three obstacles located in (2, 1), (3, 1), (4, 1))
## Input
- Start coordinates
- End point coordinates
- ex.
    4 14 12 2
    (start from (4, 14), and end at (12, 2))
## Output
- rectangle graph in bit string on the screen.
- Path parts are marked with different colors.
![](https://i.imgur.com/mzDvQqb.png)

- output path steps by steps(ex. (4, 14)up, (4, 13)up, ...)
- Total number of steps
## Usage
```
python main.py
```

###### tags: `README.md`
@copyright @Jasonkc