## Description
Create a program that will receive as input the 2D coordinates of points A, B, C, and X. Let the coordinates be loaded from a file. The program should:
1. check whether these three points can be the vertices of the rectangle. If they cannot, the program must stop working in a controlled manner and inform the user about the error,
2. check whether point X is inside the rectangle ABC and inform the user about the result,
3. calculate the diagonal of the figure.

Addition
1. depending on points A, B and C, the program should recognize which type of rectangle it is (rectangle or cuboid) and for its execution it should dynamically determine which classes or functions will be called
2. expand the program so that it can support the entry of points A, B, C, D and X, each of which has 3 dimensions. Let the program check whether points A, B, C and D can be vertices of a cube. Let him check if the point X is inside the box ABCD. Let him calculate the spatial diagonal.
3. make the program work with an arbitrary number of dimensions, all from the previous task

Examples of inputs and outputs

Input:
```text
0, 0
5, 0
0, 5
2, 2
```

Output:
True

Input:
```text
0, 0, 0
5, 0, 0
0, 3, 0
0, 0, 1
1, 1, 2
```

Output:
False

## Requirements
- python3

## Flags
- by default runs for taskfiles/input1.txt and appendixfiles/input2.txt
- extrafiles flag with include all txt files in taskfiles and appendixfiles
- debug flag will print extra messages

## Quick Start
```console
$ python3 main.py --debug --extrafiles
```
```console
$ python3 main.py
```
