import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Sample simulated data for demonstration
episodes = np.arange(1, 501)
np.random.seed(42)

# 6. Win / Draw / Loss Ratio Over Episodes
wins = np.random.randint(0, 2, 500)
draws = np.random.randint(0, 2, 500)
losses = 1 - (wins + draws)
wins[wins + draws > 1] = 0  # Make sure only one per game
draws[wins + draws > 1] = 0
losses = 1 - (wins + draws)

# 7. Exploration vs Exploitation Rate
exploration_rate = np.linspace(1, 0.1, 500)
exploitation_rate = 1 - exploration_rate

# 8. Reward Distribution Histogram
rewards = np.random.normal(loc=0, scale=10, size=500)

# 9. Move Count Per Game
move_counts = np.random.randint(10, 80, 500)

# 10. Q-Value Distribution Plot (simulated Q-values)
q_values = np.random.normal(loc=0, scale=1, size=1000)

# 12. Training Time Per Episode
training_times = np.random.normal(loc=0.05, scale=0.01, size=500)  # In seconds

# Plotting

# Win/Draw/Loss Plot
plt.figure(figsize=(10, 4))
plt.plot(episodes, np.cumsum(wins), label='Wins')
plt.plot(episodes, np.cumsum(draws), label='Draws')
plt.plot(episodes, np.cumsum(losses), label='Losses')
plt.xlabel("Episodes")
plt.ylabel("Cumulative Count")
plt.title("Win/Draw/Loss Over Episodes")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("win_draw_loss_over_episodes.png")
plt.close()

# Exploration vs Exploitation Plot
plt.figure(figsize=(10, 4))
plt.plot(episodes, exploration_rate, label="Exploration Rate")
plt.plot(episodes, exploitation_rate, label="Exploitation Rate")
plt.xlabel("Episodes")
plt.ylabel("Rate")
plt.title("Exploration vs Exploitation Over Time")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("exploration_vs_exploitation.png")
plt.close()

# Reward Distribution Histogram
plt.figure(figsize=(8, 4))
sns.histplot(rewards, kde=True, bins=30, color='skyblue')
plt.title("Reward Distribution Across Episodes")
plt.xlabel("Reward")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("reward_distribution.png")
plt.close()

# Move Count Per Game
plt.figure(figsize=(10, 4))
plt.plot(episodes, move_counts, color='orange')
plt.xlabel("Episode")
plt.ylabel("Move Count")
plt.title("Number of Moves Per Game")
plt.grid(True)
plt.tight_layout()
plt.savefig("move_count_per_game.png")
plt.close()

# Q-Value Distribution
plt.figure(figsize=(8, 4))
sns.histplot(q_values, kde=True, bins=30, color='green')
plt.title("Distribution of Q-Values")
plt.xlabel("Q-value")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("q_value_distribution.png")
plt.close()

# Training Time Per Episode
plt.figure(figsize=(10, 4))
plt.plot(episodes, training_times, color='purple')
plt.xlabel("Episode")
plt.ylabel("Training Time (s)")
plt.title("Training Time Per Episode")
plt.grid(True)
plt.tight_layout()
plt.savefig("training_time_per_episode.png")
plt.close()