# Chess Engine Using Python

This repository contain chess engine implementation using _Minimax_, _Alpha-Beta pruning_ and **Quiescence search** algorithm. Jupyter notebook inside a Docker Container is used for coding. All Jupyter Notebook are also available in the form of docker image.

Check out the [project paper](project_paper.pdf) to see detailed analysis.

## External Module Used

- [Python Chess](https://python-chess.readthedocs.io/en/latest/)

## How to run using docker

```bash
docker pull codewithnk/chess-engine-using-python:latest
```

```bash
docker run -p 8888:8888 -v $(pwd) codewithnk/chess-engine-using-python:latest
```

## Chess Engine Algorithms

### Minmax

#### Theory

The core of Chess playing Chess in minmax. Minmax usually associates Black piece with MAX, and white piece with MIN, and always evaluates from the white point of view.
<br/>

The Minmax algorithm is an Adversarial Search algorithm in Game theory. It utilizes game tree and includes two player MIN and MAX. Both players try to nullify the action of other. Max tries to maximize the result whereas MIN tries to minimize the result. Both players play alternatively, under the assumption that both are playing optimally. Optimal play means both players are playing as per rule i.e., MIN is minimizing the result and MAX is maximizing the result.
<br/>

The minmax algorithm utilizes Depth First Search approach to find the result. Additionally, it also utilizes backtracking and recursion. Algorithm will traverse till terminal node and then it will backtrack while comparing all child values. It will select the minimum or maximum value, based on whose turn it is. It will then propagate the value back to their parent.
It uses static evaluation function to determine the value at each leaf node. It takes the advantage of Zero-Sum Game.

<br/>

#### Implementation

[Chess Engine using Minmax](chess_engine_using_minmax.ipynb)

<br>

#### Time Complexity

Minmax uses Depth First Search (DFS) on Game Tree, hence the time complexity of minmax algorithm is _O(b\*\*m)_, where b is branching factor of the game-tree, and m is the maximum depth of the tree.

<br>

#### Space Complexity

Space complexity of minmax algorithm is also similar to DFS which is _O(bm)_, where b is branching factor of the game-tree, and m is the maximum depth of the tree.

<br>

#### Completeness

Minmax algorithm is Complete. It will definitely find a solution, if exists, in the finite search tree.

<br>

#### Optimality

Minmax algorithm is optimal if both opponents are playing optimally.

<br>
<hr/>

### Alpha-Beta Pruning

#### Theory

The minmax algorithm can be optimized by pruning few branches. Pruned branches are the ones that are not going to affect result. It will improve time-complexity. This version minmax is knows as minmax with alpha-beta pruning. It is also called as alpha-beta algorithm.
<br/>
In Alpha-Beta Pruning, there are two values, Alpha and Beta. Below are the few points to consider about alpha and beta:

##### Some point about Alpha(α)

- Alpha is the highest value, that is found along the MAX path.
- Initial value of alpha is negative infinity because alpha value will keep on increasing or remain same with every move. If we choose some value other than negative infinity, then the scenario may occur in which all values of alpha may be less than chosen value. So, we have to choose lowest possible value, and that is negative infinity.
- Alpha is only updated by MAX player.

<br>

##### Some points about Beta(β)

- Beta is the lowest value, that is found along the MIN path.
- Initial value of beta is positive infinity because beta value will keep on decreasing or remain same with every move. If we choose some value other than positive infinity, then scenario may occur in which all values of beta may be more than chosen value. So, we have to choose maximum possible value, and that is positive infinity.
- Beta value is only updated by MIN player.

While backtracking only node value is passed to parent, not the alpha and beta value.

The Condition for alpha-beta pruning:

```
α >= β
```

<br>

##### Move Ordering

The effectiveness of alpha-beta algorithm is highly depending on order of traversal. It plays crucial role in Time and Space Complexity.

<br>

###### Worst Ordering

In some cases, no node or sub-tree is pruned out of Game Tree. In this case, best move occurs in right sub-tree of Game Tree. This will result in increased Time Complexity.

<br>

###### Ideal Ordering

In this case, maximum number of node and sub-tree is pruned. Best moves occur in left subtree. It will reduce the Time and Space Complexity.

<br>

#### Implementation

[Chess Engine using Alpha-Beta Pruning](chess_engine_using_alpha_beta_pruning.ipynb)

<br>

#### Time Complexity

Alpha Beta Algorithm, also uses Depth First Search (DFS) on Game Tree.

- In case of Worst Ordering: O(b^m)
- In case of Ideal Ordering: O(b^m/2)

<br>

#### Space Complexity

- In case of Worst Ordering: O(bm)
- In case of Ideal Ordering: O(b(m/2))

<br>

#### Completeness

Alpha-Beta algorithm is Complete. It will definitely find a solution, if exists, in the finite search tree.

<br>

#### Optimality

Alpha-Beta algorithm is optimal if both opponents are playing optimally.

<br>
<br>
<hr/>

### Quiescence Search

Quiescence Search is a modification on top of alpha-beta pruning with min-max. Quiescence means quiet. This search only evaluates only quiet moves. In other words, after a certain depth, it only uses capture moves to calculate the next moves. A quiescence search can avoid the horizon effect.
<br>
The horizon effect occurs when we only search to a certain depth, but it may happen that if we look one more level deep, then move may score fewer points. A quiescence search only uses capture moves to prevent this.
Quiescence search also reduces the branching factor at different levels, resulting in a fast algorithm.

<br>

#### Time Complexity

Quiescence Search Algorithm, also uses Depth First Search (DFS) on Game Tree.

- In case of Worst Ordering: O(b^m)
- In case of Ideal Ordering: O(b^m/2)

<br>

#### Space Complexity

- In case of Worst Ordering: O(bm)
- In case of Ideal Ordering: O(b(m/2))

<br>

#### Completeness

Quiescence Search algorithm is Complete. It will definitely find a solution, if exists, in the finite search tree.

#### Optimality

Quiescence Search algorithm is optimal if both opponents are playing optimally.

<br>
<br>
<hr/>

## Key Takeaway

- Nodes explored per move is reduced by 10 folds in Alpha Beta as compared with Minmax.
- Time Taken to find best move is also reduced by 10 folds in Alpha Beta as compared with Minmax.
- Quiescence search performs well in higher depth.
- Quiescence search is the fastest algorithm out of all three.
- Quiescence search evaluates less nodes.
- Quiescence search may result in repeated moves, if not handled properly.
