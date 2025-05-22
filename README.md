# 🎯 AI Tic-Tac-Toe: Minimax vs Alpha-Beta Pruning

This project implements an AI agent to play Tic-Tac-Toe using two strategies:
- The **Minimax algorithm**
- The **Alpha-Beta Pruning optimized Minimax**

It includes a performance comparison between the two approaches, demonstrating the efficiency gained through pruning unnecessary branches in the game tree.

## 📚 Assignment Overview

**Course:** Artificial Intelligence and Expert System  
**Assignment #02** – CR-22037  
**Author:** Anas Qutbi  
**GitHub:** [Tic-Tac-Toe AI with Minimax and Alpha-Beta Pruning](https://github.com/AnasQutbi/Tic-Tac-Toe-AI-with-Minimax-and-Alpha-Beta-Pruning)  
**YouTube Demo:** [Watch here](https://youtu.be/-TpYLQ9ZEKg)

---

## 🧠 Objectives

- ✅ Implement core logic of Tic-Tac-Toe
- ✅ Develop an AI using the Minimax algorithm
- ✅ Optimize the AI using Alpha-Beta Pruning
- ✅ Compare performance based on time and node exploration
- ✅ Allow user to choose between algorithms before starting

---

## 🕹️ Game Features

- Playable game loop: You (X) vs AI (O)
- Option to choose Alpha-Beta Pruning or standard Minimax
- Interactive board display and user input
- Move validation, win/draw detection
- Performance table at the end showing:
  - Time taken
  - Nodes explored
  - Efficiency improvement

---

## 🧩 Algorithms Used

### 🔁 Minimax
A recursive decision-making algorithm that explores all possible game states to choose the optimal move for the AI.

### ✂️ Alpha-Beta Pruning
An optimization of Minimax that avoids exploring branches that won’t affect the final decision. This significantly reduces computation.

---

## 📊 Sample Performance Comparison

| Algorithm   | Time (s)   | Nodes Explored | Efficiency              |
|-------------|------------|----------------|--------------------------|
| Minimax     | 0.001232   | 549945         | Baseline                |
| Alpha-Beta  | 0.000013   | 1932           | 284.61x fewer nodes     |

(Note: Actual numbers may vary slightly depending on the state of the board.)

---

## ▶️ How to Run

1. Make sure you have Python installed (3.x).
2. Install the required library:
   ```bash
   pip install tabulate
3. python tic_tac_toe_ai.py
