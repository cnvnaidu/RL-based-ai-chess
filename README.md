♟️ Reinforcement Learning-Based Chess AI
A custom-built Reinforcement Learning (RL) agent designed to learn and play chess through self-play, using a simplified environment and reward structure. This project tracks performance over 500 training episodes and identifies the best opening sequence.
Developed under the guidance of Prof. John Pradeep Darsy, VIT-AP.

📌 Table of Contents
About the Project

Key Features

Installation

How to Run

Results & Graphs

Project Structure

Contributors

License

🧠 About the Project
This project implements a Reinforcement Learning agent that trains on a chess environment from scratch using Q-learning. The goal is to complete episodes faster over time and extract the best 8-move opening sequence by the end of training.

✨ Key Features
Self-play based training over 500 episodes

Q-table-based decision making

Tracks:

Win/Draw/Loss trends

Reward progression

Exploration vs Exploitation trade-offs

Q-value distribution

Opening moves frequency

Graphical stats generated for performance evaluation

Automatically prints the best 8 opening moves after each episode and final summary

⚙️ Installation
bash
Copy
Edit
git clone https://github.com/your-username/rl-chess-ai.git
cd rl-chess-ai
pip install -r requirements.txt
Dependencies
Python 3.8+

matplotlib

numpy

seaborn

python-chess

You can install the required packages using:

bash
Copy
Edit
pip install matplotlib numpy seaborn python-chess
▶️ How to Run
1. Train the Agent
bash
Copy
Edit
python main.py
This runs the RL training loop for 500 episodes and logs key metrics including:

Best 8 opening moves per episode

Final best 8-move opening

2. Generate Graphs & Visualizations
After training is complete, you can generate performance graphs:

bash
Copy
Edit
python generate_graphs.py
This script creates the following graphs (saved in /graph_images/ or /mnt/data/):

Learning Curve

Opening Moves Frequency

Performance Improvement

Cumulative Rewards

Best Opening Sequence Progression

Win / Draw / Loss Over Time

Exploration vs Exploitation Trend

Reward Distribution Histogram

Move Count Per Episode

Q-value Distribution

Training Time per Episode

📊 Results & Graphs
✅ Training completed after 500 episodes

🏆 Final Best Opening (8 moves):
['g1h3', 'g8h6', 'h3g5', 'h8g8', 'g5h7', 'g8h8', 'h7f8', 'h8g8']


All graphs are auto-generated and saved for review.

🗂️ Project Structure
bash
Copy
Edit
rl-chess-ai/
│
├── main.py                        # RL agent training and logic
├── utils.py                       # Helper functions
├── generate_graphs.py             # Graph plotting and statistics
├── opening_tracker.py             # Tracks best opening sequences
├── learning_curve.py              # Reward tracking graph (optional)
├── requirements.txt
├── README.md
└── graph_images/                  # Output folder for saved graphs
👨‍💻 Contributors
Supervisor: Prof. John Pradeep Darsy, VIT-AP

CH. Naga Vengama Naidu (22BCE9341) – @minico

G. Manoj Vamsi Reddy (22BCE20281) – @gmanoj

📜 License
This project is licensed for academic and research purposes.
Please cite the contributors if using or building upon this work.
