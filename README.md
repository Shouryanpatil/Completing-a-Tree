# Completing a Tree

This Python script solves the **"Completing a Tree"** problem — determining the minimum number of edges needed to transform a given acyclic graph (forest) into a single connected tree.

## Problem Description

A tree is a connected graph with no cycles and exactly `n - 1` edges for `n` nodes. If a graph is acyclic but not connected, it is a **forest** — a collection of trees.

### Goal:

Given an undirected acyclic graph on `n` nodes, compute the **minimum number of edges** needed to connect all the disconnected components into a **single tree**.

## Approach

1. **Count the number of connected components** using Depth-First Search (DFS).
2. The answer is simply:

   ```
   number_of_components - 1
   ```

## Sample Input

```
n = 10
Edges:
1 2
2 8
4 10
5 9
6 10
7 9
```

## Sample Output

```
3
```

## How to Run

### Requirements

* Python 3.x

### Running the script

1. Clone the repository or download the script.
2. Run:

```bash
python complete_tree.py
```

You can modify the sample input directly in the script to test different cases.

## File Structure

```
.
├── complete_tree.py    # Main script
└── README.md           # This file
```

## License

This project is open source and available under the [MIT License](LICENSE).
