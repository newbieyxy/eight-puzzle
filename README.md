## eight-puzzle

Three searching methods are used for solving eight-puzzle problem: IDS(iterative deepening search), greedy search, A* search. There are two different kinds of heuristic function: 1) sum of Manhattan distance 2) count of misplaced digits.

#### IDS

```bash
python main.py --method IDS --test-num 50
```
#### Greedy search

```bash
python main.py --method Greedy --test-num 50
```
#### A* with sum of Manhattan distance

```bash
python main.py --method AStar_man --test-num 50
```
#### A* with count of misplaced digits

```bash
python main.py --method AStar_mis --test-num 50
```
