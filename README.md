# Tucil2_13521051_13521088

## Table of Contents

- [Description](#description)
- [Program Requirements & Installation](#program requirements & installation)
- [Get Started](#get started)
- [Author](#author)

## Description
This is a program to find pair(s) of closest points (by euclidean distance) in n dimensional space. This program use divide & conquer algorithm by splitting points into two regions with a slit and then proceed to find the closest points in either first region, second region, or in the 'crossing-slit' region. This program also implementing brute force algorithm and compare it to the divide & conquer algorithm. The comparison done with two metrics: execution time & the number of euclidean distance operations. For points in 3D and 2D, this program provides visualisation using scatter plot with pair(s) of closest points indicated by different color. This programs also providing coordinates input from file and from randomization.

## Program Requirements & Installation
- Python (all of the current version should be compatible)
https://www.python.org/downloads/
- Matplotlib Library
```markdown
// installation 
python -m pip install -U pip
python -m pip install -U matplotlib
```

## Get Started
1. Run main.py inside the 'src' folder with this command.
  ```markdown
  % python main.py
  ```
2. Enter the dimensions you want to calculate.
3. Enter the number of points you want to calculate.
4. Choose how to generate the points' coordinates.
  ```markdown
  How do you want to input the points' coordinates?
  1. Randomize
  2. Input File
  >>> // input 1 or 2
  ```
5. If you choose to randomize, the program will start the calculation.
6. Else, the program will ask you to input a file path.
7. After the calculation done, pair(s) of closest points and its distance will be outputed. 
8. Then, a visualisation scatter plot will pop up (only for 3D and 2D) with pair(s) of closest points indicated by different color. You can toggle, zoom, configure, and save the plot with provided buttons.
9. To see the comparison between using brute force algorithm and divide and conquer, close the plot.
10. After that you'll be opted to continue other calculation or exot the program.
  ```markdown
  Do you want to do another calculation? (y/n)
  >>> // input 'y' or 'n'
  ```
  
## Author
- Manuella Ivana Uli Sianipar (13521051)
- Puti Nabilla Aidira (13521088)
